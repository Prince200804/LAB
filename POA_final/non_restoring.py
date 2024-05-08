def conversion(a):
    temp = count - len(a)
    return "0"*temp + a

def twos(a):
    res = list(a)
    i = len(a) - 1
    f = 0
    while(i!=-1):
        while(f==0):
            if(res[i] != "1"):
                res[i] = a[i]
                i = i-1
            else:
                res[i] = a[i]
                i = i-1
                f=1
                break
            
        if(res[i] == "0"):
            res[i] = "1"
        else:
            res[i] = "0"
        i = i-1

    return "".join(res)

def leftShift(AC, Q):
    ac = list(AC)
    q = list(Q)
    ac[-1] = Q[0]
    for i in range(0, len(AC)-1):
        ac[i] = AC[i+1]
    for i in range(0, len(Q)-1):
        q[i] = Q[i+1]
    return "".join(ac),"".join(q)

def add(AC, M_neg):
    carry = 0
    res = list(AC)
    for i in range(len(AC)-1,-1,-1):
        sum = int(AC[i]) + int(M_neg[i]) + carry
        if(sum == 0):
            res[i] = "0"
            carry = 0
        elif(sum == 1):
            res[i] = "1"
            carry = 0
        elif(sum == 2):
            res[i] = "0"
            carry = 1
        elif(sum == 3):
            res[i] = "1"
            carry = 1
    return "".join(res)

Q = int(input("Enter Divident: "))
M = int(input("Enter Divisor: "))

Q = bin(Q).replace("0b", "")
M = bin(M).replace("0b", "")

count = len(Q) + 1

AC = "0"*count
M = conversion(M)
M_neg = twos(M)

print("The table for the Booth's algorithm is as follows: ")
print("Count \tAC \tQ \tOperation")
print(f"{count-1} \t{AC} \t{Q} \tInitial")

for i in range(len(Q)-1, -1, -1):
    AC, Q = leftShift(AC, Q)

    if(AC[0] == "1"):
        AC = add(AC, M)
        Q = list(Q)
        if(AC[0] == "1"):
            Q[-1] = "0"
        else:
            Q[-1] = "1"
        Q = "".join(Q)
        print(f"{i} \t{AC} \t{Q} \tLeft Shift, Add M")
    else:
        AC = add(AC, M_neg)
        Q = list(Q)
        if(AC[0] == "1"):
            Q[-1] = "0"
        else:
            Q[-1] = "1"
        
        Q = "".join(Q)
        print(f"{i} \t{AC} \t{Q} \tLeft Shift, Sub M")

if(AC[0] == "1"):
    AC = add(AC, M)

print(f"Remainder: {int(AC,2)}, Quotient: {int(Q,2)}")
