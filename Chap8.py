class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    pass
class Mammals(Animals):
    pass
class Giraffes(Mammals):
    pass

def norm_func():
    print 'Normal function'
class ThisIsAClass:
    def class_func():
        print 'Class function'
    def also_class_func():
        print 'Also class fucntion'
class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass
class Mammals(Animals):
    def feed_young_with_milk(self):
        pass
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass
reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
harold = Giraffes()
harold.move()
class Animals(Animate):
    def breathe(self):
        print 'breathing'
    def move(self):
        print 'moving'
    def eat_food(self):
        print 'eating food'
class Mammals(Animals):
    def feed_young_with_milk(self):
        print 'feeding young'
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print 'eating leaves'
reginald = Giraffes()
reginald.move()
harold = Giraffes()
harold.eat_leaves_from_trees()
import turtle
avery = turtle.Pen()
kate = turtle.Pen()
avery.forward(100)
avery.right(90)
avery.forward(100)
kate.left(90)
kate.forward(100)
kate.right(90)
kate.forward(100)
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(100)
jacob.right(90)
jacob.forward(100)
john = turtle.Pen()
john.right(90)
john.forward(100)
john.right(90)
john.forward(100)
reginald.move()
reginald.breathe()
reginald.eat_food()
reginald.feed_young_with_milk()
reginald.move()
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print "I've found food!"
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
reginald = Giraffes()
reginald.dance_a_jig()
class Giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print ozwald.giraffe_spots
print gertrude.giraffe_spots
