# Name: Nana Kwasi Owusu
# Program Description: Maze game to learn how linked lists work 
from room import Room
from maze import Maze

def play(my_maze):
    #Play a game
    while not my_maze.atExit():
        
        print(my_maze.getCurrent())
        direction = input("Enter direction to move: north, west, east, south or restart:\n").strip().lower()
        if direction == "north":
            my_maze.moveNorth()
        elif direction == "south":
            my_maze.moveSouth()
        elif direction == "east":
            my_maze.moveEast()
        elif direction == "west":
            my_maze.moveWest()
        elif direction == "restart":
            my_maze.reset()
            print("You went back to the start!")
        else:
            print("Direction invalid, try again.")
    print("You found the exit!")

#Empty Maze
EMPTY_MAZE = Maze()

# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
room1 = Room("This room is the entrance")
room2 = Room("This room has toys. Maybe the toy room?")
room3 = Room("This room is the exit. Good job!")

room1.setEast(room2)
room2.setNorth(room3)
SIMPLE_MAZE = Maze(room1,room3)


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
room1 = Room("This room is the entrance")
room2 = Room("This room is haunted. Maybe the basement?")
room3 = Room("This room is room smells good. Maybe the kitchen?")
room4 = Room('This room has a bathtub. Maybe the bathroom?')
room5 = Room('This room has a car. Maybe the garage?')
room6 = Room('This room is the exit. Good job!')

room1.setWest(room2)
room2.setWest(room3)
room3.setWest(room4)
room4.setNorth(room5)
room5.setEast(room6)
INTERMEDIATE_MAZE = Maze(room1,room6)


if __name__=="__main__":
    play(SIMPLE_MAZE)
    play(INTERMEDIATE_MAZE)