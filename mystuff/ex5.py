# -- coding: utf-8 --

my_name = 'André de Knegt'
my_age = 35
my_height = 1.74
my_weight = 83
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blond'

print "Let's talk about %s." % my_name
print "He's %f meters tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exacly right
print "If I add %d, %f, and %d I get %r." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
