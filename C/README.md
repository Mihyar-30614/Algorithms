# Problem C: Flood Modeling
Your task is to model how a piece of terrain would be flooded if it were covered with a large amount
of water. The terrain is represented as a rectangular grid with square cells. Each cell has a certain
height given as a non-negative integer. An example of such a model is the 3x3 rectangle specified
in the first sample input and depicted in the figure (see C.pdf).

Now imagine that a large amount of water is poured over the terrain.
Any water that lands on a border cell spills off into the unbounded
area outside the grid, but water that lands on an inner cell is either
trapped there or spills onto one or more adjacent cells, where again
it may be trapped or may spill further onto yet other adjacent cells,
and so on, potentially reaching border cells and leaving the grid. For
the purposes of this problem, “adjacent” means directly north, south, east, or west.

As your intuition probably tells you, water will be trapped above an 
inner cell if that cell lies in a “valley” formed by the surrounding terrain.
More formally, water at some height h > 0 above an inner cell
C is trapped if and only if it is impossible for that water to travel to
the unbounded area outside the grid by moving from cell to adjacent
cell without going uphill at some point.
In our particular example, water will be trapped above the middle cell (which itself has height 1) up
to height 2, since any water higher than that will spill onto the adjacent cell to the south with height 2
(the bottom middle cell) and then leave the grid. Therefore the height of the water trapped above the
middle cell is 1. Notice that water trapped above the middle cell cannot escape to either of the two
corner cells with height 0, since cells that are positioned diagonally with respect to each other are not
considered adjacent.

Your challenge is to write a program that computes the height of water trapped above each cell after
the flooding. The expected output for the terrain in the figure is given in the first sample output.

### For more details see c.pdf 
