import os

def get(arg):
    if arg is not None:
        if(os.path.isfile(arg)):
            return arg
    print("No file provided, searching for saves...")
    save_dir = os.path.join(os.path.expanduser('~user'), 'Saved Games\Mojang Studios\Dungeons')
    
    save_list = os.listdir(save_dir)
    if(len(save_list) == 0):
        print("No saves detected")
        exit()
    elif(len(save_list) == 1):
        print("Found save", save_list[0])
        selected = save_list[0]
    else:
        print("Found", len(save_list), "saves:")
        for save in save_list:
            print(save_list.index(save) + 1, "-" ,save)
        selected = save_list[int(input("Enter save to use > ")) - 1]

    save_dir = os.path.join(save_dir, selected, "Characters")
    characters = []
    for character in os.listdir(save_dir):
        if character.endswith('.json'):
            characters.append(character)
    
    if(len(characters) == 0):
        print("No characters detected. Have you decrypted your save file?")
        exit()
    elif(len(characters) == 1):
        print("Found character", characters[0])
        return os.path.join(save_dir, characters[0])
    else:
        print("Found", len(characters), "characters:")
        for character in characters:
            print(characters.index(character) + 1, "-", character)
        return os.path.join(save_dir, characters[int(input("Enter character to use > ")) - 1])
