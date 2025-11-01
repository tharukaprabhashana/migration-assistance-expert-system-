# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class NewZealandRules:
    """Rules for New Zealand"""
    @Rule(Person(preferred_country='New Zealand', education='PhD', ielts=P(lambda x: x is not None and x >= 6.5), experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def new_zealand_strong(self):
        self.declare(Fact(eligibility=('New Zealand', 'TopPath', 0.95)))
        self.declare(Fact(points=('New Zealand', 80)))
        self.declare(Fact(explanation="New Zealand: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', education='Masters', ielts=P(lambda x: x is not None and x >= 6.0), experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def new_zealand_medium(self):
        self.declare(Fact(eligibility=('New Zealand', 'MidPath', 0.85)))
        self.declare(Fact(points=('New Zealand', 65)))
        self.declare(Fact(explanation="New Zealand: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', role='student'), salience=60)
    def new_zealand_student(self):
        self.declare(Fact(eligibility=('New Zealand', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('New Zealand', 35)))
        self.declare(Fact(explanation="New Zealand: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def new_zealand_it(self):
        self.declare(Fact(add_points=('New Zealand','IT', 10)))
        self.declare(Fact(explanation="New Zealand: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def new_zealand_engineering(self):
        self.declare(Fact(add_points=('New Zealand','Engineering', 11)))
        self.declare(Fact(explanation="New Zealand: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def new_zealand_healthcare(self):
        self.declare(Fact(add_points=('New Zealand','Healthcare', 13)))
        self.declare(Fact(explanation="New Zealand: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def new_zealand_business(self):
        self.declare(Fact(add_points=('New Zealand','Business', 7)))
        self.declare(Fact(explanation="New Zealand: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def new_zealand_hospitality(self):
        self.declare(Fact(add_points=('New Zealand','Hospitality', 6)))
        self.declare(Fact(explanation="New Zealand: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def new_zealand_research(self):
        self.declare(Fact(add_points=('New Zealand','Research', 9)))
        self.declare(Fact(explanation="New Zealand: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='New Zealand', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def new_zealand_spouse_edu(self):
        self.declare(Fact(add_points=('New Zealand','SpouseEducation', 15)))
        self.declare(Fact(explanation="New Zealand: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='New Zealand', has_spouse=True, spouse_is_working=True))
    def new_zealand_spouse_work(self):
        self.declare(Fact(add_points=('New Zealand','SpouseWorking', 10)))
        self.declare(Fact(explanation="New Zealand: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='New Zealand', salary_local=P(lambda s: s is not None and s >= 42000)), salience=30)
    def new_zealand_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="New Zealand: reported salary meets conservative threshold (42000 NZD)."))

    @Rule(Person(preferred_country='New Zealand', num_children=P(lambda n: n is not None and n > 0)))
    def new_zealand_dependent(self):
        self.declare(Fact(dependent_possible=('New Zealand', True)))
        self.declare(Fact(explanation="New Zealand: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='New Zealand'))
    def new_zealand_alternatives(self):
        self.declare(Fact(alternative_suggestions=['United Kingdom', 'United States', 'Canada', 'Australia']))
        self.declare(Fact(explanation="New Zealand: suggested alternative countries based on climate/culture group."))


# end of New Zealand
