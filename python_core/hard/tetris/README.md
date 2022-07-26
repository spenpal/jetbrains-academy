# Tetris

## Stage 1
### Description
The original Tetris game has 7 unique pieces, each made up of 4 segments: the `T` piece, the `O` piece, the `L` piece, the `J` piece, the `I` piece, the `S` piece, and the `Z` piece.

In this stage, you need to design the pieces and show how they can be rotated counterclockwise at 90 degrees inside a 4x4 grid.

    00 01 02 03
    04 05 06 07
    08 09 10 11
    12 13 14 15

The numbers `00 01 02 03` represent the first items on the four columns of the grid. The numbers below represent the first items of the grid rows.

    00
    04
    08
    12

So, a 4x4 grid should have four rows and columns — naturally, a 4x4 matrix. Every element in our matrix is filled with a hyphen, `-`, and one space.

    - - - -
    - - - -
    - - - -
    - - - -

Each piece is designed with the help of four zeros `(0)`. They are our building segments. In the end, we should have the following:

The `I` piece:

    - 0 - -
    - 0 - -
    - 0 - -
    - 0 - -

The `S` piece:

    - - - -
    - 0 0 -
    0 0 - -
    - - - -

The `Z` piece:

    - - - -
    0 0 - -
    - 0 0 -
    - - - -

The `L` piece:

    - 0 - -
    - 0 - -
    - 0 0 -
    - - - -

The `J` piece:

    - - 0 -
    - - 0 -
    - 0 0 -
    - - - -

The `O` piece:

    - - - -
    - 0 0 -
    - 0 0 -
    - - - -

The `T` piece:

    - 0 - -
    0 0 0 -
    - - - -
    - - - -

### Objectives
In this stage, your program should:

1.  Create a 4x4 grid.
2.  Design seven unique pieces: `I, S, Z, L, J, O, T`
3.  Design the rotated states of the unique pieces.
4.  The pieces and their rotated states should be placed inside one list. The unique piece should take the first position in the list. the next positions should be filled with the pieces rotated by 90 degrees counterclockwise.
5.  Rotate the pieces inside the grid. The piece is rotated automatically and should appear in a new grid
6.  Print and rotate the unique pieces in the order they were created. Separate each new grid with **one** empty line, as shown in the Examples below.

> There are several ways to represent the figures and their rotated states, use the design shown below for the sake of consistency.

    O = [[5, 6, 9, 10]]
    I = [[1, 5, 9, 13], [4, 5, 6, 7]]
    S = [[6, 5, 9, 8], [5, 9, 10, 14]]
    Z = [[4, 5, 9, 10], [2, 5, 6, 9]]
    L = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
    J = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
    T = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]

> Print a unique piece first. Then print new grids with all its rotated states. The O piece does not change on rotation, so it has only one state. A piece will be rotated four times as shown in the examples below.

### Examples
The example below shows how your program should work.

The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _typing "T" as input_

    > T

    - - - -
    - - - -
    - - - -
    - - - -
    
    - 0 - -
    0 0 0 -
    - - - -
    - - - -
    
    - 0 - -
    0 0 - -
    - 0 - -
    - - - -
    
    - - - -
    0 0 0 -
    - 0 - -
    - - - -
    
    - 0 - -
    - 0 0 -
    - 0 - -
    - - - -
    
    - 0 - -
    0 0 0 -
    - - - -
    - - - -

**Example 2:** _typing "J" as input_

    > J

    - - - -
    - - - -
    - - - -
    - - - -
    
    - - 0 -
    - - 0 -
    - 0 0 -
    - - - -
    
    - - - -
    0 0 0 -
    - - 0 -
    - - - -
    
    - 0 0 -
    - 0 - -
    - 0 - -
    - - - -
    
    0 - - -
    0 0 0 -
    - - - -
    - - - -
    
    - - 0 -
    - - 0 -
    - 0 0 -
    - - - -

---

## Stage 2
### Description

The original Tetris board design employs a 10x20 grid. Several variants of this design have emerged over the years, but the 10x24 option remains one of the most popular. Your game should allow for any board dimension, but use the 10x20 grid as the default one. The board is basically an MxN matrix, where M is the board width and N is the board height.

    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -

In the previous stage, we created our pieces in a 4x4 grid. At this stage, you need to simulate their movement on the Tetris board. The pieces should move from the top to the bottom every time a new command is printed. The player can also move the pieces to the left or right. Besides, the pieces can be rotated as they fall. Do not rotate them automatically. Your program should take instruction to rotate the piece or move it to the left or right.

