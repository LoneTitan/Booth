#Convert decimal to  binary
def dtb(i):
    ans = "";
    temp = abs(i);
    while(temp > 0):
        ans = str(temp%2) + ans ;
        temp = temp//2;
    return(ans);

#Perform left shift  operation
def rightShift(i):
    return i[:-1]

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
            carry = False;
            ans = ans + "0";
        elif s == '0' and t == '0' and carry:
            carry = False;
            ans = ans + "1";
        elif ((s == '0' and t == '1') or (s == '1' and t == '0')) and not carry:
            ans = ans + "1"
            carry = False;
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
    maxlen = max(len(a_bin), len(b_bin));

    #All length same
    for p in range(len(a_bin), maxlen+1):
        a_bin = '0' + a_bin;
    for p in range(len(b_bin), maxlen+1):
        b_bin = '0' + b_bin;

    #If negative take twos complement
    if(a < 0):
        a_bin = twosComplement(a_bin)
    if(b < 0):
        b_bin = twosComplement(b_bin)

    maxlen = max(len(a_bin), len(b_bin));
    print(a_bin + "   " + b_bin)
    #Normalisation done
    ac = ''
    for p in range(0,maxlen):
        ac += '0'
    q_npo = '0'
    counter = maxlen

    while not counter == 0:
        #Printing values
        print(ac , a_bin , q_npo, counter)
        counter = counter - 1;

        #FlowChart condition 1
        if(a_bin[-1] == '1' and  q_npo ==  '0'):
            ac = binaryAdd(ac,twosComplement(b_bin))
        #FlowChart condition 2
        elif(a_bin[-1] == '0' and  q_npo ==  '1'):
            ac = binaryAdd(ac,b_bin)
            print(ac)
        ac = ac[-maxlen:]
        #Shifting
        q_npo = a_bin[-1]
        last = ac[-1]
        if(ac[0] == '0'):
            ac = '0' + ac
        else:
            ac = '1' + ac
        if(counter == -1):
            break
        a_bin = last + a_bin
        ac = rightShift(ac)
        a_bin = rightShift(a_bin)
    print(ac + "   " + a_bin)
    ans = ac + a_bin
    print(ans)
    if(ans[0] == '1'):
        ans = twosComplement(ans)
    print(int(ans, 2))

main()
#print(binaryAdd("1110","0111"))
