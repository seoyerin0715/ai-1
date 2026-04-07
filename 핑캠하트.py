

width = 13
height = 10

for y in range(height):
    for x in range(width):

        top_curve = (y == 1 and ((1 < x < 5) or (7 < x < 11)))
        shoulders = (1 < y < 4 and (x == 1 or x == 11))
        middle_dip = (y == 2 and x == 6)
        v_shape = (y >= 4 and ((y - x == 3) or (y + x == 15)))
        if top_curve or shoulders or middle_dip or v_shape:
            print("#", end="") 
        else:
            print("  ", end="")
            

    print()

