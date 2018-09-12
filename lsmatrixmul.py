a=[[1,2,3],[3,4,5],[5,6,7]]
b=[[2,3,4],[3,6,7],[7,7,2]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
	for j in range(len(a[0])):
		for k in range(len(b)):
			result[i][j]+=a[i][k]*b[k][j]
for r in result:
  print(r)