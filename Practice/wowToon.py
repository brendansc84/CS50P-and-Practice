class Character:
    def __init__(self, name, race, char_class, level):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level

    def introduce(self):
        return f"I am {self.name}, a level {self.level} {self.race} {self.char_class}!"
    
sylrien = Character("Sylrien", "Blood Elf", "Survival Hunter", 80)
rhazjin = Character("Rhazjin", "Zandalari", "Elemental Shaman", 80)

print(sylrien.introduce())