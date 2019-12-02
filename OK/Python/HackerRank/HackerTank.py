#!/usr/bin/python3.7
#
#David Alonso Garduño Granados
#Python(3.7.4)
#01/12/19
#01/12/19
#Por fin HackerTank
il=1
ih=10
initialmaxhealth = 10

maxhealth = initialmaxhealth

mylevel = il
myhealth = ih

bugskilled = 0

def damage(buglevel):
    global myhealth
    global mylevel
    if buglevel>mylevel:
        damagedone = 2*buglevel
    elif buglevel == mylevel:
        damagedone = buglevel
    else:
        damagedone = 1
    myhealth = myhealth - damagedone
    return(myhealth,damagedone)
    
def levelup(bugskilled):
    global myhealth
    global mylevel
    global maxhealth
    global initialmaxhealth
    mylevel = mylevel + 1
    maxhealth = initialmaxhealth + (mylevel-1)*5
    myhealth = maxhealth
    return(myhealth,mylevel,maxhealth)
        
def encounter(buglevel):
    global bugskilled
    damage(buglevel)
    global myhealth
    if myhealth > 0:
        bugskilled = bugskilled + 1
    if bugskilled%3==0:
        levelup(bugskilled)


bugwave = int(input())
bugs = input()
bugs = bugs.split()
bugs = list(map(int, bugs)) 

for m in bugs:
    if myhealth > 0:
        encounter(m)
    else:
        one=1

if myhealth > 0:
    print ("You have won! Reached level %g and killed %g bugs" % (mylevel,bugskilled))
else:
    print("You have died. Reached level %g and killed %g bugs" % (mylevel,bugskilled)) 
