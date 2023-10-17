from Character import Character


class Hero(Character):
    def __init__(self, name, xp, level, gold, attack_power, defense, max_hp, hp, weapon, inventory) -> None:
        self.xp = xp
        self.level = level
        self.gold = gold
        self.inventory = inventory
        # This is essentially calling the init method on whatever parent / super class we specified
        # We only pass the things the Character class init method needs / is not covered by this subclass
        super().__init__( name, attack_power, defense, max_hp, hp, weapon)
    
    def check_level_up(self):
        print("Check to see if hero has leveled up")