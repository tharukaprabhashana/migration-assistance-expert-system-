# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class ItalyRules:
    """Rules for Italy"""
    @Rule(Person(preferred_country='Italy', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def italy_strong(self):
        self.declare(Fact(eligibility=('Italy', 'TopPath', 0.95)))
        self.declare(Fact(points=('Italy', 80)))
        self.declare(Fact(explanation="Italy: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Italy', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def italy_medium(self):
        self.declare(Fact(eligibility=('Italy', 'MidPath', 0.85)))
        self.declare(Fact(points=('Italy', 65)))
        self.declare(Fact(explanation="Italy: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Italy', role='student'), salience=60)
    def italy_student(self):
        self.declare(Fact(eligibility=('Italy', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Italy', 35)))
        self.declare(Fact(explanation="Italy: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Italy', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def italy_it(self):
        self.declare(Fact(add_points=('Italy','IT', 8)))
        self.declare(Fact(explanation="Italy: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Italy', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def italy_engineering(self):
        self.declare(Fact(add_points=('Italy','Engineering', 10)))
        self.declare(Fact(explanation="Italy: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Italy', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def italy_healthcare(self):
        self.declare(Fact(add_points=('Italy','Healthcare', 8)))
        self.declare(Fact(explanation="Italy: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Italy', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def italy_business(self):
        self.declare(Fact(add_points=('Italy','Business', 7)))
        self.declare(Fact(explanation="Italy: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Italy', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def italy_hospitality(self):
        self.declare(Fact(add_points=('Italy','Hospitality', 8)))
        self.declare(Fact(explanation="Italy: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Italy', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def italy_research(self):
        self.declare(Fact(add_points=('Italy','Research', 10)))
        self.declare(Fact(explanation="Italy: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Italy', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def italy_spouse_edu(self):
        self.declare(Fact(add_points=('Italy','SpouseEducation', 15)))
        self.declare(Fact(explanation="Italy: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Italy', has_spouse=True, spouse_is_working=True))
    def italy_spouse_work(self):
        self.declare(Fact(add_points=('Italy','SpouseWorking', 10)))
        self.declare(Fact(explanation="Italy: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Italy', salary_local=P(lambda s: s is not None and s >= 30000)), salience=30)
    def italy_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Italy: reported salary meets conservative threshold (30000 EUR)."))

    @Rule(Person(preferred_country='Italy', num_children=P(lambda n: n is not None and n > 0)))
    def italy_dependent(self):
        self.declare(Fact(dependent_possible=('Italy', True)))
        self.declare(Fact(explanation="Italy: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Italy'))
    def italy_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Germany', 'France', 'Netherlands', 'Latvia']))
        self.declare(Fact(explanation="Italy: suggested alternative countries based on climate/culture group."))


# end of Italy
