#import another_module
#print(another_module.another_variable)

from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
