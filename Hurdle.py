#Hurdle 1
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

jump()
jump()
jump()
jump()
jump()
jump()

#hurdle 2
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()

#Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def forward():
    if front_is_clear():
        move()
    else:
        jump()

while not at_goal():
    forward()
