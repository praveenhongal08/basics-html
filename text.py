num=int(input("enter the number:"))
num=int(num)
for each in range(1,num+1):
    c=0
    i=1
    while(i<=each):
         if(each%i==0):
          c=c+1
          i=i+1
         if(c==2):
             print(each)
