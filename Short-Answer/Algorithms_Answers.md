#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) this is O(n), the body is constant and is repeated n times

b) this is O(n log n), j is doubling on line 20, so it makes the inner loop O(log n), and the outer is O(n)

c) this is O(n), it is a recursive function that calls itself n times based on input

## Exercise II

we would use an approach similar to a binary search, where we start at a floor halfway to the top and drop one.
Depending on if it broke or not we would move up or down, the distance determined by half the remaining floors.
Continue this way until we found the highest floor where it would not break when dropped.
This would be a O(log n) complexity because we are removing half of the possibilites on each try.
