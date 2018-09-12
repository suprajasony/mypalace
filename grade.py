sub1=int(input("enter marks of the first subject: "))
sub2=int(input("enter marks of the second subject: "))
sub3=int(input("enter marks of the third subject: "))
avg=(sub1+sub2+sub3)/3
if(avg>=90):
	print("grade: A")
elif(avg>=90&avg<=80):
    print("grade: B")
elif(avg>=80&avg<=70):
    print("grade: C") 
else:
    print("grade: F")      
