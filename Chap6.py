print "hello"
print "hello"
print "hello"
print "hello"
print "hello"


for x in range(0,5):
    print "hello"
for x in range(0,5):
    print "hello %s" % x

x = 0
print "hello %s" % x
x = 1
print "hello %s" % x
x = 2
print "hello %s" % x
x = 3
print "hello %s" % x
x = 4
print "hello %s" % x

wizard_list = ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
for i in wizard_list:
    print i
print wizard_list[0]
print wizard_list[1]
print wizard_list[2]
print wizard_list[3]
print wizard_list[4]
print wizard_list[5]

hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print i
    print i

hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print i
    for j in hugehairypants:
        print j

print 20 + 10 * 365 - 3 * 52
found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1,53):
    coins = coins + magic_coins - stolen_coins
    print 'Week %s = %s' % (week, coins)
for step in range(0,20):
    print step
step = 0
tired = True
badweather = True
while step < 10000:
    print step
    if tired == True:
        break
    elif badweather == True:
        break
    else:
        step = step + 1
x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print x, y
