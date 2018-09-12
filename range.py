a=int(input("enter the numbers:"))
for i in range(1,a+1):
    if(i % 3 == 0 or i % 5 == 0):
       print("multiples of 3&5") 
    else:
       print("error")    	
