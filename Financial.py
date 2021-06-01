# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:53:44 2021

@Roshan Raj Ramesh: 91824
"""

import numpy as np;
import matplotlib.pyplot as plt;

year = int(input("Enter number of year: "))

def h_w(n):
    return (5000+(5000*10/100)*(year-1))*n

#Product A

A_l = []
i_l = []

def cpu_A(n):
    if (n<=300):
        return 2;
    elif (n>300 and n<=600):
        return 4;
    else:
        return 8;
    
def disaster(d):
    return 30*(d/100)

def after5(a):
    return (a*(1+(0.18)*(year-1))) + (Hardware_a*(1+(0.15)*(year-1))) 

Hardware_a = 200000    

A1 = 100
A2 = 150
A3 = 300
A4 = 5000
A5 = 4000
A6 = 3000

for i in range(100, 1050, 50):
    i_l.append(i)
    cpu_count_a = cpu_A(i);
    Ba = cpu_count_a*(A4+A5+A6)
    A = i*(A1+A2+A3) + Ba
    AD = disaster(Ba)
    t = A+AD
    last = h_w(cpu_count_a*2)
    TCO = after5(t) + last
    A_l.append(TCO)
    print("TCO for product A", i ," users for ", year,"  years is ",TCO)

CAPEX_A = 165000 + Hardware_a + 24000 + (30/100*(24000)) + 5000*(2*2)
print("Total CAPEX for product A: ",int(CAPEX_A))
OPEX_A = ((165000 + 24000 + (30/100*(24000)))*0.18*4) + (Hardware_a*0.15*4) + (5000*0.1*4*4)
print("Total OPEX for product A: ",int(OPEX_A))
print("Total TCO for product A: ",int(CAPEX_A)+int(OPEX_A))

#Product B

B_l = []

def addsubs(B,i):
    return B+(300*year*i)

for i in range(100, 1050, 50):
    B = i*350
    BS = addsubs(B,i)
    B_l.append(BS)
    print("TCO for product B", i ," users for", year," years is ",BS)
#print(B_l)

CAPEX_B = 350*300
print("Total CAPEX for product B: ",int(CAPEX_B))
OPEX_B = 300*300*5
print("Total OPEX for product B: ",int(OPEX_B))
print("Total TCO for product B: ",int(CAPEX_B)+int(OPEX_B))
#Product C

C_l = []

def cpu_c(n):
    if (n<=400):
        return 2;
    elif (n>400 and n<=600):
        return 6;
    else:
        return 8;
    
    
Hardware_c = 500000

for i in range(100, 1050, 50):
    cpu_count = cpu_c(i);
    x = h_w(cpu_count)
    TCO_c = cpu_count*(25000*year) + Hardware_c + x
    C_l.append(TCO_c)
    print("TCO for product C", i ," users for", year," years is ",TCO_c)
    
CAPEX_C = 500000 + 5000*2
print("Total CAPEX for product C: ",int(CAPEX_C))

OPEX_C = 25000*5*2 + 5000*0.1*4*2
print("Total OPEX for product C: ",int(OPEX_C))

print("Total TCO for product C: ",int(CAPEX_C)+int(OPEX_C))

i_l = np.array(i_l)
A_l = np.array(A_l)
B_l = np.array(B_l)
C_l = np.array(C_l)


plt.plot(i_l,A_l,color='red', marker='.', label='Product A')
plt.plot( i_l, B_l, color='blue', marker='.', label='Product B')
plt.plot( i_l, C_l, color='olive', marker='.', label='Product C')
plt.legend()
plt.suptitle('TCO costs for 5 years')
plt.xlabel('Number of Users')
plt.ylabel('TCO Cost in M')
# Display a figure
plt.show()