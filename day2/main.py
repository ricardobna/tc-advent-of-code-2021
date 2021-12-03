#gets path information from input file
input = open('input', 'r')
path = input.readlines()

horizontal_movement = 0
vertical_movement = 0

for movement in path:
    direction = movement.split(" ")[0]    
    if direction == "forward":
        horizontal_movement += int(movement.split(" ")[1])
    elif direction == "down":
        vertical_movement += int(movement.split(" ")[1])
    elif direction == "up":
        vertical_movement -= int(movement.split(" ")[1])
    print(horizontal_movement)
    print(vertical_movement)

print(horizontal_movement * vertical_movement)