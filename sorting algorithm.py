unlist=[]
nos=int(input("Enter the numberof elements"))
for i in range(0,nos):
    temp=int(input("enter the element"))
    unlist.append(temp)
print("the unsorted list=",unlist)
def sorterasc():
    for i in range(0,len(unlist)):
        for j in range(i,len(unlist)):
                       if unlist[i]>=unlist[j]:
                           unlist[i],unlist[j]=unlist[j],unlist[i]
    print("the sorted list=",unlist)                      
def sorterdesc():
    for i in range(0,len(unlist)):
        for j in range(i,len(unlist)):
                       if unlist[i]<=unlist[j]:
                           unlist[i],unlist[j]=unlist[j],unlist[i]
    print("the sorted list",unlist)                     
mode=input("enter type as asc/desc")                      
if mode=='asc':
    sorterasc()
elif mode=='desc':
    sorterdesc()
    
