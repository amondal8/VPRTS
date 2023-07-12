def trial():
    a=10
    print(f"value of a: {a}")
ant=(10,20)
print(ant)
trial()

class ani:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    # def printName(self):
    #     return
    def __str__(self):
        name=self.first+self.last
        return name

a1=ani("ani","mon")
a1.first="swa"

x=lambda a:a+10
print(f"The sum is: {x(5)}")


def myfunc(n):
    return lambda a:a*n

double=myfunc(2)
triple=myfunc(3)

print(double(10))
print(triple(20))

# del a1
print(a1)

print("""
Hello Sir,
     This is a multiple print statement.
""")

print(bool(10))

str1="banana"
for x in range(len(str1)):
    print(str1[x])
mylist=[]
# mylist=[str1[0:2],str1[0:3]]
mylist.append(str1[0:4])
print(mylist)

a=71
if(a>=90):
    print("90")
elif(a>80):
    print("80")
elif (a > 70):
    print("70")
else:
    print("null")
print("done")

def trial1():
    r,c=2,2
    # nwArr=[10]*10
    nwArr=[[0 for i in range(c)] for j in range(r)]
    nwArr[0][0]=9
    print(f"row: {len(nwArr)}, col: {len(nwArr[0])}")

    print(nwArr)
    for rows in range(r):
        for cols in range(c):
            print(f"{nwArr[rows][cols]}", end=" ")
        print()

    # print(f"{nwArr[0][1]}\n")

trial1()

a="12.9876557"
b=float(a)
print(b)
