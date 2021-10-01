#function to convert integer to binary
def binary(n):
    res = ''
    while (n > 0):
        res += str(n % 2)
        n = n // 2
    res = res[::-1]
    strn = len(str(n))
    return res.zfill(strn)

#function to add binary numbers
def add_binary(n, m, e):
    max_len = max(len(n), len(m))
    n = n.zfill(max_len)
    m = m.zfill(max_len)
    res = ''
    carry = 0
    
    #iterating through the binary numbers considering carry bits
    for i in range(max_len - 1, -1, -1):
        if (carry==0):
            if (n[i]=='1' and m[i]=='1'):
                carry = 1
                res = '0' + res
            elif (n[i]=='1' and m[i]=='0'):
                res = '1' + res
            elif (n[i]=='0' and m[i]=='1'):
                res = '1' + res
            elif (n[i]=='0' and m[i]=='0'):
                res = '0' + res
        else:
            if (n[i]=='1' and m[i]=='1'):
                res = '1' + res
            elif (n[i]=='1' and m[i]=='0'):
                res = '0' + res
            elif (n[i]=='0' and m[i]=='1'):
                res = '0' + res
            elif (n[i]=='0' and m[i]=='0'):
                carry = 0
                res = '1' + res
    if (carry==1):
        e = '1'
    return (res, e)
    
#function to right shift
def right_shift(e, a, q):
    q = a[len(a)-1] + q[0:len(a)-1]
    a = e + a[0:len(a)-1]
    e = '0'
    return [e,a,q]
    
#starting inputs
question = input("Decimal or Binary? ")
if (question.lower() == "decimal"):
    b = int(input("Enter multiplicand: "))
    q = int(input("Enter multiplier: "))
    b = binary(b)
    q = binary(q)
elif(question.lower() == "binary"):
    b = input("Enter multiplicand: ")
    q = input("Enter multiplier: ")

#initializing e, a, sc
e = '0'
sc = max(len(b),len(q))
a = '0'.zfill(sc)

b_binary = b.zfill(sc)
q_binary = q.zfill(sc)

print('\n')
print('\t E \t A \t Q \t SC')
print('\t' + e + '\t' + a + '\t' + q_binary + '\t' + str(binary(sc)))
print('\n')

len_q = len(q_binary)

while(sc != 0):
    if (q_binary[len_q - 1] == '0'):
        e, a, q_binary = right_shift(e, a, q_binary)
        sc -= 1
        print('Shift \t' + e + '\t' + a + '\t' + q_binary + '\t' + str(binary(sc)))
        print('\n')
    else:
        a, e = add_binary(a, b_binary, e)
        print('Add \t' + e + '\t' + a + '\t' + q_binary )
        e, a, q_binary = right_shift(e, a, q_binary)
        sc -= 1
        print('Shift \t' + e + '\t' + a + '\t' + q_binary + '\t' + str(binary(sc)))
        print('\n')

ans = a + q_binary
print('Result in binary: ' + ans)
dec = int(ans, 2)
print('Result in decimal:', end=' ')
print(dec)   
