# Auto-generated country rules
from experta import Rule, Fact, P
from rules.base_rules import Person

class SaudiArabiaRules:
    """Rules for Saudi Arabia"""
    @Rule(Person(preferred_country='Saudi Arabia', education='PhD', experience_years=P(lambda e: e is not None and e >= 3)), salience=80)
    def saudi_arabia_strong(self):
        self.declare(Fact(eligibility=('Saudi Arabia', 'TopPath', 0.95)))
        self.declare(Fact(points=('Saudi Arabia', 80)))
        self.declare(Fact(explanation="Saudi Arabia: PhD-level top path (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', education='Masters', experience_years=P(lambda e: e is not None and e >= 2)), salience=70)
    def saudi_arabia_medium(self):
        self.declare(Fact(eligibility=('Saudi Arabia', 'MidPath', 0.85)))
        self.declare(Fact(points=('Saudi Arabia', 65)))
        self.declare(Fact(explanation="Saudi Arabia: Masters-level / mid path (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', role='student'), salience=60)
    def saudi_arabia_student(self):
        self.declare(Fact(eligibility=('Saudi Arabia', 'StudentToWorkPath', 0.6)))
        self.declare(Fact(points=('Saudi Arabia', 35)))
        self.declare(Fact(explanation="Saudi Arabia: student->work/graduate path often exists (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', occupation=P(lambda o: o and ('IT' in o or 'I' in o))), salience=65)
    def saudi_arabia_it(self):
        self.declare(Fact(add_points=('Saudi Arabia','IT', 10)))
        self.declare(Fact(explanation="Saudi Arabia: occupation IT receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', occupation=P(lambda o: o and ('Engineering' in o or 'Engineerin' in o))), salience=65)
    def saudi_arabia_engineering(self):
        self.declare(Fact(add_points=('Saudi Arabia','Engineering', 10)))
        self.declare(Fact(explanation="Saudi Arabia: occupation Engineering receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', occupation=P(lambda o: o and ('Healthcare' in o or 'Healthcar' in o))), salience=65)
    def saudi_arabia_healthcare(self):
        self.declare(Fact(add_points=('Saudi Arabia','Healthcare', 12)))
        self.declare(Fact(explanation="Saudi Arabia: occupation Healthcare receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', occupation=P(lambda o: o and ('Business' in o or 'Busines' in o))), salience=65)
    def saudi_arabia_business(self):
        self.declare(Fact(add_points=('Saudi Arabia','Business', 8)))
        self.declare(Fact(explanation="Saudi Arabia: occupation Business receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', occupation=P(lambda o: o and ('Hospitality' in o or 'Hospitalit' in o))), salience=65)
    def saudi_arabia_hospitality(self):
        self.declare(Fact(add_points=('Saudi Arabia','Hospitality', 12)))
        self.declare(Fact(explanation="Saudi Arabia: occupation Hospitality receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', occupation=P(lambda o: o and ('Research' in o or 'Researc' in o))), salience=65)
    def saudi_arabia_research(self):
        self.declare(Fact(add_points=('Saudi Arabia','Research', 7)))
        self.declare(Fact(explanation="Saudi Arabia: occupation Research receives bonus points (illustrative)."))

    @Rule(Person(preferred_country='Saudi Arabia', has_spouse=True, spouse_education=P(lambda se: se in ['Bachelors','Masters','PhD'])))
    def saudi_arabia_spouse_edu(self):
        self.declare(Fact(add_points=('Saudi Arabia','SpouseEducation', 15)))
        self.declare(Fact(explanation="Saudi Arabia: spouse education adds adaptability points."))

    @Rule(Person(preferred_country='Saudi Arabia', has_spouse=True, spouse_is_working=True))
    def saudi_arabia_spouse_work(self):
        self.declare(Fact(add_points=('Saudi Arabia','SpouseWorking', 10)))
        self.declare(Fact(explanation="Saudi Arabia: spouse employment adds adaptability points."))

    @Rule(Person(preferred_country='Saudi Arabia', salary_local=P(lambda s: s is not None and s >= 60000)), salience=30)
    def saudi_arabia_financial_ok(self):
        self.declare(Fact(financial_ok=True))
        self.declare(Fact(explanation="Saudi Arabia: reported salary meets conservative threshold (60000 SAR)."))

    @Rule(Person(preferred_country='Saudi Arabia', num_children=P(lambda n: n is not None and n > 0)))
    def saudi_arabia_dependent(self):
        self.declare(Fact(dependent_possible=('Saudi Arabia', True)))
        self.declare(Fact(explanation="Saudi Arabia: dependent child detected — family visa streams may apply."))

    @Rule(Person(preferred_country='Saudi Arabia'))
    def saudi_arabia_alternatives(self):
        self.declare(Fact(alternative_suggestions=['United Arab Emirates']))
        self.declare(Fact(explanation="Saudi Arabia: suggested alternative countries based on climate/culture group."))


# end of Saudi Arabia
