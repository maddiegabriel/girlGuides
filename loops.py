#!/usr/bin/python

for x in range(0, 5):
    print "This is loop # %d" % (x)

print "\n~~~~~~ A Pyramid of Smiles! ~~~~~~\n"
for i in range(10):
    print(':) ' * (i + 1))

print "\n\n~~~~~~ A Triangle of Stars! ~~~~~~\n"
for x in range(5):
    out = ''
    for y in range(5-x):
        out += ' '
    for y in range(x):
        out += '*'
    print(out)
for x in range(5):
    out = ''
    for y in range(x):
        out += ' '
    for y in range(5-x):
        out += '*'
    print(out)