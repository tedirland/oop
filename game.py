from Character import Character
from GameSettings import GameSettings

character_name = input("Well met, stranger. Welcome to the Drunken Dragon! What be thine name? > ")

the_hero=Character(character_name)
game_on = True

while game_on:
    print(f"What can I do fer ye, {the_hero.character_name}?")

    for option in GameSettings.main_options:
        print(f"{option['input_key']}. {option['text']} ")
        game_on = False

