rows=int(input("enter no.of rows:"))
cols=int(input("enter no.of columns:"))
a=[[1 for i in range(cols)]for j in range(rows)]
print(a)
for i in range(rows):
	for j in range(cols):

		a[i][j]=i+j
for s in a:
    print(s)
