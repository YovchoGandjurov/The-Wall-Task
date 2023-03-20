import logging

from constants import CUBIC_YARDS_PER_DAY, GOLD_DRAGON_COIN


logging.getLogger().setLevel(logging.DEBUG)



class Profile:
    def __init__(self, number, sections):
        self.number = number
        self.sections = sections if len(sections) <= 2000 else sections[:2000]
    
    def is_finished(self) -> bool:
        return all([section.is_constructed() for section in self.sections])

    def ice_specific_day(self, day: int) -> int:
        return sum([section.ice_specific_day(day) for section in self.sections])
    
    def cost_specific_day(self, day: int) -> int:
        return sum([section.cost_specific_day(day) for section in self.sections])
    
    def total_ice_amount(self) -> int:
        return sum([section.ice_amount() for section in self.sections])

    def total_cost(self) -> int:
        return sum([section.cost() for section in self.sections])

    def __repr__(self) -> str:
        return f"Profile {self.number} - {self.sections}"


class Section:
    def __init__(self, current_feet, profile_number, section_position):
        self.current_feet = int(current_feet)
        self.profile_number = profile_number
        self.section_position = section_position
        self.day = 0
        self.workdays = []
    
    def is_constructed(self):
        return False if self.current_feet < 30 else True
    
    def ice_specific_day(self, day: int) -> int:
        if day in self.workdays:
            return CUBIC_YARDS_PER_DAY
        return 0
    
    def cost_specific_day(self, day: int) -> int:
        return self.ice_specific_day(day) * GOLD_DRAGON_COIN
    
    def ice_amount(self) -> int:
        return len(self.workdays) * CUBIC_YARDS_PER_DAY

    def cost(self) -> int:
        return self.ice_amount() * GOLD_DRAGON_COIN

    def build(self) -> None:
        if not self.is_constructed():
            self.current_feet += 1
            self.day += 1
            self.workdays.append(self.day)

    def __repr__(self):
        return f"Section {self.section_position} feet - {self.current_feet}"
