range=int(raw_input("enter the number of elements of the series"))
n1=0
n2=1
i=2
if range<=0:
	print("positive integer")
elif range==1:
    print("fibonacci series up to",range,":")
    print(n1)
else:
    print("fibonacci series up to",range,":")
    print(n1)
    print(n2)
 while i<range:
      n3=n1+n2
    print(n3)
     n1=n2
     n2=n3
     i=i+1         	
