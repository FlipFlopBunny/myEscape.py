# this is a list of lists:
# we have a 5x5 map, so our list has 5 rows(lists) and 5 columns(items):
room_map = [[1, 0, 0, 0, 0], 
            [0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0],
            [0, 3, 0, 0, 0],
            [0, 0, 0, 0, 4]]
# the book is different
# but let's say left to right is x (lists), top to bottom is y (items)
# the append() function adds items to the end of a list changing its size
# the remove function removes items from a list changing its size

room_map[0][0] = 5
room_map[4][4] = 6

print(room_map)
