from Character import Character


class Monster(Character):
    def __init__(self, name, xp_drop, gold_drop, attack_power, defense, max_hp, hp, weapon) -> None:
        self.xp_drop = xp_drop
        self.gold_drop = gold_drop
        # This is essentially calling the init method on whatever parent / super class we specified
        # We only pass the things the Character class init method needs / is not covered by this subclass
        super().__init__( name, attack_power, defense, max_hp, hp, weapon)
    
    def growl(self):
        print(f"The {self.name} growls in anger")