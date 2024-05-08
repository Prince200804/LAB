def conversion(a):
    temp = count - len(a)
    return "0"*temp+a

def twos(a):
    res = list(a)
    i = len(a)-1
    f = 0
    while(i!=-1):
        while(f==0):
            if a[i] != "1":
                res[i] = a[i]
                i = i-1
            else: 
                res[i] = a[i]
                f = 1
                i = i-1
                break
            
        if a[i] == "0":
            res[i] = "1"
        else: 
            res[i] = "0"
        i = i-1

    return "".join(res)

def rightShift(AC, Q, Q1):
    ac = list(AC)
    q = list(Q)
    q[0] = AC[-1]
    q1 = Q[-1]
    for i in range(1, len(AC)):
        ac[i] = AC[i-1]
    for i in range(1, len(Q)):
        q[i] = Q[i-1]
    return "".join(ac), "".join(q), q1

def add(AC, M_NEG):
    carry = 0
    res = list(AC)
    for i in range(len(AC)-1,-1,-1):
        sum = int(AC[i]) + int(M_NEG[i]) + carry
        if(sum == 0):
            res[i] = "0"
            carry = 0
        elif (sum == 1):
            res[i] = "1"
            carry = 0
        elif(sum == 2):
            res[i] = "0"
            carry = 1
        elif(sum == 3):
            res[i] = "1"
            carry = 1   
    return "".join(res)         

x = int(input("Enter the multiplicand: "))
y = int(input("Enter the multiplier: "))

x = bin(x).replace("0b", "")
y = bin(y).replace("0b", "")

negative_x = 0
negative_y = 0

if x[0] == "-":
    x = x.replace("-","")
    negative_x = 1

if y[0] == "-":
    y = y.replace("-","")
    negative_y = 1

if len(x) > len(y):
    count = len(x) + 1
else: 
    count = len(y) + 1

x = conversion(x)
y = conversion(y)
x_neg = twos(x)
y_neg = twos(y)

if(negative_x == 0):
    M = x
    M_NEG = x_neg
else:
    M = x_neg
    M_NEG = x

if(negative_y == 0):
    Q = y
else:
    Q = y_neg

AC = "0"*count
Q1 = "0"

print("The table for the Booth's algorithm is as follows: ")
print("Count \tAC \tQ \tQ1 \tOperation")
print(f"{count} \t{AC} \t{Q} \t{Q1} \tInitial")

for i in range(count-1,-1,-1):
    if(Q[-1] == Q1):
        AC, Q, Q1 = rightShift(AC, Q, Q1)
        print(f"{i} \t{AC} \t{Q} \t{Q1} \tRight Shift")

    elif(Q[-1]+Q1 == "10"):
        AC = add(AC, M_NEG)
        AC, Q, Q1 = rightShift(AC, Q, Q1)
        print(f"{i} \t{AC} \t{Q} \t{Q1} \tAC = AC-M and Right Shift")

    elif(Q[-1]+Q1 == "01"):
        AC = add(AC, M)
        AC, Q, Q1 = rightShift(AC, Q, Q1)
        print(f"{i} \t{AC} \t{Q} \t{Q1} \tAC = AC+M and Right Shift")

if(AC[0] == "1"):
    print(f"-{int(twos(AC+Q),2)}")
else:
    print(f"{int((AC+Q),2)}")


