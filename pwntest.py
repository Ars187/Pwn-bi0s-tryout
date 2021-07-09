from pwn import *
import math
from Crypto.Util.number import inverse
con=remote('challenges.traboda.com',30840)
con.recvuntil('?\n\n')
con.sendline('madrid')
print(con.recvline())
con.recvuntil(' ?\n\n')
con.sendline('vincent van gogh')
print(con.recvline())
con.recvuntil('e?\n\n')
con.sendline('alan turing')
print(con.recvline())
con.recvuntil('mean!\n\n\t')
l=[]
for i in range(5):
	s=con.recvline()
	for j in s.split():
		if j.isdigit():
			l.append(int(j))
avg=sum(l)/len(l)
con.sendline(str(math.floor(avg)))
print(con.recvline())
a=con.recvline()
for j in a.split():
	if j.isdigit():
		a=int(j)
con.sendline(str(avg*a))
print(con.recvline())
con.recvuntil('order!\n')
ls=[]
b=con.recvline()
for j in b.split():
	if j.isdigit():
		ls.append(int(j))
ls.sort()
d = ' '
for i in ls:
    d=d+str(i)+' '
con.sendline(d)
print(con.recvline())
print(con.recvline())
con.recvuntil('t?\n\n')
con.sendline(b' crypto{ASCII_pr1nt4bl3}')
print(con.recvline())
con.recvuntil('Cipher?\n\n')
con.sendline(b' pprwr laaqm')
print(con.recvline())
con.recvuntil(')\n\n')
n = 882564595536224140639625987659416029426239230804614613279163
c = 77578995801157823671636298847186723593814843845525223303932
e = 65529 + len('GRYFFINDOR')
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
con.sendline(str(m))
con.recvuntil('y?\n\n')
print(con.recvline())
