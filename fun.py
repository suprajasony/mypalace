list=[]
len=int(input('enter the length of the list\n'))
for a in range(0,len):
	b=input('enter the element\n')
	list.append(b)
print(list)
element=input('enter the elemnt whose index number ')
def indexreturn(list,element):
    for i in list:
       if i==element:
          return list.index(element)
print(indexreturn(list,element))          	
