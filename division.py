ACC = "0"
REG_Q = "0"
QUOTIENT = 0
REMAINDER = 0
DEC_DIVISIOR = 0
DEC_DIVIDEND = 0
BIN_DIVISIOR = ""
BIN_DIVIDEND = ""
ISPOS_DIVISIOR = True
ISPOS_DIVIDEND = True
BITS_DIVIDEND = 0
POSITIVE = "0"
NEGATIVE = "1"

def convertToBinary(dec,length):
	binary = bin(dec)[2:]
	binary = "0"*(length-len(binary))+binary
	return binary
def twosComplementtoDec(binary):
	global NEGATIVE
	pos = True
	if(binary[0] == NEGATIVE):
		binary = twosComplement(binary)
		pos = False
	if(pos):
		return int(binary,2)
	else:
		return -int(binary,2)


def leftShift(binary):
	binary = binary[1:]+"0"
	return binary

def onesComplement(i):
	ans = ""
	for t in i:
		if t == '0':
			ans = ans + '1';
		else:
			ans = ans + '0';
	return ans

def add(i,j):
	ans = ""
	carry ="0"
	length = len(i)-1
	# print(length)
	print(len(i)," ",len(j))
	while(length>=0):
		temp = int(carry) + int(i[length])+int(j[length])
		if(temp>1):
			carry ="1"
		else:
			carry ="0"
		if(temp%2 == 1):
			ans = "1" + ans
		else:
			ans = "0"+ans 
		length = length - 1
	return ans


def sub(i,j):
	temp = twosComplement(j)
	# print(temp)
	temp = add(i,temp)
	print(temp+"sub")
	return temp


def twosComplement(i):
    temp = onesComplement(i)
    
    return add(temp, "00000000001")


def main():
	global ACC
	global REG_Q
	global REG_M
	global DEC_DIVISIOR
	global DEC_DIVIDEND
	global BIN_DIVIDEND
	global BIN_DIVISIOR
	global ISPOS_DIVISIOR
	global ISPOS_DIVIDEND
	global POSITIVE
	global NEGATIVE
	global QUOTIENT
	global REMAINDER
	print("Enter the Dividend")
	DEC_DIVIDEND = int(input())
	
	print("Enter the Divisior")
	DEC_DIVISIOR = int(input())

	if(DEC_DIVISIOR == 0):
		print("Cannot Divide by 0")
		return

	if(DEC_DIVISIOR<0):
		DEC_DIVISIOR = - DEC_DIVISIOR
		ISPOS_DIVISIOR = False

	if(DEC_DIVIDEND < 0):
		DEC_DIVIDEND = -DEC_DIVIDEND
		ISPOS_DIVIDEND = False


	BIN_DIVISIOR = convertToBinary(DEC_DIVISIOR,11)
	BIN_DIVIDEND = convertToBinary(DEC_DIVIDEND,22)

	ACC = 11*"0"
	REG_Q = 11*"0"
	REG_M = 11*"0"

	ACC = BIN_DIVIDEND[:11]
	REG_Q = BIN_DIVIDEND[11:]
	REG_M = BIN_DIVISIOR

	COUNTER = 11
	print("STEP:",0," ACC:",ACC,"REG_Q:",REG_Q,"REG_M",REG_M)

	for i in range(COUNTER):
		ACCPLUSREGQ = ACC+REG_Q
		ACCPLUSREGQ = leftShift(ACCPLUSREGQ)
		print("Shifted Dividend", ACCPLUSREGQ)

		
		ACC = ACCPLUSREGQ[:11]
		
		REG_Q = ACCPLUSREGQ[11:]

		previousACC = ACC

		if REG_M[0] == ACC[0]:
			ACC = sub(ACC,REG_M)

		else:
			ACC = add(ACC,REG_M)
		print("After sub/add",ACC,REG_Q,REG_M)
		if ACC[0] == previousACC[0] or (ACC == 11*"0") or (REG_Q == 11*"0"):
			REG_Q = REG_Q[:-1] + "1"
		else:
			print("Restored")
			ACC = previousACC
		print("STEP:",i+1," ACC:",ACC,"REG_Q:",REG_Q,"REG_M",REG_M)

	if (not ISPOS_DIVIDEND) and ISPOS_DIVISIOR :
		REG_Q = twosComplement(REG_Q)
		ACC = twosComplement(ACC)

	elif (ISPOS_DIVIDEND) and not ISPOS_DIVISIOR :
		REG_Q = twosComplement(REG_Q)

	elif not ISPOS_DIVIDEND and not ISPOS_DIVIDEND:
		ACC = twosComplement(ACC)

	QUOTIENT = twosComplementtoDec(REG_Q)
	REMAINDER = twosComplementtoDec(ACC)
	
	print("QUOTIENT:" ,REG_Q, "REMAINDER:",ACC)

	print("QUOTIENT IN DECIMAL:",QUOTIENT," REMAINDER IN DECIMAL:",REMAINDER)

	


	

main()




		
