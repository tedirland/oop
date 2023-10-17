from Character import Character
from GameSettings import GameSettings
from battle_engine_function import battle_engine

game_settings = GameSettings()
character_name = input("Well met, stranger. Welcome to the Drunken Dragon! What be thine name? > ")
the_hero = Character(character_name, xp = 0, level = 1,
                   gold = 5,attack_power= 10,
                   defense = 5, max_hp = 10, hp = 10, weapon= "fists", inventory = ['health_potion'])
goblin = Character(character_name = "Chris Goblin", xp = 0, level = 1,
                   gold = 5, attack_power= 3,
                   defense = 3, max_hp = 7, hp = 7, weapon= "fists", inventory = ['rotten fish'])
ghoul = Character(character_name = "Little Green Ghoul, Buddy!", xp = 0, level = 1,
                   gold = 5, attack_power= 5,
                   defense = 2, max_hp = 7, hp = 7, weapon= "fists", inventory = ['rotten fish'])


enemies = [goblin, ghoul]

game_on = True

while game_on:
    print(f"What can I do fer ye, {the_hero.character_name}?")
    for option in game_settings.main_options:
        print(f"{option['input_key']}. {option['text']} ")
    action = input("> ")
    if action == "1":
        battle_engine(the_hero,enemies)
    elif action == "q":
        game_on = False
    



