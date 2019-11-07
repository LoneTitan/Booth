#Convert decimal to  binary
def dtb(i):
    ans = "";
    temp = abs(i);
    while(temp > 0):
        ans = str(temp%2) + ans ;
        temp = temp//2;
    print(ans);

#Perform left shift  operation
def leftShift(i):
    return i[:-1]

#Perform Right shift operation
def rightShift(i):
    return i+"0"

#Take ones complement
def onesComplement(i):
    ans = ""
    for t in i:
        if t == '0':
            ans = ans + '1';
        else:
            ans = ans + '0';
    return ans

#Adds two binary numers
def binaryAdd(i,j):
    ans = "";
    carry = False;
    maxlen = max(len(i), len(j))
    for t in range(0,maxlen-len(i)):
        i = "0" + i
    for t in range(0,maxlen-len(j)):
        j = "0" + j
    i = i[::-1]
    j = j[::-1]
    for s,t in zip(i,j):
        if s == '1' and t == '1' and not carry:
            carry = True;
            ans = ans + "0";
        elif s == '1' and t == '1' and carry:
            carry = True;
            ans =  ans + "1";
        elif s == '0' and t == '0' and not carry:
            ans = ans + "0"
        elif s == '0' and t == '0' and carry:
            carry = False
            ans = ans + "1"
        elif ((s == '0' and t == '1') or (s == '1' and t == '0')) and not carry:
            ans = ans + "1"
        elif ((s == '0' and t == '1') or (s == '1' and t == '0')) and carry:
            ans = ans + "1"
            carry = False;
        else:
            print(ans)

    if carry:
        ans = ans + "1"
    ans = ans[::-1]
    return ans

#Calculate twos complement    
def twosComplement(i):
    temp = onesComplement(i)
    return binaryAdd(temp, "1")
print(binaryAdd("000","000"))
