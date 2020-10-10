#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) this is O(n), the body is constant and is repeated n times

b) this i O(n^2), recognized by nested loops, not as good as it can be and may work for smaller sample sizes but should be improved if possible

c) this is O(2^n), it is similar to the fibonacci recursive algorithm, where answers to lesser value inputs are required first, as they are part of the final answer

## Exercise II

we would use an approach similar to a binary search, where we start at a floor halfway to the top and drop one.
Depending on if it broke or not we would move up or down, the distance determined by half the remaining floors.
Continue this way until we found the highest floor where it would not break when dropped.
This would be a O(log n) complexity because we are removing half of the possibilites on each try.
