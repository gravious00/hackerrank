#https://www.hackerrank.com/contests/projecteuler/challenges/euler023

# Enter your code here. Read input from STDIN. Print output to STDOUT
def pop(a):
    s=0
    for i in range(1,a):
        if a%i==0:
            s=s+i
    if s>a:
        return 1
    else:
        return 0

x=input("")#mention
for j in range(x):
    t=0
    x=input("")
    for k in range(1,(x/2)+1):
        q=x-k
        if pop(k)+pop(q)==2:
            t=1
    if t==1:
        print "YES"
    else:
        print "NO"
