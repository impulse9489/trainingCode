from character import *
from item import *
from librarian import *
from operations import *

stu = Character("Stu")
print stu.get_stats()
print stu.heal(10), stu.health
print "EVIL MOB TIME"

evilstu = Mob("Evil Stu")
# for attr, value in evilstu.__dict__.iteritems():
#    print attr,value
print evilstu.get_stats()

stu.health += 1000
print stu.health
