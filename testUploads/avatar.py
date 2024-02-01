import turtle                   #basic setting
t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#e3f5fa")       #background color setting
t.speed(0)                      #speed of executing codes

t.hideturtle()                  #hideturtle
t.penup()
t.goto(50,-70)

def talloval(r):                # Verticle Oval
    t.left(45)
    for loop in range(2):       # Draws 2 halves of ellipse
        t.circle(r,90)          # Long curved part
        t.circle(r/2,90)
t.color("#695e4c")              # Face (line) color
t.fillcolor("#fcecc7")          # Face color (inside)
t.begin_fill()    
t.pendown()
talloval(120)                   
t.end_fill()
t.penup()
t.goto(6,80)                    # Start Hair
t.left(90)

def hair():                     # Definition of Hair
  t.pendown()
  t.color("#4d3616")
  t.circle(30,95)               # Curve 1
  t.left(10)
  t.forward(5)
  t.circle(150,50)              # Curve 2
  t.forward(30)             
  for repetition in range (3):  # Curve 3
    t.right(10)
    t.forward(4)
    t.right(5)
    t.forward(15)
  t.circle(20,20)               # Curve 4
  t.right(150)
  t.circle(70,20)               # Curve 5
  t.right(40)
  t.circle(50,25)               # Curve 6
  t.left(130)
  t.circle(50,30)               # Curve 7
  t.right(160)
  t.circle(80,20)               # Curve 8
  for repetition in range(5):   # Curve 9
    t.right(7)
    t.forward(5)
  for repetition in range(15):  # Curve 10
    t.right(2.5)
    t.forward(5)
  for repetition in range(3):   # Curve 11
    t.left(10)
    t.forward(10)
  t.right(10)
  t.circle(80,10)               # Curve 12
  t.circle(-75,30)              # Curve 13
  t.left(5)
  t.circle(-115,40)             # Curve 14
 # 63 & 67 
  for repetition in range(15):  # Curve 15
    t.right(5)
    t.forward(3.5)
  t.left(87)
  for repetition in range(15):  # Curve 16
    t.right(7)
    t.forward(7)
  t.circle(-170,25)             # Curve 17
  for repetition in range(7):   # Curve 18
    t.left(4)
    t.forward(3)
  for repetition in range(15):  # Curve 19
    t.right(5)
    t.forward(3)
  t.circle(15,60)               # Curve 20
  t.forward(15)
  for repetition in range(18):  # Curve 21
    t.right(2)
    t.forward(5)
  t.right(160)
  t.circle(100,30)              # Curve 22
  t.left(150)
  t.circle(-50,60)              # Curve 23
  t.right(120)
  for repetition in range(5):   # Curve 24
    t.left(5.5)
    t.forward(6)
  for repetition in range(10):  # Curve 25
    t.right(4)
    t.forward(6)
  for repetition in range(4):   # Curve 26
    t.right(6.5)
    t.forward(3)
  t.circle(50,30)               # Curve 27
  t.circle(130,35)              # Curve 28
  t.circle(80,15)               # Curve 29
  t.left(10)      
  for repetition in range(10):  # Curve 30
    t.left(6.5)
    t.forward(5)

def left_ear(x=-60,y=25):       # Definition of left ear(x=-60,y-25)
  t.goto(x,y)                   # Starting point
  t.pendown()
  t.fillcolor("#fcecc7")        # Ear color
  t.begin_fill()
  t.circle(23,150)              # Ear shape
  t.end_fill()
  t.penup()
  t.goto(x+5,y-40)              # Definition of ear ring
  t.pendown()
  t.fillcolor("#e6fafa")        # Ear ring color
  t.begin_fill()
  t.circle(3)                   # Ear ring (a circle)
  t.end_fill()

def right_ear(x=70,y=25):       # Definition of right ear(x=70,y=25)
  t.penup()
  t.goto(x,y)                   # Starting point
  t.pendown()
  t.fillcolor("#fcecc7")        # Fillcolor
  t.begin_fill()
  t.circle(-23,170)             # Ear shape
  t.end_fill()
  t.penup()
  t.goto(x+5,y-37)              # Ear ring (starting point)
  t.pendown()
  t.fillcolor("#e6fafa")        # Ear ring color
  t.begin_fill()
  t.circle(3)                   # Ear ring (circle)
  t.end_fill()
  t.penup()
  
