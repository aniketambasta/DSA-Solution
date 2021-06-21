import os
def staircase(n,s):
    result=0
    i=1
    if (n==1 or n==0):
        return 1
    
    while i<=n and i<=s:
        result=result+staircase(n-i,s)
        i=i+1
    return result
   
while (True):
    print("-"*30) 
    os.system("cls")
    n=int(input("Enter the total number of stairs: "))
    s=int(input("Enter the max steps you can climb at once: "))
    print("-"*30)
    if (s>n):
        print("-"*30)
        print("WARNING\n")
        print("Sorry you have entered max. step more than total number of stairs please enter the details again correctly")
        os.system("TIMEOUT 5")
        continue
    output=staircase(n,s)
    print("Total number of possible sequence in which you can climb the stairs are-: " ,output)
    print("-"*30)
    choice = input("press 'q' to quit or enter to continue: ")
    if (choice=='q'):
        break
        
    