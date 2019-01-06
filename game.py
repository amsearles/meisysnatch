# A simple text-based game inspired by BanderSnatch
#Coded By Anthony M Searles
#Story & design by Meisy  Tunay

print("Welcome to MeisySnatch!!!! A game where you have to please Meisy else you will be snatched")
print("Shall we begin?")
print("You walk down a cold, empty hallway that is bare of any furnishings.")
print("As you come across a door, you are left with two options: Open the door or move on")
#start of game, User is given two choices with each choice branching off to a different path. If user doesnt enter correct input, the function loops again.
def startGame():
    firstChoice = input("What is your choice? Choose wisely for the consequences may be dire...")
    if firstChoice.casefold() == 'open the door'.casefold():
        advOne()
    elif firstChoice.casefold() == 'move on'.casefold():
        advTwo()
    else: startGame()
    
def choice():
  
#Adventure One starts, User opened door   
def advOne():
    print("As you open the door, you are greeted by.....")
    advOneFirstChoice = input("What")

#Adventure Two Starts, User moved on
def advTwo():
    print("testing 2")

def gameOver():
    print("...you feel a presence behind you...")
    print("A WILD MEISY APPEARS!!! SHE SNATCHES YOU!")
    quit()

startGame()
