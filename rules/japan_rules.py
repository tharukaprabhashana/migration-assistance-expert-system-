# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class JapanRules:
    """Rules for Japan"""
    @Rule(Person(preferred_country='Japan', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def japan_strong(self):
        self.declare(Fact(eligibility=('Japan', 'TopPath', 0.95)))
        self.declare(Fact(points=('Japan', 80)))
        self.declare(Fact(explanation="Japan: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Japan', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def japan_medium(self):
        self.declare(Fact(eligibility=('Japan', 'MidPath', 0.85)))
        self.declare(Fact(points=('Japan', 65)))
        self.declare(Fact(explanation="Japan: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Japan', role='student'), salience=60)
    def japan_student(self):
        self.declare(Fact(eligibility=('Japan', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Japan', 35)))
        self.declare(Fact(explanation="Japan: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Japan', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def japan_it(self):
        self.declare(Fact(add_points=('Japan','IT', 10)))
        self.declare(Fact(explanation="Japan: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Japan', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def japan_engineering(self):
        self.declare(Fact(add_points=('Japan','Engineering', 10)))
        self.declare(Fact(explanation="Japan: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Japan', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def japan_healthcare(self):
        self.declare(Fact(add_points=('Japan','Healthcare', 8)))
        self.declare(Fact(explanation="Japan: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Japan', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def japan_business(self):
        self.declare(Fact(add_points=('Japan','Business', 7)))
        self.declare(Fact(explanation="Japan: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Japan', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def japan_hospitality(self):
        self.declare(Fact(add_points=('Japan','Hospitality', 6)))
        self.declare(Fact(explanation="Japan: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Japan', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def japan_research(self):
        self.declare(Fact(add_points=('Japan','Research', 10)))
        self.declare(Fact(explanation="Japan: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Japan', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def japan_spouse_edu(self):
        self.declare(Fact(add_points=('Japan','SpouseEducation', 15)))
        self.declare(Fact(explanation="Japan: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Japan', has_spouse=True, spouse_is_working=True))
    def japan_spouse_work(self):
        self.declare(Fact(add_points=('Japan','SpouseWorking', 10)))
        self.declare(Fact(explanation="Japan: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Japan', salary_local=P(lambda s: s is not None and s >= 3000000)), salience=30)
    def japan_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Japan: reported salary meets conservative threshold (3000000 JPY)."))

    @Rule(Person(preferred_country='Japan', num_children=P(lambda n: n is not None and n > 0)))
    def japan_dependent(self):
        self.declare(Fact(dependent_possible=('Japan', True)))
        self.declare(Fact(explanation="Japan: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Japan'))
    def japan_alternatives(self):
        self.declare(Fact(alternative_suggestions=['Singapore']))
        self.declare(Fact(explanation="Japan: suggested alternative countries based on climate/culture group."))


# end of Japan
