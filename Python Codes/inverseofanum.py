a=int(input())
i=0
j=1
while(a>0):
     d=int(a%10)
     a=int(a/10)
     i+=j*(10**d-1)
     j+=1
print(i)