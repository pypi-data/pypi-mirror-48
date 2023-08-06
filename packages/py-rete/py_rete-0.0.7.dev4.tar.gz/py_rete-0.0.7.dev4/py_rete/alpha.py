class ConstantTestNode:
    """
    This node tests that a particular field equals a particular constant.
    """

    def __init__(self, field_to_test, field_must_equal=None, amem=None,
                 children=None):
        """
        :type field_to_test: str
        :type children: list of ConstantTestNode
        :type amem: AlphaMemory
        """
        self.field_to_test = field_to_test
        self.field_must_equal = field_must_equal
        self.amem = amem
        self.children = children if children else []

    def __repr__(self):
        return "<ConstantTestNode %s=%s?>" % (self.field_to_test,
                                              self.field_must_equal)

    def dump(self):
        return "%s=%s?" % (self.field_to_test, self.field_must_equal)

    def activation(self, wme):
        """
        If the node is a valid test (not no-test), then check it against the
        provided WME. If it passes and points to an alpha memory, then activate
        the alpha memory with the wme. If it passes and points to additional
        constant test nodes, then activate those with the wme too.

        :type wme: rete.WME
        """
        if self.field_to_test != 'no-test':
            v = getattr(wme, self.field_to_test)
            if v != self.field_must_equal:
                return False
        if self.amem:
            self.amem.activation(wme)
        for child in self.children:
            child.activation(wme)

    @classmethod
    def build_or_share_alpha_memory(cls, node, path=[]):
        """
        :type node: ConstantTestNode
        :type path: [(field, value)...]
        :rtype: AlphaMemory
        """
        if not len(path):
            if node.amem:
                return node.amem
            else:
                am = AlphaMemory()
                node.amem = am
                return am
        f, v = path.pop(0)
        fields = ['identifier', 'attribute', 'value']
        assert f in fields, "`%s` not in %s" % (f, fields)
        next_node = cls.build_or_share_constant_test_node(node, f, v)
        return cls.build_or_share_alpha_memory(next_node, path)

    @classmethod
    def build_or_share_constant_test_node(cls, parent, field, symbol):
        """
        :rtype: ConstantTestNode
        :type symbol: str
        :type field: str
        :type parent: ConstantTestNode
        """
        for child in parent.children:
            if (child.field_to_test == field and child.field_must_equal ==
                    symbol):
                return child
        new_node = ConstantTestNode(field, symbol, children=[])
        parent.children.append(new_node)
        return new_node


class AlphaMemory:

    def __init__(self, items=None, successors=None):
        """
        Stores a set of WMEs (items). If activating an activated wme does not
        exist, then it addes it. It also right activates all of its successors,
        which correspond ot beta nodes.

        TODO:
            - replace self.items with a set rather than a list?
            - why are beta nodes (successors) activated in reverse order?

        :type successors: list of BetaNode
        :type items: list of rete.WME
        """
        self.items = items if items else []
        self.successors = successors if successors else []

    def activation(self, wme):
        """
        :type wme: rete.WME
        """
        if wme in self.items:
            return
        self.items.append(wme)
        wme.amems.append(self)
        for child in reversed(self.successors):
            child.right_activation(wme)
