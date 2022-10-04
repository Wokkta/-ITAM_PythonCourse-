2.A
N = input()
users=[]
for i in range (0,int(N)):
    users.append(input().split())
ocn = 0
zaocn = 0
for i in range (0,len(users)):
    if users[i][-1]=="True":
        ocn+=1
    else: zaocn+=1
print(ocn," ",zaocn)
2.B
N = input()
users=[]
for i in range (0,int(N)):
    users.append(input().split())
print(users)
ocn = 0
zaocn = 0
undef = 0
for i in range (0,len(users)):
    bol=0
    for j in range(0,len(users[i])):
        if users[i][j]=="True" or users[i][j]=="False":
            bol+=1
    if bol ==1:
        for q in users[i]:
            if q=="True":
                ocn+=1
            elif q=="False":
                zaocn+=1
    elif bol >=2:
            if users[i][-1] == "True":
                   ocn+=1
            elif users[i][-1] == "False":
                   zaocn+=1
            else: undef+=1
                   
print(ocn," ",zaocn," ",undef)

2.C
x = "thisisabracadabraHt1eadljjl12ojh."
g = ""
for _ in range(len(x)):
    if (x[_].isupper()):
        g += x[_]
    if (x[_].isdigit()):
        break
print(g + x[_+1:len(x):3])

2.D
x = "4 5 3 4 2 3".split()
for _ in range(len(x)-1):
    x = x[1:]+x[:1]
print(" ".join(x))
x = "3 5 7 9".split()
for _ in range(len(x)-1):
    x = x[1:]+x[:1]
print(" ".join(x))