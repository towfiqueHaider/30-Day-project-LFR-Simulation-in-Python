import movement_module as mm

Position = (0,0) #Packing a tuple
Direction = "up"

Position = mm.move_forward(Position, Direction)
Direction = mm.turn_right(Direction)
Position = mm.move_backward(Position, Direction)
Direction = mm.turn_left(Direction)
Position = mm.move_backward(Position, Direction)
Direction = mm.turn_left(Direction)

print("Position: ", Position)
print("Direction: ", Direction)



    



    
    
