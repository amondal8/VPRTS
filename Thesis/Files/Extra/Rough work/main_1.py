# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sol(S):
    sum=0
    for char in S:
        if(char=='a'):
            sum+=1
    ways=0
    if(sum%3==0):
        lsum=sum/3
        msum=2*lsum
        sum=0
        count=0
        # for k in range(len(S)):
        #     print(f'Range is {k}')
        mylist1=[]
        mylist2=[]
        for i in range(len(S)-1):
            if(S[i]=='a'):
                sum+=1
            if(sum==msum):
                ways+=count
                mylist2.append(S[marking+1:i+1])
            if(sum==lsum):
                count+=1
                mylist1.append(S[0:i+1])
                marking=i

    print(mylist1)
    print(mylist2)
    return ways

print(sol("ababaababa"))
# print(sol("abcacac"))     ababa
# See PyCharm help at http
# s://www.jetbrains.com/help/pycharm/