def left_eye_brow(x=-10,y=40):
  t.pendown()
  t.right(150)                  
  t.forward(7)                  # Slope 1
  t.goto(x,y)
  t.left(145)
  t.forward(25)                 # Slope 2
  t.left(15)
  t.forward(8)                  # Slope 3
  t.right(150)                  
  t.forward(9)                  # Slope 4
  t.right(30)
  t.forward(10)                 # Slope 5
  t.right(23)
  t.forward(20)                 # Slope 6
  t.penup()
  
def right_eye_brow(x=20,y=40):
  t.pendown()
  t.left(150)
  t.forward(7)                  # Slope 1
  t.right(140)
  t.forward(20)                 # Slope 2
  t.right(15)
  t.forward(9)                  # Slope 3
  t.right(23)
  t.forward(10)                 # Slope 4
  t.right(150)
  t.forward(25)                 # Slope 5
  t.penup()

def left_eye(x=0,y=0):
  t.penup()
  t.goto(x-10,y+20)             # Position the turtle at the starting point
  t.pendown()
  t.color("#574339")
  t.fillcolor("white")          # Eye color
  t.begin_fill()
  t.right(30)
  t.circle(23, 80)              # Draw a semicircle
  t.left(90)
  t.circle(23, 80)              # Draw the other half of the semicircle
  t.end_fill()
  t.penup()
  t.goto(x-20,y+12)             # Starting point of drawing iris
  t.color("#574339")            # Iris color
  t.begin_fill()
  t.circle(7)                   # Iris size (drawing: circle)
  t.end_fill()
  t.goto(x-23,y+18)             # Starting point of drawing pupil
  t.color("black")              # Pupil color
  t.dot(5)                      # Pupil size
  t.penup()
  t.goto(x-27,y+20)             # Starting point of highlight
  t.pendown()
  t.color("white")              # Highlight color
  t.dot(3)
  t.penup()                   # Highlight size
    
def right_eye(x=0,y=0): # numbers
  t.penup()
  t.goto(x+25,y+15)           # Position the turtle at the starting point
  t.pendown()
  t.color("#574339")
  t.fillcolor("white")
  t.begin_fill()
  t.right(75)
  t.circle(23, 80)              # Draw a semicircle
  t.left(90)
  t.circle(23, 80)              # Draw the other half of the semicircle
  t.end_fill()
  t.penup()
  t.goto(x+35,y+24)             # Starting point of drawing iris
  t.color("#574339")            # Iris Color
  t.begin_fill()
  t.circle(7)                   # Iris size
  t.end_fill()
  t.goto(x+38,y+19)             # Starting point of pupil
  t.color("black")              # Pupil color
  t.dot(5)                      # Pupil size
  t.goto(x+40,y+20)             # Starting point of highlight
  t.color("white")              # Highlight color
  t.dot(3)                      # Highlight size
  t.penup()
  
def nose(x=0,y=0):
  t.goto(x-13,y-15)             # Starting point of nose
  t.pendown()
  t.color("#bfa486")            # Nose highlight
  t.circle(7,170)               # Nose highlight size
  t.left(100) 
  #t.fillcolor("#997648")       # Nose 
  t.begin_fill()
  for repetition in range(10):  # Curve 1
    t.forward(1)
    t.right(20)
  t.left(50)
  for repetition in range(2):   # Curve 2
    t.forward(2)
    t.right(1)
  t.right(90)
  t.forward(2)
  t.right(70)
  t.forward(4)
  t.end_fill()
  t.penup()
  t.right(180)
  t.forward(4)
  t.pendown()
  t.right(30)
  t.circle(6,95)                # Curve 3
  t.right(20)
  t.fillcolor("#997648")
  t.begin_fill()
  for repetition in range(3):   # Curve 4
    t.forward(2)
    t.right(1)
  t.right(70)
  t.forward(4)
  t.right(90)
  t.forward(3)
  t.right(60)
  t.forward(6)
  t.end_fill()
  t.penup()
  t.right(180)
  t.forward(8)
  t.pendown()
  t.circle(7,170)
  t.penup()
  t.goto(x+7,y-13)              # Final nose component
  t.color("#ffeddb")
  t.dot(17)