The representation below shows how the unique pieces appear at the top of the game board:

    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    
    - - - - 0 0 - - - -
    - - - 0 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    - - - - 0 0 - - - -
    - - - - - 0 0 - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - - - - - - -
    
    - - - - - 0 - - - -
    - - - - - 0 - - - -
    - - - - 0 0 - - - -
    - - - - - - - - - -
    
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -

> You may need to redesign the pieces to fit them into your game board. There are multiple ways to do it, so please use the design shown below for the sake of consistency.

    O = [[4, 14, 15, 5]] 
    I = [[4, 14, 24, 34], [3, 4, 5, 6]] 
    S = [[5, 4, 14, 13], [4, 14, 15, 25]] 
    Z = [[4, 5, 15, 16], [5, 15, 14, 24]] 
    L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]] 
    J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]] 
    T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]

There are no border restrictions in this stage, so a piece can move through the bottom, left, and right borders:

    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 0 - - - -

Mind that when you move the piece down, you need to move it down precisely one row in the grid.

    - - - - - - - - - -
    - - - - - - - - 0 0
    - - - - - - - - 0 0
    - - - - - - - - - -
    
    > right
    - - - - - - - - - -
    - - - - - - - - - -
    0 - - - - - - - - 0
    0 - - - - - - - - 0

##### Objectives

In this stage, your program should:

1.  Take the unique pieces from the list.
2.  Move the piece to the left, right, and down.
3.  Rotate the piece inside the game board.

At this stage, your program should deal with the `rotate`, `left`, `right`, `down`, and `exit` commands.

##### Examples

The example below shows how your program should work.

The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _typing "I" (piece) and "10 20" (dimensions of the grid) as input_

    > I
    > 10 20
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > rotate
    
    - - - - - - - - - -
    - - - 0 0 0 0 - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > right
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 0 0 0 - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > right
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - 0 0 0 0 -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - 0 0 0 0 -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > rotate
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - 0 - - -
    - - - - - - 0 - - -
    - - - - - - 0 - - -
    - - - - - - 0 - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - 0 - - - -
    - - - - - 0 - - - -
    - - - - - 0 - - - -
    - - - - - 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > exit

**Example 2:** _typing "T" (piece) and "10 24" (dimensions of the grid) as input_

    > T
    > 10 24
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - 0 - - - - - -
    - - - 0 0 - - - - -
    - - - 0 - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 - - - - - - -
    - - 0 0 - - - - - -
    - - 0 - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > rotate
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 - - - - - - -
    - 0 0 0 - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > right
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - 0 - - - - - -
    - - 0 0 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > rotate
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > exit

---

## Stage 3
### Description
Now, once the pieces have been transferred and the player can move them across the board, we need to implement the borders to restrict the movement of pieces. In the previous stage, it was like that:

    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - 0 0
    - - - - - - - - 0 0
    - - - - - - - - - -
    - - - - - - - - - -

The `O` piece above moves through the left board's wall and emerges from the right as shown in the figure below.

    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 - - - - - - - - 0
    0 - - - - - - - - 0
    - - - - - - - - - -
    - - - - - - - - - -

Let's add a rule to restrict that. Create the borders so that the piece cannot move through the imaginary walls. And don't forget about the "floor". Your pieces should not fall through it. Once the piece hits the floor, it should be stored on the game board and remain static.

### Objectives

In this stage, your program should:

1.  Restrict the piece movement on the game board.
2.  Rotate the pieces as they move.
3.  Make the piece static once it hits the floor of the game board.

> Remember, your board can be of any size you want.

### Examples
The example below shows how your program should work.

The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _typing "O" (piece) and "10 10" (dimensions of the grid)_

    > O
    > 10 10
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - 0 0 - - - - -
    - - - 0 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 - - - - - -
    - - 0 0 - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - 0 0 - - - - - - -
    - 0 0 - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > right
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - 0 0 - - - - - - -
    - 0 0 - - - - - - -
    - - - - - - - - - -
    
    > right
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 - - - - - -
    - - 0 0 - - - - - -
    
    > down
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 - - - - - -
    - - 0 0 - - - - - -
    
    
    > right
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 - - - - - -
    - - 0 0 - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 - - - - - -
    - - 0 0 - - - - - -
    
    > exit

