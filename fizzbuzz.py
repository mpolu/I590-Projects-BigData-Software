import sys

def fizz_buzz(n):
    for i in range(1,n+1):
        if (i % 2 == 0) and (i % 3 == 0):
           print "fizzbuzz"
        elif (i % 2 == 0):
           print "fizz"
        elif (i % 3 == 0):
           print "buzz"
        else :
           print i
if __name__== '__main__':
    n= int(sys.argv[1])
    fizz_buzz(n)



