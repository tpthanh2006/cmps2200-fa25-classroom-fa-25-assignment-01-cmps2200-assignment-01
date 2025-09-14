# CMPS 2200  Assignment 01

Please check assignment-01.md or assignment-01.pdf

You can include your written solutions in a new md or pdf file.

**Name:** Phu Thanh Tran

1. (2 pts ea) **Asymptotic notation** (12 pts)
  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
    - Yes, $2^{n+1} \is in O(2^n)$\.
    - $2^{n+1} \= $2^n * 2\, which is just $2^n multiplied by a constant factor.
    - In Big-O Notation, multiplying by a constant does not change the asymptotic class. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
    - No, $2^{2^n} \is not in O(2^n)$\. $2^{2^n} \grows much faster than $2^n \as it is an exponential of an exponential, while $2^n \is just exponential.
    - For large n, $2^{2^n} \will always outpace $2^n\.
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
    - No, $n^{1.01} not \in O(\mathrm{log}^2 n)$. $n^{1.01} is a polynomial function, while $\mathrm{log}^2 n grows much slower.
  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
    - Yes, $n^{1.01} \in \Omega(\mathrm{log}^2 n)$. $n^{1.01} grows much faster than $\mathrm{log}^2 n for large n.
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
    - No, $\sqrt{n} is not \in O((\mathrm{log} n)^3)$.
    - For any constant c, $\sqrt{n} will eventually be greater than c * $(\mathrm{log} n)^3.
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
    - Yes, $\sqrt{n} is \in \Omega((\mathrm{log} n)^3)$ as there exists a constant c and n0 such that $\sqrt{n} is larger than or equal to c * ((\mathrm{log} n)^3) for all n >= n0.
  
2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  - DONE 

  - 2b. (6 pts) What does this function do, in your own words?  
    - If x <= 1, return x. Otherwise, the fibonacci number at position x will be equal to the sum of the fibonacci number at position x - 1 and x - 2.

  
3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`. - DONE

  - 3b. (4 pts) What is the Work and Span of this implementation?  
    - Work: O(n)$. Every element of mylist is visited once in a single loop, so the total work is linear in the size of the list.
    - Span: O(n)$. The loop is sequential; each iteration depends on the previous value of cnt, so the longest 

  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`. - DONE

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
    - Work: 𝑂(𝑛). Each level of recursion does O(1) work to combine results, and there are O(logn) levels, but every element is touched once, so total work is O(n).
    - Span: O(logn). The recursion splits the list in half each time, so the longest chain of dependent calls is O(logn).

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?
  - Work: O(n). The work remains the same as the sequential version because parallelization doesn't change the total number of operations needed.
  - Span: O(log n). With parallelization, both recursive calls run simultaneously, so the span is determined by the depth of the recursion tree, which is log n since we split in half each time.    