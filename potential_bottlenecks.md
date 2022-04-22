The Big O Notation allows us to state how larger datasets will affect complexity. It gives the
maximum amount of operations that might be needed to be executed for the task. For the code to
calculate the similarity between two input fingerprints, we need them to be somehow paired up.
This means for the whole dataset, we need all possible combinations of 2 in these n inputs. We
can think in terms of the simplified formula of the combination being n*(n-1) /2 which is quadratic;
every individual input has to pair with all other inputs one by one except for itself and (a,b) is
considered the same with (b,a) so we divide by 2. So since the code needs to calculate the
similarity score for all these pairs, the complexity and the amount of time it'll take will scale
quadratically. This case is often annotated by O(n ). So if an input size of 2 fingerprints which only
essentially requires 1 execution for the computation for the score lasts for on average 49.2 ms, an
input size of 1000 audio fingerprints that require 100_C_2 = 499,500 pairs and thus number or
executions would approximately take 49.2*499500= 24575400 ms= 6.8265 hours. This is actually a
computational bottleneck, where even the data is not very large, the code is running a
computationally intense task. Therefore, if we do not attempt an optimization for this code, I might
even fail to run this code on my local machine with the new weekly data because my CPU simply
might not have the capacity.
