import re

from ucca.layer1 import EdgeTags

from .dep import DependencyConverter


class ConllConverter(DependencyConverter):
    def __init__(self, *args, tree=True, **kwargs):
        if "format" not in kwargs:
            kwargs["format"] = "conll"
        super().__init__(*args, tree=tree, **kwargs)

    def read_line(self, line, previous_node, copy_of):
        fields = self.split_line(line)
        # id, form, lemma, coarse pos, fine pos, features, head, relation, [enhanced], [misc]
        position, text, lemma, pos, tag, features, head_position, rel, *enhanced_misc = fields[:10]
        edges = []
        if head_position and head_position != "_":
            edges.append(self.Edge.create(head_position, rel))
        if len(enhanced_misc) < 1 or enhanced_misc[0] == "_":
            enhanced = "_"
        elif self.enhanced:
            enhanced = enhanced_misc[0]
            for enhanced_spec in enhanced.split("|"):
                enhanced_head_position, _, enhanced_rel = enhanced_spec.partition(":")
                if enhanced_head_position not in (position, head_position):
                    edges.append(self.Edge(enhanced_head_position, enhanced_rel, remote=True))
        else:
            enhanced = None
        if len(enhanced_misc) < 2 or enhanced_misc[1] == "_":
            misc = "_"
        else:
            misc = enhanced_misc[1]
            m = re.match(r"CopyOf=(\d+)", misc)
            if m:
                copy_of[position] = m.group(1)
        if "." in position:
            return None
        span = list(map(int, position.split("-")))
        if not edges or previous_node is None or previous_node.position != span[0]:
            return self.Node(None if len(span) > 1 else span[0], edges,
                             token=self.Token(text, tag, lemma, pos, features),
                             is_multi_word=len(span) > 1, enhanced=enhanced, misc=misc, span=span)
        previous_node.add_edges(edges)

    def generate_lines(self, graph, test):
        yield from super().generate_lines(graph, test)
        # id, form, lemma, coarse pos, fine pos, features
        for i, dep_node in enumerate(graph.nodes):
            position = i + 1
            assert position == dep_node.position
            if dep_node.parent_multi_word and position == dep_node.parent_multi_word.span[0]:
                yield ["-".join(map(str, dep_node.parent_multi_word.span)),
                       dep_node.parent_multi_word.token.text] + 8 * ["_"]
            fields = [position, dep_node.token.text, dep_node.token.lemma, dep_node.token.pos, dep_node.token.tag,
                      dep_node.token.features]
            if test:
                yield fields + 4 * ["_"]  # head, relation, enhanced, misc
            else:
                heads = [(e.head_index, e.rel + ("*" if e.remote else "")) for e in dep_node.incoming] or \
                        [(0, self.ROOT)]
                if self.tree:
                    heads = [heads[0]]
                for head in heads:
                    yield fields + list(head) + [dep_node.enhanced, dep_node.misc]

    def generate_header_lines(self, graph):
        yield from super().generate_header_lines(graph)
        yield ["# sent_id = " + graph.id]

    def omit_edge(self, edge, linkage=False):
        return (self.tree or not linkage) and edge.tag in (EdgeTags.LinkRelation, EdgeTags.LinkArgument)
