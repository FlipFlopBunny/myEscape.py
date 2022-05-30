room_map = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]

# range is a function, that's why it's in purple
# range creates a sequence of 7 numbers starting at 0
# if you give it two numbers as parameters it will create a sequence that
# goes from the first number up to, but not including, the 2nd one
# for and in are commands that's why they are in orange
# y for the rows(lists), x for the columns(elements)
for y in range(7):
    for x in range(5):
        print("y=", y, "x=", x)
    print()
    