def mouth():                    # Definition of mouth       
  t.penup()
  t.goto(-17,-50)               # Starting point of mouth
  t.pendown()
  t.color("#b5625c")            # Mouth line colors
  t.fillcolor("#e08a84")        # Mouth color
  t.begin_fill()
  t.right(180)
  t.forward(3)
  t.left(40)
  t.forward(11)
  for repetition in range(3):   # Curve 1
    t.right(20)
    t.forward(2)
  t.forward(1)
  for repetition in range(3):   # Curve 2
    t.left(24)
    t.forward(2)
  t.forward(3)
  for repetition in range(3):   # Curve 3
    t.right(20)
    t.forward(2)
  t.forward(12)
  t.right(100)
  t.circle(-25,119)             # Curve 4
  t.end_fill()
  

def left_ear_curve():
  t.goto(-60,10)                # Curve 1
  t.pendown()
  t.color("#6e4f4d")            # Ear curve color
  t.left(120)
  t.circle(10,80)               # Ear curve color
  t.penup()
  
def right_ear_curve():
  t.goto(76,10)                 # Starting point of right ear curve
  t.pendown()
  t.color("#6e4f4d")            # Right ear curve color
  t.circle(-10,80)              # Curve 1
  t.penup()

def neck():
  t.penup()
  t.goto(-17,-82)  # Starting point of neck
  t.color("#fcecc7")
  t.pendown()
  t.fillcolor("#fcecc7")        # Neck color (same as face)
  t.begin_fill()  
  t.left(40)
  t.circle(-40,50)              # Curve 1
  t.left(90)
  t.circle(50,90)               # Curve 2
  t.left(90)
  t.circle(-40,48)              # Curve 3
  t.left(120)
  t.circle(-50,60)              # Curve 4
  t.end_fill()
  

t.fillcolor("#523a2c")          
t.begin_fill()
hair()                          # Execution of hair code
t.end_fill()
t.penup()
left_ear()                      # Execution of left ear code
t.penup()
right_ear()                     # Execution of right ear code
t.penup()
t.goto(-10,40)                  # Starting point of eye brows
t.fillcolor("#523a2c")          # Left eye brow color (brown)
t.begin_fill()
left_eye_brow()                 # Execution of left eye brow
t.end_fill()
t.penup()
t.goto(25,40)                   # Starting point of right eye brow
t.fillcolor("#523a2c")          # Color of right eye brow
t.begin_fill()
right_eye_brow()                # Execution of right eye brow
t.end_fill()
t.penup()
t.goto(-10,20)                  # Starting point of left eye
t.fillcolor("white")            # Color of left eye
t.begin_fill()
left_eye()                      # Execution of left eye
t.end_fill()
t.goto(20,20)                   # Starting point of right eye
t.fillcolor("white")            # Color of right eye
t.begin_fill()
right_eye()                     # Execution of right eye
t.end_fill()
t.penup()
nose()                          # Execution of nose
t.penup()
mouth()                         # Execution of mouth
t.penup()
left_ear_curve()                # Execution of left ear curve
right_ear_curve()               # Execution of right ear curve
t.penup()

t.goto(130,140)                 # Starting point of writing pieces
t.color("#091382")              # Writing color
for repetition in range(2):     # Rectangle frame
  t.forward(50)
  t.right(90)
  t.forward(30)
  t.right(90)
t.penup()
t.goto(120,130)                 # Starting point of writing sentences
t.pendown()                 
t.write("Jenny Liu")            # Execution of name: "Jenny Liu"
t.penup()
t.goto(110,120)                 # Starting point of writing sentences
t.pendown()
t.write("November 29th,1700")   # Execution of date: "November 7th, 2023"
t.penup()
neck()                          # Execution of neck

t.penup()
t.goto(70,70)                   # Starting point of spiral
t.pendown()

colors=["pink","purple","orange","brown"]   # four color choices
for x in range (30):
  for y in range (4):
    t.pencolor(colors[y])
    t.forward(x)                
    t.left(93)                    # turning angle
t.penup()