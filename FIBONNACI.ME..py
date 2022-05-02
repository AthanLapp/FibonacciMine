#Fibonacci by 

a=0
b=1
i=0
c=0
for i in range(1,2000+1): #Change the second number(2000) to calculate to that set number
    c=b
    b+=a
    a=c
    print(i,b) #Prints the numbers position (ascending) and the calculated fibonacci's number. delete the tab (intentetion) to calculate only the last number of the sequence.
