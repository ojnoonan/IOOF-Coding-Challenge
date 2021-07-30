# IOOF Coding Challenge 2
# Created By: Oliver Noonan
# Date: 28th July 2021

# Classes: Main loop, Input Checker, Out of Bounds, Place, Move, Turn, Report

# Grid Layout
# 0,4 1,4 2,4 3,4 4,4
# 0,3 1,3 2,3 3,3 4,3
# 0,2 1,2 2,2 3,2 4,2
# 0,1 1,1 2,1 3,1 4,1
# 0,0 1,0 2,0 3,0 4,0

bearings = ['NORTH', 'EAST', 'SOUTH', 'WEST']
robot_placed = False
robot_coords = None
robot_facing = None


# main method for looping the program for user input
def main():
    print("IOOF Coding Challenge")
    print("By Oliver Noonan")
    while True:
        user_input = input("Enter a Command: ")
        if user_input:
            input_check(user_input.split())


# used by the main method to check the user input
# matches user input against item in dictionary
def input_check(command):
    command_dict = {
        'PLACE': place,
        'MOVE': move,
        'LEFT': turn,
        'RIGHT': turn,
        'REPORT': report
    }
    command[0] = command[0].upper()
    if command[0] in command_dict:
        # if the user input is not PLACE and
        # the robot is not placed display error
        if command[0] != 'PLACE' and robot_placed is False:
            print("must place robot")
        else:
            stored_function = command_dict[command[0]]
            # checks if there are args with command
            if len(command) > 1:
                stored_function(command[1])
            elif command[0] == 'LEFT' or command[0] == 'RIGHT':
                stored_function(command[0])
            else:
                stored_function()


# check if input coordinates are within the 5x5 grid
def out_of_range_check(coordinates):
    out_of_range = None
    for coord in coordinates:
        if coord > 4 or coord < 0:
            print("out of range")
            out_of_range = True
            break
        else:
            out_of_range = False
    return out_of_range


# place the robot
# split the user input into coordinates and facing direction
def place(options):
    global robot_placed, robot_coords, robot_facing
    options_list = options.split(",")
    if len(options_list) == 3:
        # check that the coordinates are numbers
        if options_list[0].isnumeric() and options_list[1].isnumeric():
            input_coords = [int(options_list[0]), int(options_list[1])]
            if not out_of_range_check(input_coords):
                if options_list[2].upper() in bearings:
                    robot_coords = input_coords
                    robot_facing = options_list[2].upper()
                    robot_placed = True


# move the robot one tile in facing direction
def move():
    global robot_coords
    temp_coords = list(robot_coords)
    if robot_facing == 'NORTH':
        temp_coords[0] += 1
    elif robot_facing == 'EAST':
        temp_coords[1] += 1
    elif robot_facing == 'SOUTH':
        temp_coords[0] -= 1
    elif robot_facing == 'WEST':
        temp_coords[1] -= 1
    if not out_of_range_check(temp_coords):
        robot_coords = temp_coords


# turn the robot
# passed the direction to turn the robot
def turn(direction):
    global robot_facing
    if direction == 'LEFT':
        # check if the robot is facing NORTH
        if robot_facing == bearings[0]:
            robot_facing = bearings[3]
        else:
            # set the robot direction based on the index of the bearing
            robot_facing = bearings[bearings.index(robot_facing) - 1]
    if direction == 'RIGHT':
        # check if the robot is facing WEST
        if robot_facing == bearings[3]:
            robot_facing = bearings[0]
        else:
            # set the robot direction based on the index of the bearing
            robot_facing = bearings[bearings.index(robot_facing) + 1]


# report the coordinates and the facing direction of the robot
def report():
    report_data = str(robot_coords) + " " + str(robot_facing)
    print(report_data)
    return report_data


if __name__ == "__main__":
    main()
