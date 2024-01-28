#   a123_apple_1.py
#updated the textures of the apple pear and background
import turtle as trtl
import random
import time
#list for what button to click later
thewholealphabet = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r","s", "t", "v", "w", "x", "z"]

thewholealphabetpears = ["a", "e", "i", "o", "u", "y"]
#-----setup-----
rand1ap = random.choice(thewholealphabet)
xposwosloz = random.randint(-250, 250)


ready = False



wonumber = 0
scorelore = wonumber
donez = "y"
#these are all my different apple images that generate, go to their positions and write the letter needed to be presse
apple_image = "apple.gif" # Store the file name of your shape
apple = trtl.Turtle()
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

#update that makes you click the screen to start rather than typing in console
def easy(x,y):
  global ready, wonumber
  ready = True
  wonumber = 5
def medium(x,y):
  global ready, wonumber
  ready = True
  wonumber = 10
def hard(x,y):
  global ready, wonumber
  wonumber = 15
  ready = True
lettrl = trtl.Turtle()
easyt = trtl.Turtle()
lettrl.hideturtle()
easyt.penup()
easyt.color("green")
mediumt = trtl.Turtle()
mediumt.penup()
mediumt.color("orange")
hardt = trtl.Turtle()
hardt.penup()
hardt.color("red")
mediumt.forward(20)
hardt.forward(60)
lettrl.penup()
lettrl.setposition(-290,0)
lettrl.color("white")
lettrl.write("Click the green turtle for easy orange for medium and red for hard", font=("Arial", 10, "bold"))
apple.color("red")
apple.hideturtle()
while ready == False:
  easyt.onclick(easy)
  mediumt.onclick(medium)
  hardt.onclick(hard)
  wn.listen()
easyt.hideturtle()
mediumt.hideturtle()
hardt.hideturtle()


apple.color("black")
lettrl.clear()
apple.showturtle()
apple.penup()

apple.speed(1)
faltre = False
wondernbonder = "yes"

#-----functions-----
def lettlewhwelfoal():
  global faltre, wondernbonder
  wondernbonder = "no"
  if faltre == False:
    apple.hideturtle()
    apple.color("blue")
    apple.write(rand1ap, font=("Arial", 50, "bold"))
    wondernbonder = "donezezo"
    
def blnk():
  gordinofornino = 0
def appole_fall_lol(keylatterpressnow):
  global faltre, lettlewhwelfoal, wondernbonder, scorelore
  print(3)
  apple.right(90)
  wn.onkeypress(lettlewhwelfoal, keylatterpressnow)
  wn.listen()
  apple.backward(200)
  wn.onkeypress(blnk, keylatterpressnow)
  while wondernbonder == "yes":
    faltre = True
    if faltre == True:
      apple.hideturtle()
      apple.color("red")
      apple.write(keylatterpressnow, font=("Arial", 50, "bold"))
      scorelore = scorelore - 1
      wondernbonder = 'no'
  print("it passed this")
lettrl = trtl.Turtle()
lettrl.hideturtle()
lettrl.penup()
lettrl.setpos(0,200)
lettrl.color("black")
lettrl.write(rand1ap, font=("Arial", 50, "bold"))

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def eazay(x,y):
  global wonumber
  wonumber = 5
  print(wonumber)
def medum():
  global wonumber
  wonumber = 10

def lard():
  global wonumber
  wonumber = 15

def contin():
  global donez
  donez = "y"
def stopgop():
  global donez
  donez = "n"
#-----function calls-----
#draws the apples textures and makes sure to make the apple fall when the certain key is pressed
while donez == "y":
  lettrl.clear()
  lettrl.setpos(-250,10)
  lettrl.color("black")
  scorelore = wonumber
  for i in range(wonumber):
    lettrl.clear()
    choiceloice = random.randint(0,1)
    if choiceloice == 1:
      rand1ap = random.choice(thewholealphabet)
      apple_image = "pear.gif"
    if choiceloice == 0:
      rand1ap = random.choice(thewholealphabetpears)
      apple_image = "apple.gif"
    
    xposwosloz = random.randint(-250, 250)
    wn.addshape(apple_image)
    apple = trtl.Turtle()
    apple.speed(1)
    apple.penup()
    apple.setpos(xposwosloz,-200)
    faltre = False
    wondernbonder = "yes"
    lettrl = trtl.Turtle()
    lettrl.hideturtle()
    lettrl.penup()
    lettrl.setpos(0,200)
    lettrl.color("black")
    lettrl.write(rand1ap, font=("Arial", 50, "bold"))
    draw_apple(apple)
    appole_fall_lol(rand1ap)
    lettrl.clear()
    wn.listen()
  print("Your final score for the ammount of apples you catched is", scorelore)
  donez = "vlem"
  lettrl.setpos(-250,10)
  lettrl.color("black")
  lettrl.write("Do you want to keep playing (y/n): ", font=("Arial", 15, "bold"))
  while donez == "vlem":
    wn.onkeypress(eazay, "n")
    wn.listen()
    wn.onkeypress(medum, "y")
    wn.listen()



wn.mainloop()