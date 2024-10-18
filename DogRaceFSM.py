import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Dog race")
wn.bgcolor("lightblue")
wn.register_shape("Asset/dog_running.gif")

# Create the turtle
pen = turtle.Turtle()
pen.speed(2)

# Create the dog
dog = turtle.Turtle()
dog.shape("Asset/dog_running.gif")
dog.penup()

# Start state
dog.goto(-400, 50)

# State text
state_text = turtle.Turtle()
state_text.hideturtle()
state_text.penup()
state_text.goto(0, 200)

# Function to draw the start line
def draw_start():
    pen.penup()
    pen.goto(-400, 0)
    pen.pendown()
    pen.pensize(5)
    pen.color("black")
    pen.forward(800)
    pen.penup()
    pen.goto(-400, 100)
    pen.pendown()
    pen.write("START", font=("Arial", 16, "bold"))

# Function to draw the finish line with flag
def draw_finish():   
    # Draw flagpole
    pen.penup()
    pen.goto(400, 0)
    pen.pendown()
    pen.left(90)
    pen.pensize(3)
    pen.forward(60)
    
    # Draw flag
    pen.pensize(1)
    pen.color("red")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(30)
        pen.right(90)
        pen.forward(20)
        pen.right(90)
    pen.end_fill()
    
    # Finish text
    pen.penup()
    pen.goto(325, 100)
    pen.pendown()
    pen.color("black")
    pen.write("FINISH", font=("Arial", 16, "bold"))
    pen.penup()

# State map
state_map = {
    "start" : "Dog at start",
    "moving" : "Dog running...",
    "stopped" : "Dog stopped",
    "finish" : "Dog finished the race!"
}

# State Status
def update_headline():
    state_text.clear()
    state_text.write(state_map[state], align="center", font=("Arial", 18, "bold"))

# Start to moving state
def start_moving():
    global state 
    state = "moving"
    update_headline()
    dog_move()

# Stop state
def stop_moving():
    global state 
    if state == "finish":
        return
    state = "stopped"
    update_headline()

# Reset state
def reset_dog():
    global state
    state = "start"
    dog.goto(-400, 50)
    update_headline()

# Moving State
def dog_move():
    global state 
    if dog.pos()[0] >= 400:  # Finish State
        state = "finish"
        update_headline()
    if state == "moving":
        dog.forward(1)
    if state != "finish":
        wn.ontimer(dog_move, 10) 

# Draw the start and finish lines
draw_start()
draw_finish()
pen.hideturtle()

# Event listeners
wn.listen()
wn.onkey(start_moving, "space") 
wn.onkey(stop_moving, "s")      
wn.onkey(reset_dog, "e")        

state = "start"
update_headline()

wn.mainloop()