**Example 2:** _typing "L" (piece) and "10 10" (dimensions of the grid)_

    > L
    > 10 10
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > rotate
    
    - - - - - - - - - -
    - - - - - 0 - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > rotate
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 0 - - - -
    - - - - - 0 - - - -
    - - - - - 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - 0 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 - - - - - -
    - - - 0 - - - - - -
    - - - 0 - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - 0 0 - - - - - - -
    - - 0 - - - - - - -
    - - 0 - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    - 0 - - - - - - - -
    - 0 - - - - - - - -
    - - - - - - - - - -
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    - 0 - - - - - - - -
    - 0 - - - - - - - -
    
    > right
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    - 0 - - - - - - - -
    - 0 - - - - - - - -
    
    > down
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    - 0 - - - - - - - -
    - 0 - - - - - - - -
    
    
    > left
    
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    - 0 - - - - - - - -
    - 0 - - - - - - - -
    
    > exit

---

## Stage 4
### Description
We are not done yet. We know how to rotate a piece, move it from left or right, and store it on the floor. Also, we restricted all these movements to the four walls of the game board.

Let's take our game to the next level. In addition to other features we have implemented, at this stage, the piece should become static when it touches another piece. Another thing we should do is to make horizontal blocks disappear when a row is filled. The game should end when the game board is filled.

    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -

As you can see, the T piece is on the floor, static. We requested the `O` piece. If the `O` piece continues on its current path, it is going to touch the `T` piece and become static as shown below:

    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - 0 0 - - - - -
    - - - 0 0 - - - - -
    - - - 0 - - - - - -
    - - 0 0 0 - - - - -

The figure below shows the `O` piece and two rotated `I` pieces. The `O` and the first rotated piece are on the floor. When the second `I` piece hits the base, the entire row should disappear from the board:

    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - 0 0 0 0
    0 0 0 0 0 0 - - - -

The figure below shows the game board once it has been done:

    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -

The game should end once there is no more free space for our pieces.

> The column is considered filled when the height of the column equals the height of the pieces on the board. The row is considered filled when the row width equals the width of the row with pieces. We will also test if a moving piece can go through the static blocks. It means we will run the `down` command one more time when a piece is on top of a static block.

### Objectives
In this stage your program should:

1.  Make a piece static when it touches another piece on the game board.
2.  Make rows disappear. The rows should disappear when the user types the `break` command.
3.  Reduce the height of the block.
4.  End the game when the vertical column is filled.

All in all, your program should react to a number of input commands:

*   `piece`: indicating that the user wishes to enter a new piece into the game.
*   `rotate`, `left`, `right`, `down`: moving the piece within the grid.
*   `break`: making the filled row disappear.
*   `exit`: indicated that the user wants to end the game.

### Examples
The example below shows how your program should work.

The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1.**

    > 10 10
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > piece
    > T
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > rotate
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > piece
    > S
    - - - - 0 0 - - - -
    - - - 0 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > rotate
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - - 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - - 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - - 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - - 0 - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - - 0 - - - -
    - - - - 0 - - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    > piece
    > I
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    > piece
    > O
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    > down
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - 0 0 0 - - - -
    
    Game Over!

**Example 2.**

    > 10 10
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > piece
    > O
    - - - - 0 0 - - - -
    - - - - 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    - - - - - - - - - -
    - - - 0 0 - - - - -
    - - - 0 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 - - - - - -
    - - 0 0 - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - 0 0 - - - - - - -
    - 0 0 - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > left
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    - - - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > piece
    > I
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > rotate
    - - - - - - - - - -
    - - - 0 0 0 0 - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > left
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 0 0 - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 0 0 - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - 0 0 0 0 - - - -
    0 0 - - - - - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 0 0 0 0 - - - -
    0 0 - - - - - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > piece
    > I
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - 0 - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > rotate
    - - - - - - - - - -
    - - - 0 0 0 0 - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > right
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - 0 0 0 0 - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > right
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - 0 0 0 0 -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > right
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - 0 0 0 0
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - 0 0 0 0
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - 0 0 0 0
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - 0 0 0 0
    0 0 - - - - - - - -
    0 0 0 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - 0 0 0 0
    0 0 0 0 0 0 - - - -
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 0 0 0 0
    
    > down
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    0 0 0 0 0 0 0 0 0 0
    
    > break
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    - - - - - - - - - -
    0 0 - - - - - - - -
    
    > exit