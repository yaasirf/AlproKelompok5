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
  turn_right()
  move()
  turn_left()

while(not at_goal()):
    jump()

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

#Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def forward():
    if front_is_clear():
        move()
    else:
        jump()

while not at_goal():
    forward()
