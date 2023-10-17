from Hero import Hero # Hero is a subclass of character
from GameSettings import GameSettings
from battle_engine_function import battle_engine

game_settings = GameSettings()
name = input("Well met, stranger. Welcome to the Drunken Dragon! What be thine name? > ")
the_hero = Hero(name, xp = 0, level = 1,
                   gold = 5,attack_power= 8,
                   defense = 5, max_hp = 10, hp = 10, 
                   weapon= "fists", inventory = ['health_potion'])


game_on = True

while game_on:
    print(f"What can I do fer ye, {the_hero.name}?")
    for option in game_settings.main_options:
        print(f"{option['input_key']}. {option['text']} ")
    action = input("> ")
    if action == "1":
        battle_engine(the_hero)
    elif action == "4":
        print(f"May your journeys be safe, brave {the_hero.name}")
        game_on = False
    



