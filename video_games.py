# -----------------------------------------+
# William Wood                             |
# Megan Ferhes                             |
# CSCI 127, Program 3                      |
# Last Updated: October 14, 2019           |
# -----------------------------------------+
import string
import time

def video_game_info(file):
    data = open(file, "r")
    line = data.readline()
    gametitles = []
    gamegenre = []
    gamescore = []
    gamerating = []
    string = ""
    for line in data:
        #splits each list in the file and appends it into the appropriate list
        titles = line.split(",")
        genre = line.split(",")
        score = line.split(",")
        rating = line.split(",")
        gametitles.append(titles[0])
        gamegenre.append(genre[5:-30])
        gamescore.append(score[-27])
        gamerating.append(rating[-23])
    for i in range(len(gametitles)):
        #prints out each video game title along with its corresponding information
        print(str(i+1) + "." + "Game: " + str(gametitles[i]) +
              " --- " + "Genre: " + str(gamegenre[i]) + " --- " +
              "Rating: " + str(gamerating[i]) + " --- " + "Score: "
              + str(gamescore[i]) + "\n")
        if i + 1 == 50:
            break 
    data.close()
#------------------------------------------------------------------------------

def list_genres(file):
    #prints a list of each unique genre in the list
    input_file = open(file, "r")
    input_file.readline()
    game_genres = []
    for line in input_file:
        values = line.split('","')
        if game_genres.count(values[5]) != 1:
            game_genres.append(values[5])
    sort_genres = []
    for items in game_genres:
        genre = items.split(",")
        for item in genre:
            sort_genres.append(item)
    print(sorted(set(sort_genres)))
    input_file.close()
#------------------------------------------------------------------------------

def how_many_games_published(file):
    data = open(file, "r")
    line = data.readline()
    publisher_names = []
    new_names = ""
    for line in data:
        publisher = line.split(",")
        publisher_names = [publisher.lower() for publisher in publisher_names]
        publisher_names.append(publisher[-29])
    #asks for user input to see how many games the chosen publisher has in the list
    pub_name = input("\nEnter a publisher name to see how many published games they have on the list!: ")
    pub_name = '"' + pub_name.lower() + '"'
    games = str(publisher_names.count(pub_name))
    if pub_name != '"ea"':
        print(pub_name.title() + " has published this many games from the list: " + games + " games")
    elif pub_name == '"ea"':
        print('"EA" has published this many games from the list: ' + games + " games")
    again = input("Would you like to try a different publisher? y or n: ")
    again.lower()
    while True:
        #asks for user input to see if they want to check a different publisher
        if again == "y":
            how_many_games_published(file)
            break
        elif again == "n":
            print("Bye!")
            break
        elif again != "y" or again != "n":
            print("\nPlease enter a valid key. y or n: ")
            again = input("Would you like to try a different publisher? y or n: ")
            again.lower()
#------------------------------------------------------------------------------


def main(file):
    print("Program 3: Video Game Analysis\n")
    time.sleep(1) #wait x seconds before executing the next action
    print("Displaying information on the first 50 games in list...\n")
    time.sleep(3)
    video_game_info(file)
    time.sleep(2)
    print("Displaying all game genres...\n")
    time.sleep(2)
    list_genres(file)
    time.sleep(1)
    how_many_games_published(file)

main("video_games.csv")
