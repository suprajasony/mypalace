height=int(input("enter the height of the triangle:"))
c=str(input("enter the character you want to print in the triangle:"))
for i in range(0,height):
	for j in range(0,height-i):
		print(c+" ",end='')
	print()