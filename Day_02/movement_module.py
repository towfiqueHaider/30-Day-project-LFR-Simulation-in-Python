#movement module
Movement_Commands = ["up", "right", "down", "left"]

def move_forward(Position, Direction):
    # Long method of updating tuples
    # Position_list = list(Position)
    # x = Position_list[0]
    # y = Position_list[1]
    x, y = Position
    if Direction == "up":
        y = y+1
    elif Direction == "right":
        x = x+1
    elif Direction == "down":
        y = y-1
    elif Direction == "left":
        x = x-1
    else:
        print("Invalid Command")
    return (x,y)

def move_backward(Position, Direction):
    #Short method of updating tuples by unpacking
    x, y = Position # Unpacking a tuple
    
    if Direction == "up":
        y = y-1
    elif Direction == "right":
        x = x-1
    elif Direction == "down":
        y = y+1
    elif Direction == "left":
        x = x+1
    else:
        print("Invalid Command")
    return (x,y)

# def turn_right(Direction):
    
#     if Direction == "up":
#         Direction = "right"
#     elif Direction == "right":
#         Direction = "down"
#     elif Direction == "down":
#         Direction = "left"
#     elif Direction == "left":
#         Direction = "up"
#     else:
#         print("Invalid Command")
#     return Direction

def turn_right(Direction):
    i = Movement_Commands.index(Direction)
    return Movement_Commands[(i+1)%4]

# def turn_left(Direction):
#     if Direction == "up":
#         Direction = "left"
#     elif Direction == "right":
#         Direction = "up"
#     elif Direction == "down":
#         Direction = "right"
#     elif Direction == "left":
#         Direction = "down"
#     else:
#         print("Invalid Command")
#     return Direction
def turn_left(Direction):
    i = Movement_Commands.index(Direction)
    return Movement_Commands[(i-1)%4]