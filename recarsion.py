def binary_search(a,size,key):
    i=0
    j=size-1
    flag=0
    while i<=j and flag==0:
        mid=(i+j)//2
        if a[mid]==key:
            pos=mid+1
            flag=1
        if a[mid]<key:
            i=mid+1
        if a[mid]>key:
            j=mid-1
    if flag==1:
        print("Element found at",pos,"position")
    else:
        print("Element not found")
size=int(input("enter size of the list:-"))                          
a=[]
for i in range(size):
    val=int(input("enter the number:-"))
    a.append(val)
key=int(input("enter number to search:-"))
binary_search(a,size,key)              