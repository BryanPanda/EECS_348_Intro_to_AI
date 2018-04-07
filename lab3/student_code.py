import read, copy
from util import *
from logical_classes import *

verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB

        Args:
            fact_rule (Fact|Rule) - the fact or rule to be added

        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)

        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)

    def kb_assert(self, statement):
        """Assert a fact or rule into the KB

        Args:
            statement (Statement): Statement we're asserting in the format produced by read.py
        """
        printv("Asserting {!r}", 0, verbose, [statement])
        self.kb_add(Fact(statement) if factq(statement) else Rule(statement))

    def kb_ask(self, statement):
        """Ask if a fact is in the KB

        Args:
            statement (Statement) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        printv("Asking {!r}", 0, verbose, [statement])
        if factq(statement):
            f = Fact(statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else False

        else:
            print "Invalid ask:", statement
            return False

    def kb_retract(self, statement):
        """Retract a fact from the KB

        Args:
            statement (Statement) - Statement to be asked (will be converted into a Fact)

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [statement])
        ####################################################
        # Student code goes here
        if factq(statement): #statement is fact
            for fact in self.facts:
                if fact.supported_by == [] and fact.statement == Statement(statement):
                    self.facts.remove(fact)
                    # facts supported by this fact
                    for supports_fact in fact.supports_facts:
                        for each in supports_fact.supported_by:
                            if fact in each:
                                # each is the a [rule, fact] list that support this rule
                                each[0].supports_facts.remove(supports_fact)
                                supports_fact.supported_by.remove(each)
                        if supports_fact.supported_by == [] and not supports_fact.asserted:
                            new_statement = [supports_fact.statement.predicate]
                            # convert term to element
                            for each in supports_fact.statement.terms:
                                new_statement.append(each.term.element)
                            self.kb_retract(new_statement)
                    # rules supported by this fact
                    for supports_rule in fact.supports_rules:
                        for each in supports_rule.supported_by:
                            if fact in each:
                                each[0].supports_rules.remove(supports_rule)
                                supports_rule.supported_by.remove(each)
                        if supports_rule.supported_by == [] and not supports_rule.asserted:
                            new_statement = [supports_rule.lhs, supports_rule.rhs]
                            self.kb_retract(new_statement)
        else: # statment is rule
            for rule in self.rules:
                if rule.supported_by == [] and [rule.lhs, rule.rhs] == statement:
                    self.rules.remove(rule)
                    # facts supported by this rule
                    for supports_fact in rule.supports_facts:
                        for each in supports_fact.supported_by:
                            if rule in each:
                                # each is the a [rule, fact] list that support this rule
                                each[1].supports_facts.remove(supports_fact)
                                supports_fact.supported_by.remove(each)
                        if supports_fact.supported_by == [] and not supports_fact.asserted:
                            new_statement = [supports_fact.statement.predicate]
                            # convert term to element
                            for each in supports_fact.statement.terms:
                                new_statement.append(each.term.element)
                            self.kb_retract(new_statement)
                    # rules supported by this rule
                    for supports_rule in rule.supports_rules:
                        for each in supports_rule.supported_by:
                            if rule in each:
                                each[1].supports_rules.remove(supports_rule)
                                supports_rule.supported_by.remove(each)
                        if supports_rule.supported_by == [] and not supports_rule.asserted:
                            new_statement = [supports_rule.lhs, supports_rule.rhs]
                            self.kb_retract(new_statement)

class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing            
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        # Student code goes here
        bindings = match(fact.statement, rule.lhs[0])

        if bindings:
            supported_by = [[rule, fact]]
            new_rhs = instantiate(rule.rhs, bindings)
            if len(rule.lhs) == 1:
                # construct new fact
                new_fact = Fact(new_rhs, supported_by)
                # add supports
                fact.supports_facts.append(new_fact)
                rule.supports_facts.append(new_fact)
                # add to kb
                kb.kb_add(new_fact)
            else:
                # construct new rule
                new_lhs = []
                for each in rule.lhs[1:]:
                    new_lhs.append(instantiate(each, bindings))
                # new_rhs = instantiate(rule.rhs, bindings)
                new_rule = Rule([new_lhs, new_rhs], supported_by)
                # add supports
                fact.supports_rules.append(new_rule)
                rule.supports_rules.append(new_rule)
                # add new rule to kb
                kb.kb_add(new_rule)