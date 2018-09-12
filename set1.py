str=input("enter a string:")
count=0
vowel=set("aeiou")
for i in str:
  if i in vowel:
   count=count+1
  print("number of vowels:",count)
		
