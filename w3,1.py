def malti(y):
    sum=1
    i=0
    while i<len(y):
        sum=sum*y[i]
        i=i+1
    print(sum)
malti([2,3,4,5,6,6,7,9])