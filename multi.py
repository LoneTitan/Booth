#Convert decimal to  binary
def dtb(i):
    ans = "";
    temp = abs(i);
    while(temp > 0):
        ans = str(temp%2) + ans ;
        temp = temp//2;
    for i in range(len(ans), 31):
        ans = '0' + ans
    return(ans);

#Perform left shift  operation
def rightShift(i):
    return i[:-1]

#Perform Right shift operation
def leftShift(i):
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
            ans = ans + "0"
            carry = True;
    if carry:
        ans = ans + "1"
    ans = ans[::-1]
    return ans

#Calculate twos complement
def twosComplement(i):
    temp = onesComplement(i)
    return binaryAdd(temp, "1")

def main():
    a = int(input())
    b = int(input())

    a_bin = dtb(abs(a));
    b_bin = dtb(abs(b));

    #Normalise the binary
    maxlen = max(len(a_bin), len(b_bin)) - 1;
    if(a < 0):
        a_bin = "1" + a_bin
    else:
        a_bin = "0" + a_bin
    if(b < 0):
        b_bin = "1" + b_bin
    else:
        b_bin = "0" + b_bin
    #Normalisation done

    ac = "00000000000000000000000000000000"
    q_npo = '0'
    counter = 32
    while not counter == 0:
        print(ac , a_bin , q_npo)
        counter = counter - 1;
        if(a_bin[-1] == '1' and  q_npo ==  '0'):
            ac = binaryAdd(ac,twosComplement(b_bin))
        elif(a_bin[-1] == '0' and  q_npo ==  '1'):
            ac = binaryAdd(ac,b_bin)
        q_npo = a_bin[-1]
        last = ac[-1]
        if(ac[0] == '0'):
            ac = '0' + ac
        else:
            ac = '1' + ac
        a_bin = last + a_bin
        ac = rightShift(ac)
        a_bin = rightShift(a_bin)
    if((a < 0 and b < 0) or (a > 0 and b > 0)):
        a_bin = '0' + a_bin[2:]
    if((a < 0 and b > 0) or (a > 0 and b < 0)):
        a_bin = '1' + a_bin[2:]
    if(a_bin[0] == '1'):
        print('-' + str(int('0'+a_bin[2:], 2)))
    else:
        print(int('0'+a_bin[2:], 2))

main()
