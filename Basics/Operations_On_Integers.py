
###Doing basic maths functions

a,b = 5,3

def Sum():
    print "Sum of {} and {} is {}".format(a,b,a+b)

def Diff():
    c = a-b
    print "Diff between {} and {} is {}".format(a,b,c)

def Mult():
    c=a*b
    print "Multiplication of {} and {} is {}".format(a,b,a*c)

def Divison(a,b):
    c = a/b
    print "Division between {} amd {} is {}".format(a,b,c)

    
Sum()
print "***************"
Diff()
print "***************"
Mult()
print "***************"
Divison(6,3)


###Output is
"""
Sum of 5 and 3 is 8
***************
Diff between 5 and 3 is 2
***************
Multiplication of 5 and 3 is 75
***************
Division between 6 amd 3 is 2
"""
