# def calculator(a,b):
#     add=a+b
#     print("add",add)
#     sub=a-b
#     print("sub",sub)
#     multiply=a*b
#     print("multiply",multiply)
#     divide=a/b
#     print("divide",a/b)
#     modules=a%b
#     print("modules",modules)
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# calculator(a,b)



def calculator(a,b,sembol):
    if sembol=="+":
       print(a+b)
    if sembol=="-":
        print(a-b)
    if sembol=="*":
        print(a*b)
    if sembol=="/":
        print(a/b)
    if sembol=="//":
        print(a//b)
    if sembol=="%":
        print(a%b)
a=int(input("enter the number"))
b=int(input("enter the number"))
sembol=input("entr sembol")
calculator(a,b,sembol)

