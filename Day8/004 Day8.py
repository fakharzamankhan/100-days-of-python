import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5




def paint_calculator(height,width, cover):
    number_of_cans=math.ceil((height*width)/cover)
    print(f"No of cans required:{number_of_cans} ")

paint_calculator(height=test_h, width=test_w, cover=coverage)

