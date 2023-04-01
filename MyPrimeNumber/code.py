def isPrimeNumber(num):
    i=2
    while (i < num):
        if (num % i == 0):
            return False
        i+=1
    if (num == i):
        return True

def primeNumberList (st,ed):
    lst = []
    for i in range (st,ed+1):
        if (isPrimeNumber(i)):
            lst.append(i)
    return lst

def start ():
    return "It is imam Hussain a.s institute library"


