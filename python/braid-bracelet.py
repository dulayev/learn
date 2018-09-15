print("Hello! Let's make a friendship-bracelet!")
rows_per_cm = float(input("Rows per cm: "))
width_of_the_bracelet = float(input("Width of the bracelet:"))

side_sweets_in_the_start = input("Side sweets in the start (Yes/No): ")
if side_sweets_in_the_start == "Yes":
    side_sweets_in_the_start_len = 0.3
else:
    side_sweets_in_the_start_len = 0.0
    
side_sweets_in_the_end = input("Side sweets in the end (Yes/No): ")
if side_sweets_in_the_end == "Yes":
    side_sweets_in_the_end_len = 0.3
else:
    side_sweets_in_the_end_len = 0
    
slanting_sweets_in_the_start = float(input("Slanting sweets in the start(count): "))
if slanting_sweets_in_the_start > 0:
    lenght_of_the_slanting_sweets_in_the_start = float(input("Lenght of the slanting sweets in the start: "))

slanting_sweets_in_the_end= float(input("Slanting sweets in the end(count): "))
if slanting_sweets_in_the_end > 0:
    lenght_of_the_slanting_sweets_in_the_end = float(input("Lenght of the slanting sweets in the end: "))


standart_sweets_in_the_start = float(input("Standart sweets in the start(count): "))
if width_of_the_bracelet %2 != 0:
    standart_sweets_in_the_start < 2
    if standart_sweets_in_the_start > 1:
     print("Impossible :(")
     standart_sweets_in_the_start = float(input("Standart sweets in the start(count): "))
if standart_sweets_in_the_start > 0:
    rows_in_the_sweets_in_the_start = input("Rows in the sweets in the start: ")
    if rows_in_the_sweets_in_the_start == "all":
        rows_in_the_sweets_in_the_start = width_of_the_bracelet/2/standart_sweets_in_the_start
    else:
        rows_in_the_sweets_in_the_start = float(rows_in_the_sweets_in_the_start)
else:
    rows_in_the_sweets_in_the_start = 0.0
          
standart_sweets_in_the_end = float(input("Standart sweets in the end(count): "))
if width_of_the_bracelet %2 != 0:
    standart_sweets_in_the_end < 2
    if  standart_sweets_in_the_end > 1:
        print("Impossible :(")
        standart_sweets_in_the_end = float(input("Standart sweets in the end(count): "))
if standart_sweets_in_the_end > 0:
    rows_in_the_sweets_in_the_end = input("Rows in the sweets in the end: ")
    if rows_in_the_sweets_in_the_end == "all":
        rows_in_the_sweets_in_the_end = width_of_the_bracelet/2/standart_sweets_in_the_end           
    else: 
        rows_in_the_sweets_in_the_end = float(rows_in_the_sweets_in_the_end)
else:
    rows_in_the_sweets_in_the_end = 0.0
                    
loops = input("Are there any loops in the bracelets? ")
if loops == "Yes":
    if width_of_the_bracelet %2 == 0:
        print("Possible!")
        length_of_the_loops = float(input("What is the lenght of the loops?: "))
    if width_of_the_bracelet %2 != 0:
        print("Impossible :(")
        length_of_the_loops = 0.0
else:
    length_of_the_loops = 0.0
clamps = input("Are there clamps on the bracelet?(Yes/No): ")
if  clamps == "Yes":
    clamps_len = 0.6
else:
    clamps_len = 0.0
    
quadratic_knots = float(input("How many quadratic knots are there on the bracelet? "))
leght_of_scheme = float(input("How many rows are there in tne scheme? " ))
leght_of_bracelet = float(input("Braclet's lenght: "))                    
empty_rows = (leght_of_bracelet - (leght_of_scheme/rows_per_cm + side_sweets_in_the_start_len + \
                                  side_sweets_in_the_end_len + \
                                  rows_in_the_sweets_in_the_end/rows_per_cm + \
                                  rows_in_the_sweets_in_the_start/rows_per_cm + \
                                  length_of_the_loops \
                                  +clamps_len + \
                                  +lenght_of_the_slanting_sweets_in_the_end \
                                  +lenght_of_the_slanting_sweets_in_the_start\
                                  +quadratic_knots * 0.2))*rows_per_cm
print("empty roads:{}".format (empty_rows))

        

    


                            
                            
                            
