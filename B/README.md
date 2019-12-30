# Problem B: Shortlex
The set of all binary strings of finite length, denoted {0, 1}, plays an
important role in computer science, and it is often useful to impose
an ordering on the elements of this set. One option is standard lexicographic
order (dictionary order with the convention that 0 comes
before 1), but this has a serious drawback: every string that starts
with 0 appears before every string that starts with 1, and since there
are infinitely many strings that start with 0, it is impossible to assign
a finite index to any string that starts with 1. A better option is lengthlexicographic
order, also known as shortlex order, which is based on
two simple rules. For x, y in {0; 1}*:
1. if the length of x is less than the length of y, then x precedes y
2. if x and y have the same length, then they are ordered lexicographically relative to each other

### Read B.pdf for more details
