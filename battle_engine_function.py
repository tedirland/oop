import random

def battle_engine(hero, enemies):

    total_enemies = len(enemies)
    random_index = random.randint(0, total_enemies-1)

    enemy_encountered = enemies[random_index].copy()

    print(f"A terrifying {enemy_encountered.character_name} appears!")
    in_fight = True
    while in_fight:
        enemy_attack_modifier = 1
        print(f"You have {hero.hp} remaining, the {enemy_encountered.character_name} has {enemy_encountered.hp}")
        print(f"1. Strike with your {hero.weapon} ")
        health_potion_count = hero.inventory.count('health_potion')
        print(f"2. Drink a health potion (you have {health_potion_count} remaining)")
        print("3. Steel your defenses")
        print("4. Flee the battle")

        action = input("What action will you take? > ")
        


