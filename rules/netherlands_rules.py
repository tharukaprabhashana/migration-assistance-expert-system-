# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class NetherlandsRules:
    """Rules for Netherlands"""
    @Rule(Person(preferred_country='Netherlands', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def netherlands_strong(self):
        self.declare(Fact(eligibility=('Netherlands', 'TopPath', 0.95)))
        self.declare(Fact(points=('Netherlands', 80)))
        self.declare(Fact(explanation="Netherlands: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def netherlands_medium(self):
        self.declare(Fact(eligibility=('Netherlands', 'MidPath', 0.85)))
        self.declare(Fact(points=('Netherlands', 65)))
        self.declare(Fact(explanation="Netherlands: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', role='student'), salience=60)
    def netherlands_student(self):
        self.declare(Fact(eligibility=('Netherlands', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Netherlands', 35)))
        self.declare(Fact(explanation="Netherlands: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def netherlands_it(self):
        self.declare(Fact(add_points=('Netherlands','IT', 12)))
        self.declare(Fact(explanation="Netherlands: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def netherlands_engineering(self):
        self.declare(Fact(add_points=('Netherlands','Engineering', 12)))
        self.declare(Fact(explanation="Netherlands: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def netherlands_healthcare(self):
        self.declare(Fact(add_points=('Netherlands','Healthcare', 10)))
        self.declare(Fact(explanation="Netherlands: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def netherlands_business(self):
        self.declare(Fact(add_points=('Netherlands','Business', 12)))
        self.declare(Fact(explanation="Netherlands: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def netherlands_hospitality(self):
        self.declare(Fact(add_points=('Netherlands','Hospitality', 6)))
        self.declare(Fact(explanation="Netherlands: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def netherlands_research(self):
        self.declare(Fact(add_points=('Netherlands','Research', 11)))
        self.declare(Fact(explanation="Netherlands: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Netherlands', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def netherlands_spouse_edu(self):
        self.declare(Fact(add_points=('Netherlands','SpouseEducation', 15)))
        self.declare(Fact(explanation="Netherlands: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Netherlands', has_spouse=True, spouse_is_working=True))
    def netherlands_spouse_work(self):
        self.declare(Fact(add_points=('Netherlands','SpouseWorking', 10)))
        self.declare(Fact(explanation="Netherlands: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Netherlands', salary_local=P(lambda s: s is not None and s >= 38000)), salience=30)
    def netherlands_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Netherlands: reported salary meets conservative threshold (38000 EUR)."))

    @Rule(Person(preferred_country='Netherlands', num_children=P(lambda n: n is not None and n > 0)))
    def netherlands_dependent(self):
        self.declare(Fact(dependent_possible=('Netherlands', True)))
        self.declare(Fact(explanation="Netherlands: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Netherlands'))
    def netherlands_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Germany', 'France', 'Italy', 'Latvia']))
        self.declare(Fact(explanation="Netherlands: suggested alternative countries based on climate/culture group."))


# end of Netherlands
