print list(range(0,5))
print list(range(0,1000))
def testfunc(myname):
    print 'hello %s' % myname
testfunc('Mary')
def testfunc(fname, lname):
    print 'hello %s %s' % (fname, lname)
testfunc('Mary', 'Smith')
firstname = 'Joe'
lastname = 'Robertson'
testfunc(firstname, lastname)
def savings(pocketmoney, paper_route, spending):
    return pocketmoney + paper_route - spending
print savings(10, 10 , 5)
def var_test():
    first_var = 10
    second_var = 20
    return first_var * second_var
print var_test()
another_var = 100
def var_test2():
    first_var = 10
    second_var = 20
    return first_var * second_var * another_var
print var_test2()
def spaceship_building(cans):
    total_cans = 0
    for week in range (1,53):
        total_cans = total_cans + cans
        print 'Week %s = %s cans' % (week, total_cans)
spaceship_building(2)
spaceship_building(13)
import time
print time.asctime()
import sys
print sys.stdin.readline()
def silly_age_joke(age):
    if age >= 10 and age <= 13:
        print 'What is 13 + 49 + 84 + 155 + 97?  A headache!'
    else:
        print 'Huh?'
silly_age_joke(9)
silly_age_joke(10)
def silly_age_joke():
    print 'How old are you?'
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print 'What is 13 + 49 + 84 + 155 + 97?  A headache!'
    else:
        print 'Huh?'
silly_age_joke()
