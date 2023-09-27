from scipy.stats import norm 
import math

m=31.5 
n=100 
n_s = math.sqrt(n)
s=5   
h= 0 
h= m + norm.ppf(0.95)* s/n_s

#print(h) 

m=60.17
n=100 
n_s = math.sqrt(n)
s=8 
h= 0  
d= 0 
h= m + norm.ppf(0.975)* s/n_s
d = m - norm.ppf(0.975)* s/n_s 

#print(d) 
#print(h) 

m=5100
n=50
n_s = math.sqrt(n)
s=500 
h= 0  
d= 0 
h = m + norm.ppf(0.975)* s/n_s
d = m - norm.ppf(0.975)* s/n_s  

#print(h) 
#print(d) 

m=2.06
n=10
n_s = math.sqrt(n)
s=0.2
h= 0  
d= 0 
h = m + norm.ppf(0.975)* s/n_s
d = m - norm.ppf(0.975)* s/n_s  

#print(h) 
#print(d)  

m=139.13
n=15
n_s = math.sqrt(n)
s=6.260990337
A = norm.ppf(0.95)
h= 0  
d= 0  
h = m + A * s/n_s
d = m - A * s/n_s     

c = 142 
t= 0
t = (m - c)/s * n_s

#print(d) 
#print(h)  
#print(T)

#print(norm.ppf(0.95)) 

m=0
n=6
n_s = math.sqrt(n)
s= 1
A = 2.0150
t_d= 0  
t_h= 0  
t_d = m -s/n_s * A
t_h= m + s/n_s * A   

#print(t_h)
#print(t_d) 

print norm.ppf(0.975)

m=60.17
n=100 
n_s = math.sqrt(n)
s=8 
h= 0  
d= 0 
h= m + norm.ppf(0.975)* s/n_s
d = m - norm.ppf(0.975)* s/n_s 

print(d) 
print(h) 