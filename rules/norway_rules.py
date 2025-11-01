# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class NorwayRules:
    """Rules for Norway"""
    @Rule(Person(preferred_country='Norway', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def norway_strong(self):
        self.declare(Fact(eligibility=('Norway', 'TopPath', 0.95)))
        self.declare(Fact(points=('Norway', 80)))
        self.declare(Fact(explanation="Norway: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Norway', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def norway_medium(self):
        self.declare(Fact(eligibility=('Norway', 'MidPath', 0.85)))
        self.declare(Fact(points=('Norway', 65)))
        self.declare(Fact(explanation="Norway: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Norway', role='student'), salience=60)
    def norway_student(self):
        self.declare(Fact(eligibility=('Norway', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Norway', 35)))
        self.declare(Fact(explanation="Norway: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Norway', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def norway_it(self):
        self.declare(Fact(add_points=('Norway','IT', 12)))
        self.declare(Fact(explanation="Norway: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Norway', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def norway_engineering(self):
        self.declare(Fact(add_points=('Norway','Engineering', 12)))
        self.declare(Fact(explanation="Norway: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Norway', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def norway_healthcare(self):
        self.declare(Fact(add_points=('Norway','Healthcare', 12)))
        self.declare(Fact(explanation="Norway: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Norway', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def norway_business(self):
        self.declare(Fact(add_points=('Norway','Business', 10)))
        self.declare(Fact(explanation="Norway: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Norway', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def norway_hospitality(self):
        self.declare(Fact(add_points=('Norway','Hospitality', 7)))
        self.declare(Fact(explanation="Norway: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Norway', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def norway_research(self):
        self.declare(Fact(add_points=('Norway','Research', 11)))
        self.declare(Fact(explanation="Norway: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Norway', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def norway_spouse_edu(self):
        self.declare(Fact(add_points=('Norway','SpouseEducation', 15)))
        self.declare(Fact(explanation="Norway: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Norway', has_spouse=True, spouse_is_working=True))
    def norway_spouse_work(self):
        self.declare(Fact(add_points=('Norway','SpouseWorking', 10)))
        self.declare(Fact(explanation="Norway: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Norway', salary_local=P(lambda s: s is not None and s >= 450000)), salience=30)
    def norway_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Norway: reported salary meets conservative threshold (450000 NOK)."))

    @Rule(Person(preferred_country='Norway', num_children=P(lambda n: n is not None and n > 0)))
    def norway_dependent(self):
        self.declare(Fact(dependent_possible=('Norway', True)))
        self.declare(Fact(explanation="Norway: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Norway'))
    def norway_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Sweden', 'Finland', 'Denmark']))
        self.declare(Fact(explanation="Norway: suggested alternative countries based on climate/culture group."))


# end of Norway
