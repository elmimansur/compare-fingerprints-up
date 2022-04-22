The original code needs the user to replicate the code for every pair of fingerprints individually. This
both is time-consuming and not user friendly. Therefore it would be useful to develop a code that
can have the whole dataset as an input. For this, we could make use of numpy functions and data
structures, which would hopefully also help with computational complexity because it would
execute it in c-compiled code. We could vectorize functions to decrease the time spent in loops.
We could also compile the code with cython.
Also by creating a dictionary and storing it would be useful since we are likely to repeat these
comparisons weekly. Only the new fingerprints would be calculated, which would be less
computationally complex. However, it would be very difficult to parallelize this code. Because every
process needs every fingerprint in the memory to be able to compare it to every other fingerprint
and to avoid duplicate comparisons.
