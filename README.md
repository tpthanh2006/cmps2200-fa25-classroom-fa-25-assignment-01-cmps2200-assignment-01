# CMPS 2200  Assignment 01

Please check assignment-01.md or assignment-01.pdf

You can include your written solutions in a new md or pdf file.

**Name:** Phu Thanh Tran

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
. Yes, $2^{n+1} is \in O(2^n)$. $2^{n+1} = $2^{n} * 2, which is just $2^{n} multiplied by a constant factor.
. In Big-O Notation, multiplying by a constant does not change the asymptotic class. 

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
. No, $2^{2^n} is not \in O(2^n)$. $2^{2^n} grows much faster than $2^n as it is an exponential of an exponential, while $2^n is just exponential.
. For large n, $2^{2^n} will always outpace $2^n.

  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
. No, $n^{1.01} not \in O(\mathrm{log}^2 n)$. $n^{1.01} is a polynomial function, while $\mathrm{log}^2 n grows much slower.

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
. Yes, $n^{1.01} \in \Omega(\mathrm{log}^2 n)$. $n^{1.01} grows much faster than $\mathrm{log}^2 n for large n.

  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
. No, $\sqrt{n} is not \in O((\mathrm{log} n)^3)$.
. For any constant c, $\sqrt{n} will eventually be greater than c * $(\mathrm{log} n)^3.
  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
. Yes, $\sqrt{n} is \in \Omega((\mathrm{log} n)^3)$ as there exists a constant c and n0 such that $\sqrt{n} is larger than or equal to c * ((\mathrm{log} n)^3) for all n >= n0.