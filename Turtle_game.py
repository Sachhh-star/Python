import turtle

scherm = turtle.Screen()
scherm.title("Route in Groningen")
scherm.setup(width=800, height=600) 

try:
    scherm.bgpic("marouf.png")
except:
    print("Let op: Plaatje 'marouf.png' niet gevonden.")

loper = turtle.Turtle()
loper.shape("turtle")
loper.color("blue")
loper.pensize(5)
loper.speed(2)


route_punten = [
    (-210, 200),  
    (-210, 50),   
    (-50, 50),    
    (-50, -90),   
    (150, -90)    
]

print("Route gestart...")

for index, punt in enumerate(route_punten):
    x = punt[0]
    y = punt[1]
    
    if index == 0:
        loper.penup()
        loper.goto(x, y)
        loper.pendown()
        loper.dot(20, "red")
        loper.write("Start (A)", font=("Arial", 12, "bold"))
    
    else:
        loper.setheading(loper.towards(x, y))
        loper.goto(x, y)
        
        if index == len(route_punten) - 1:
            loper.dot(20, "red")
            loper.write("Einde (B)", font=("Arial", 12, "bold"))

print("Bestemming bereikt!")

def print_coords(x, y):
    print(f"Nieuw punt voor je lijst: ({int(x)}, {int(y)}),")
    loper.penup()
    loper.goto(x, y)
    loper.dot(5, "green")
    loper.pendown()

scherm.onscreenclick(print_coords)

turtle.done()