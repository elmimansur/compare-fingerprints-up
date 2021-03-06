I first run the code to see whether results match and the output is correct. The output verified that
the code runs correctly. To benchmark the code, I simply used the "timeit" library. I imported the
get_score function from the python file to a jupyter notebook. Because for this micro scale our input
size is only 2 and we call the get_score function only once, we can benchmark and profile that
function with the example fingerprints as its arguments to have an idea about how it is performing
in this smallest scale and hopefully identify some bottlenecks before moving on to dealing with
larger datasets. I use the Jupyter cell magic %timeit to benchmark and see how long it is taking the
function to run on average.


Then, to profile the code, I used the cell magic %prun. The output tells me most of the total time is
being spend in the correlation function. But the function get_score, even though it's only called
once, does have a high amount of time spent on that single call.

To get a better understanding of the distribution, I used line profiler. I first load the magic
with %load_ext line_profiler and then use it on the get_score function. We can see again, the
correlation function takes a long time both in total and per hit. So decided to line profile the
correlation function too. For its offset argument, since it ranges from -300 to 300, 1 by 1, I've put a
random integer between those to exemplify the performance of a single execution. As expected,
loops are taking a slightly longer time. Also, line 32, which uses the count method to count the
1s that corresponds to the two input byte strings' differences, is taking 62% of the time also with the
longest time per hit.

Lastly, I did a memory profiling both using %memit to see total memory used by get_score
and using the line-by-line memory profiling with %mprun to first the correlation and then the
get_score function. I first load the magic with %load_ext memory_profiler and I, then, use memit
magic on get_score and we see that the function only uses 59.26 MiB and increments it only
by 0.12 MiB. I, then, use the line-by-line profile to look at both functions in order. I can see that as
they start they increment by a big percentage of the memory all at once, most of this memory is the
memory used by the variables. Therefore, from the small increments in these function, we can
assume that there isn't a major memory problem at least at this scale.
