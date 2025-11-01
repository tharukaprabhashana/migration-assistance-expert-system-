# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class DenmarkRules:
    """Rules for Denmark"""
    @Rule(Person(preferred_country='Denmark', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def denmark_strong(self):
        self.declare(Fact(eligibility=('Denmark', 'TopPath', 0.95)))
        self.declare(Fact(points=('Denmark', 80)))
        self.declare(Fact(explanation="Denmark: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Denmark', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def denmark_medium(self):
        self.declare(Fact(eligibility=('Denmark', 'MidPath', 0.85)))
        self.declare(Fact(points=('Denmark', 65)))
        self.declare(Fact(explanation="Denmark: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Denmark', role='student'), salience=60)
    def denmark_student(self):
        self.declare(Fact(eligibility=('Denmark', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Denmark', 35)))
        self.declare(Fact(explanation="Denmark: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Denmark', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def denmark_it(self):
        self.declare(Fact(add_points=('Denmark','IT', 11)))
        self.declare(Fact(explanation="Denmark: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Denmark', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def denmark_engineering(self):
        self.declare(Fact(add_points=('Denmark','Engineering', 12)))
        self.declare(Fact(explanation="Denmark: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Denmark', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def denmark_healthcare(self):
        self.declare(Fact(add_points=('Denmark','Healthcare', 11)))
        self.declare(Fact(explanation="Denmark: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Denmark', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def denmark_business(self):
        self.declare(Fact(add_points=('Denmark','Business', 10)))
        self.declare(Fact(explanation="Denmark: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Denmark', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def denmark_hospitality(self):
        self.declare(Fact(add_points=('Denmark','Hospitality', 6)))
        self.declare(Fact(explanation="Denmark: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Denmark', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def denmark_research(self):
        self.declare(Fact(add_points=('Denmark','Research', 10)))
        self.declare(Fact(explanation="Denmark: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Denmark', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def denmark_spouse_edu(self):
        self.declare(Fact(add_points=('Denmark','SpouseEducation', 15)))
        self.declare(Fact(explanation="Denmark: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Denmark', has_spouse=True, spouse_is_working=True))
    def denmark_spouse_work(self):
        self.declare(Fact(add_points=('Denmark','SpouseWorking', 10)))
        self.declare(Fact(explanation="Denmark: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Denmark', salary_local=P(lambda s: s is not None and s >= 330000)), salience=30)
    def denmark_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Denmark: reported salary meets conservative threshold (330000 DKK)."))

    @Rule(Person(preferred_country='Denmark', num_children=P(lambda n: n is not None and n > 0)))
    def denmark_dependent(self):
        self.declare(Fact(dependent_possible=('Denmark', True)))
        self.declare(Fact(explanation="Denmark: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Denmark'))
    def denmark_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Norway', 'Sweden', 'Finland']))
        self.declare(Fact(explanation="Denmark: suggested alternative countries based on climate/culture group."))


# end of Denmark
