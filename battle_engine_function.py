import random
from Monster import Monster # Monster is a sub class of character

def battle_engine(hero):
    
    goblin = Monster(name = "Cave Goblin", xp_drop = 20, gold_drop = 5,
                    attack_power= 6, defense = 3, 
                    max_hp = 7, 
                    hp = 7, 
                    weapon= "fists", 
                    )
    
    banshee = Monster(name = "Moor Banshee", xp_drop = 50, gold_drop = 10,
                    attack_power= 8, defense = 5, 
                    max_hp = 7, 
                    hp = 7, 
                    weapon= "fists", 
                    )
    
    enemies = [goblin, banshee]
    total_enemies = len(enemies)
    random_index = random.randint(0, total_enemies-1)
    enemy_encountered = enemies[random_index]

    print(f"A terrifying {enemy_encountered.name} appears!")
    in_fight = True
    while in_fight:
        print(f"You have {hero.hp} remaining, the {enemy_encountered.name} has {enemy_encountered.hp}")
        print(f"1. Strike with your {hero.weapon} ")
        health_potion_count = hero.inventory.count('health_potion')
        print(f"2. Drink a health potion (you have {health_potion_count} remaining)")
        print("3. Steel your defenses")
        print("4. Flee the battle")

        action = input("What action will you take? > ")

        if action == "1":
            damage_dealt = hero.attack_power - enemy_encountered.defense
            print(f"Your blows rain down on the {enemy_encountered.name}, dealing {damage_dealt} damage")
            enemy_encountered.hp -= damage_dealt
            if enemy_encountered.hp <1:
                print("Your foe crumples to the ground, slain by its better")
                print(f"You gain {enemy_encountered.xp_drop} experience points and {enemy_encountered.gold_drop} gold")
                hero.xp += enemy_encountered.xp_drop
                hero.gold += enemy_encountered.gold_drop
                in_fight = False
            else:
        
                enemy_damage = enemy_encountered.attack_power - hero.defense
                hero.hp -= enemy_damage
                print(f"The {enemy_encountered.name} retaliates, striking you for {enemy_damage} damage")

        elif action == "2":
            
            if health_potion_count > 0:

                print(f"You pull a health potion from your satchel and drink deeply. You restore {hero.max_hp - hero.hp} health points")
                hero.inventory.remove('health_potion')
                hero.hp = hero.max_hp
            else:
                print("You reach into your satchel and your fist closes around empty air. You are out of potions")
                print(f"Seizing the advantage, the {enemy_encountered.name} strikes for {enemy_encountered.attack_power} damage")
                hero.hp -= enemy_encountered.attack_power
        elif action == "4":
            print(f"You flee the fight, leaving the {enemy_encountered.name} howling at your back")
            in_fight = False
            


        


