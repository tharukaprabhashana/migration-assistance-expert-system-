# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class SwedenRules:
    """Rules for Sweden"""
    @Rule(Person(preferred_country='Sweden', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def sweden_strong(self):
        self.declare(Fact(eligibility=('Sweden', 'TopPath', 0.95)))
        self.declare(Fact(points=('Sweden', 80)))
        self.declare(Fact(explanation="Sweden: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Sweden', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def sweden_medium(self):
        self.declare(Fact(eligibility=('Sweden', 'MidPath', 0.85)))
        self.declare(Fact(points=('Sweden', 65)))
        self.declare(Fact(explanation="Sweden: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Sweden', role='student'), salience=60)
    def sweden_student(self):
        self.declare(Fact(eligibility=('Sweden', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Sweden', 35)))
        self.declare(Fact(explanation="Sweden: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Sweden', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def sweden_it(self):
        self.declare(Fact(add_points=('Sweden','IT', 11)))
        self.declare(Fact(explanation="Sweden: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Sweden', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def sweden_engineering(self):
        self.declare(Fact(add_points=('Sweden','Engineering', 11)))
        self.declare(Fact(explanation="Sweden: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Sweden', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def sweden_healthcare(self):
        self.declare(Fact(add_points=('Sweden','Healthcare', 10)))
        self.declare(Fact(explanation="Sweden: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Sweden', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def sweden_business(self):
        self.declare(Fact(add_points=('Sweden','Business', 10)))
        self.declare(Fact(explanation="Sweden: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Sweden', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def sweden_hospitality(self):
        self.declare(Fact(add_points=('Sweden','Hospitality', 6)))
        self.declare(Fact(explanation="Sweden: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Sweden', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def sweden_research(self):
        self.declare(Fact(add_points=('Sweden','Research', 11)))
        self.declare(Fact(explanation="Sweden: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Sweden', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def sweden_spouse_edu(self):
        self.declare(Fact(add_points=('Sweden','SpouseEducation', 15)))
        self.declare(Fact(explanation="Sweden: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Sweden', has_spouse=True, spouse_is_working=True))
    def sweden_spouse_work(self):
        self.declare(Fact(add_points=('Sweden','SpouseWorking', 10)))
        self.declare(Fact(explanation="Sweden: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Sweden', salary_local=P(lambda s: s is not None and s >= 350000)), salience=30)
    def sweden_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Sweden: reported salary meets conservative threshold (350000 SEK)."))

    @Rule(Person(preferred_country='Sweden', num_children=P(lambda n: n is not None and n > 0)))
    def sweden_dependent(self):
        self.declare(Fact(dependent_possible=('Sweden', True)))
        self.declare(Fact(explanation="Sweden: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Sweden'))
    def sweden_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Norway', 'Finland', 'Denmark']))
        self.declare(Fact(explanation="Sweden: suggested alternative countries based on climate/culture group."))


# end of Sweden
