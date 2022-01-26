def short(a):
    for i in range (len(a)):
        for j in range (i+1,len(a)):
            if(a[i]>a[j]):
                a[i],a[j]=a[j],a[i]
    print(a)
short([4,5,6,4,3,2,1,9,8])                