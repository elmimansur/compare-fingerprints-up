I included a new function to be able to calculate more than two fingerprints' comparisons at once. 
I also used vectorized functions. I cythonized the code in Jupyter with cell magic. With "-a", 
I was able to see that even though I tried to specify most of the variables' types, the majority of the code was still highlighted by bold yellow, 
meaning it was mostly running in python. This cython code takes a longer time than the original code for an input of size 2. 
However, as I applied it for larger datasets, it gradually became faster than the time the original code would take. 
The initial slowness was because compiling the code adds overhead. Also, the function processes every file which adds additional overhead. 
For memory efficiency purposes, I created a dictionary with tuple fingerprints as keys and their comparison value as values. 
I, then, saved this dictionary to redis. This would also decrease time spent for the weekly operations. 
One could easily query a tuple and get the comparison score. 


%%% Not the best attempt...
