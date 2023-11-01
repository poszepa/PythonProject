from enum import IntEnum
import Shape

Menu_Shape = IntEnum('Menu_Shape', ['Square', 'Rectangle', 'Circle', 'Triangle', 'Trapeze'])

def menu_options():
    print("""
    Choose shape, which you want to calculate area:
    1. square
    2. rectangle
    3. circle
    4. triangle
    5. trapeze 
    """)
def program_to_calculate_area():
    while(True):
        menu_options()
        userChoose = int(input("Your choose? :"))

        if(userChoose == Menu_Shape.Square):
            a = int(input("Input a: "))
            print("Square area is:", Shape.calculate_area_square(a))
        elif(userChoose == Menu_Shape.Rectangle):
            a = int(input("Input a: "))
            b = int(input("Input b: "))
            print("Rectangle area is:", Shape.calculate_area_rectangle(a, b))
        elif(userChoose == Menu_Shape.Circle):
            r = int(input("Input r: "))
            print("Circle area is:", Shape.calculate_area_circle(r))
        elif(userChoose == Menu_Shape.Triangle):
            a = int(input("Input a: "))
            h = int(input("Input h: "))
            print("Triangle area is:", Shape.calculate_area_triangle(a,h))
        elif(userChoose == Menu_Shape.Trapeze):
            a = int(input("Input a: "))
            b = int(input("Input b: "))
            h = int(input("Input h: "))
            print("Triangle area is:", Shape.calculate_area_trapeze(a,b,h))
        else:
            print("You inputed wrong number")
