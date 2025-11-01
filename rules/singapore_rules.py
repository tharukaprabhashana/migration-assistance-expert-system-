# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class SingaporeRules:
    """Rules for Singapore"""
    @Rule(Person(preferred_country='Singapore', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def singapore_strong(self):
        self.declare(Fact(eligibility=('Singapore', 'TopPath', 0.95)))
        self.declare(Fact(points=('Singapore', 80)))
        self.declare(Fact(explanation="Singapore: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Singapore', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def singapore_medium(self):
        self.declare(Fact(eligibility=('Singapore', 'MidPath', 0.85)))
        self.declare(Fact(points=('Singapore', 65)))
        self.declare(Fact(explanation="Singapore: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Singapore', role='student'), salience=60)
    def singapore_student(self):
        self.declare(Fact(eligibility=('Singapore', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Singapore', 35)))
        self.declare(Fact(explanation="Singapore: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Singapore', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def singapore_it(self):
        self.declare(Fact(add_points=('Singapore','IT', 12)))
        self.declare(Fact(explanation="Singapore: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Singapore', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def singapore_engineering(self):
        self.declare(Fact(add_points=('Singapore','Engineering', 10)))
        self.declare(Fact(explanation="Singapore: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Singapore', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def singapore_healthcare(self):
        self.declare(Fact(add_points=('Singapore','Healthcare', 10)))
        self.declare(Fact(explanation="Singapore: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Singapore', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def singapore_business(self):
        self.declare(Fact(add_points=('Singapore','Business', 12)))
        self.declare(Fact(explanation="Singapore: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Singapore', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def singapore_hospitality(self):
        self.declare(Fact(add_points=('Singapore','Hospitality', 8)))
        self.declare(Fact(explanation="Singapore: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Singapore', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def singapore_research(self):
        self.declare(Fact(add_points=('Singapore','Research', 10)))
        self.declare(Fact(explanation="Singapore: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Singapore', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def singapore_spouse_edu(self):
        self.declare(Fact(add_points=('Singapore','SpouseEducation', 15)))
        self.declare(Fact(explanation="Singapore: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Singapore', has_spouse=True, spouse_is_working=True))
    def singapore_spouse_work(self):
        self.declare(Fact(add_points=('Singapore','SpouseWorking', 10)))
        self.declare(Fact(explanation="Singapore: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Singapore', salary_local=P(lambda s: s is not None and s >= 5000)), salience=30)
    def singapore_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Singapore: reported salary meets conservative threshold (5000 SGD)."))

    @Rule(Person(preferred_country='Singapore', num_children=P(lambda n: n is not None and n > 0)))
    def singapore_dependent(self):
        self.declare(Fact(dependent_possible=('Singapore', True)))
        self.declare(Fact(explanation="Singapore: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Singapore'))
    def singapore_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Japan']))
        self.declare(Fact(explanation="Singapore: suggested alternative countries based on climate/culture group."))


# end of Singapore
