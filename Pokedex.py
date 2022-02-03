import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class Pokemon:
    def __init__(self, name, number, cp, type):
        self.name = name
        self.number = number
        self.cp = cp
        self.type = type


def print_menu():
    print("\n1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Print Pokemon with Type")
    print("5. Print Average Hit Points")
    print("6. Quit")
    print()

def print_pokedex(pokedex):
    for pokemon in pokedex:
        print("\nNumber: {}, Name: {}, CP: {}, Type: {} ".format(pokemon.number,pokemon.name.capitalize(),pokemon.cp,pokemon.type[0]), end = "")
        if len(pokemon.type) > 1:
            for i in range(1, len(pokemon.type)):
                print("and {} ".format(pokemon.type[i]), end = "")
    print()

def lookup_by_name(pokedex,name):
    name = name.casefold()
    pokemon_exists = False

    for pokemon in pokedex:
        if name == pokemon.name:
            pokemon_exists = True
            print("\nNumber: {}, Name: {}, CP: {}, Type: {} ".format(pokemon.number,pokemon.name.capitalize(),pokemon.cp,pokemon.type[0]),end="")
            if len(pokemon.type) > 1:
                for i in range(1, len(pokemon.type)):
                    print("and {} ".format(pokemon.type[i]), end = "")
    print()
    if not pokemon_exists: print("There is no Pokemon named ", name)
    

def lookup_by_number(pokedex,number):
    
    number_exists = False

    for pokemon in pokedex:
        if number == pokemon.number:
            number_exists = True
            print("\nNumber: {}, Name: {}, CP: {}, Type: {} ".format(pokemon.number,pokemon.name.capitalize(),pokemon.cp,pokemon.type[0]), end = "")
            if len(pokemon.type) > 1:
                for i in range(1, len(pokemon.type)):
                    print("and {} ".format(pokemon.type[i]), end = "")
    print()

    if not number_exists: print("There is no Pokemon number ", number)


def total_by_type(pokedex, type):
    total = 0

    for pokemon in pokedex:
        if type in pokemon.type:
            total +=1

    print("\nNumber of Pokemon that contain type {} = {}\n".format(type.capitalize(), total))
        

def average_hit_points(pokedex):
    
    total = 0

    for pokemon in pokedex:
        total += pokemon.cp

    print("\nAverage Pokemon combat points = {:.2f}".format(total/len(pokedex)))
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()