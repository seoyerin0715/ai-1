
for y in range(6, -7, -1):
    line = ""
    for x in range(-6, 7):
        is_bottom = (y <= 0 and abs(x) <= 6 + y)        
        is_top = (y > 0 and (abs(x) - 3)**2 + (y - 3)**2 <= 10)
        if is_bottom or is_top:
            line += "#"
        else:
            line += " "
            
    print(" ".join(line))
