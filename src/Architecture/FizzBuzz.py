import abc


class AbstractRule:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        print "Initiating Abstract Rule Class"

    @abc.abstractmethod
    def match(self, element):
        return False

    @abc.abstractmethod
    def replace(self):
        return ""


class RuleFactory:
    def __init__(self):
        print "Initiating Rule Factory"
        self.rules = []

    def add_rules(self, rule):
        self.rules.append(rule)

    def get_rules(self):
        return self.rules


class FizzRule(AbstractRule):
    def __init__(self):
        print "Initiating Fizz Rule Class"

    def match(self, element):
        if element % 5 == 0:
            return True

        return False

    def replace(self):
        return 'Fizz'


class BuzzRule(AbstractRule):
    def __init__(self):
        print "Initiating Buzz Rule Class"

    def match(self, element):
        if element % 3 == 0:
            return True

        return False

    def replace(self):
        return 'Buzz'


class FizzBuzzRule(AbstractRule):
    def __init__(self):
        print "Initiating FizzBuzz Rule Class"

    def match(self, element):
        if element % 3 == 0 and element%5 == 0:
            return True

        return False

    def replace(self):
        return 'FizzBuzz'


class FizzBuzzRunner:
    def __init__(self):
        print "Fizz Buzz Runner"

        factory = RuleFactory()
        factory.add_rules(FizzBuzzRule())
        factory.add_rules(FizzRule())
        factory.add_rules(BuzzRule())
        self.rules = factory.get_rules()
        self.answer_list = []

    def generate(self):
        for x in xrange(1, 101):
            for rule in self.rules:
                if rule.match(x):
                    self.answer_list.append(rule.replace())
                    break
            self.answer_list.append(x)

        return self.answer_list


print FizzBuzzRunner().generate()
