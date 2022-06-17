# Dominoes

## Stage 1
### Theory
_Note:  
Before you start this project, it's better to get familiar with the basic domino rules. Keep in mind that there are many versions of the game. The rules used in this particular project will be described as we go along._

As you might know, a domino is a playing piece that is characterized by the two numbers written on it. The numbers are integers and can range from 0 to 6. A single domino piece has no orientation, so, a full domino set (that includes all the possible pairs of numbers) will have 28 unique dominoes.

You may think that there should be 7\*7=49 dominoes in total. However, this is not the case because the combinations like \[1,2\] and \[2,1\] are the same domino, not two separate ones.

### Description
To play domino, you need a full domino set and at least two players. In this project, the game is played by you and the computer.

At the beginning of the game, each player is handed 7 random domino pieces. The rest are used as stock (the extra pieces).

To start the game, players determine the starting piece. The player with the highest domino or the highest double (\[6,6\] or \[5,5\] for example) will donate that domino as a starting piece for the game. After doing so, their opponent will start the game by going first. If no one has a double domino, the pieces are reshuffled and redistributed.

`Status is the player, who is to make the next move`

### Objectives
1.  Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.  
    
2.  Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).  
    
3.  Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either `"player"` or `"computer"`.
    
        Stock pieces      # 14 domino elements
        Computer pieces   # 7 or 6 domino elements
        Player pieces     # 6 or 7 domino elements
        Domino snake      # 1 starting domino
        Status            # the player that goes first

    If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3).
4.  Output all five variables.

### Examples
**Example 1**
_The player makes the first move._

    Stock pieces: [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
    Computer pieces: [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3]]
    Player pieces: [[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6]]
    Domino snake: [[6, 6]]
    Status: player

  
**Example 2**
_The computer makes the first move._

    Stock pieces: [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2], [0, 1], [3, 3]]
    Computer pieces: [[0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5]]
    Player pieces: [[1, 3], [1, 4], [4, 5], [1, 6], [1, 1], [0, 4]]
    Domino snake: [[5, 5]]
    Status: computer
    
---
## Stage 2
### Description
A good game needs a good interface. In this stage, you will make your output user-friendly.

The player should be able to see the domino snake, the so-called playing field, and their own pieces. It's a good idea to enumerate these pieces because throughout the game the player will be selecting them to make a move.

Two things must remain hidden from the player: the stock pieces and the computer's pieces. The player should not be able to see them, only the number of pieces remaining.

### Objectives
1.  Print the header using seventy equal sign characters (`=`).
2.  Print the number of dominoes remaining in the stock – `Stock size: [number]`.
3.  Print the number of dominoes the computer has – `Computer pieces: [number]`.
4.  Print the domino snake. At this stage, it consists of the only starting piece.
5.  Print the player's pieces, `Your pieces:`, and then one piece per line, enumerated.
6.  Print the status of the game:  
    If `status = "computer"`, print `"Status: Computer is about to make a move. Press Enter to continue..."`  
    If `status = "player"`, print `"Status: It's your turn to make a move. Enter your command."`  
    Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.

### Examples
**Example 1**
_The player makes the first move (status = "player")_

    ======================================================================
    Stock size: 14
    Computer pieces: 6
    
    [6, 6]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[4, 6]
    5:[0, 1]
    6:[0, 5]
    7:[1, 6]
    
    Status: It's your turn to make a move. Enter your command.
  
**Example 2**
_The Computer makes the first move (status = "computer")_

    ======================================================================
    Stock size: 14
    Computer pieces: 7
    
    [5, 5]
    
    Your pieces:
    1:[1, 3]
    2:[1, 4]
    3:[4, 5]
    4:[1, 6]
    5:[1, 1]
    6:[0, 4]
    
    Status: Computer is about to make a move. Press Enter to continue...
    
---
## Stage 3
### Description
It's time to bring the game to life. In this stage, you need to add a game loop that will allow players to take turns until the end-game condition is met.

In dominoes, you can make a move by taking one of the following actions:

*   Select a domino and place it on the right side of the snake.
*   Select a domino and place it on the left side of the snake.
*   Take an extra piece from the stock (if it's not empty) and skip a turn.

To make a move, the player has to specify the action they want to take. In this project, the actions are represented by integer numbers in the following manner: `{side_of_the_snake (+/-), domino_number (integer)}` or `{0}`. For example:  
`-6` : Take the sixth domino and place it on the left side of the snake.  
`6` : Take the sixth domino and place it on the right side of the snake.  
`0` : Take an extra piece from the stock (if it's not empty) and skip a turn or simply skip a turn if the stock is already empty by this point.

When it's time for the player to make a move, your program must prompt the user for a number. If this number exceeds the limitations (larger than the number of dominoes), your program must generate an error message and prompt for input again. Once the valid input is received, your program must apply the move.

For now, don't bother about the AI, our goal is just to make the game playable. So, when it's time for the computer to make a move, make it choose a random number between `-computer_size` and `computer_size` (where the `computer_size` is the number of dominoes the computer has).

The end-game condition can be achieved in two ways:
1.  One of the players runs out of pieces. The first player to do so is considered a winner.
2.  The numbers on the ends of the snake are identical and appear within the snake 8 times. For example, the snake below will satisfy this condition:  
    `[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]`  
    These two snakes, however, will not:  
    `[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5]`  
    `[6,5],[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,1]`  
    If this condition is satisfied, it is no longer possible to go on with this snake. Even after emptying the stock, no player will have the necessary piece. Essentially, the game has come to a permanent stop, so we have a draw.
    

When the game ends, your program should print the result.

Throughout the gameplay, the snake will grow in length. If it gets too large, the interface might get ugly. To avoid this problem, draw only the first and the last three pieces of the snake, separate them by three dots, `...`, for example, `[3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]`.

### Objectives
Modify your Stage 2 code:
1.  At the end of the game, print one of the following phrases:  
    `Status: The game is over. You won!`  
    `Status: The game is over. The computer won!`  
    `Status: The game is over. It's a draw!`
2.  Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.
3.  Add a game loop that will repeat the following steps until the game ends:
    *   Display the current playing field (stage 2).
    *   If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: `Invalid input. Please try again.`.
    *   If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.
    *   Switch turns.

Keep in mind that at this stage we have no rules! Both the player and the computer can place their dominoes however they like.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1**
_Typical gameplay._

    ======================================================================
    Stock size: 14
    Computer pieces: 6
    
    [6, 6]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[4, 6]
    5:[0, 1]
    6:[0, 5]
    7:[1, 6]
    
    Status: It's your turn to make a move. Enter your command.
    > 4
    ======================================================================
    Stock size: 14
    Computer pieces: 6
    
    [6, 6][4, 6]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[0, 1]
    5:[0, 5]
    6:[1, 6]
    
    Status: Computer is about to make a move. Press Enter to continue...
    >
    ======================================================================
    Stock size: 14
    Computer pieces: 5
    
    [6, 6][4, 6][1, 3]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[0, 1]
    5:[0, 5]
    6:[1, 6]
    
    Status: It's your turn to make a move. Enter your command.
    > -6
    ======================================================================
    Stock size: 14
    Computer pieces: 5
    
    [1, 6][6, 6][4, 6][1, 3]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[0, 1]
    5:[0, 5]
    
    Status: Computer is about to make a move. Press Enter to continue...
    >
    ======================================================================
    Stock size: 13
    Computer pieces: 6
    
    [1, 6][6, 6][4, 6][1, 3]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[0, 1]
    5:[0, 5]
    
    Status: It's your turn to make a move. Enter your command.
    > 0
    ======================================================================
    Stock size: 12
    Computer pieces: 6
    
    [1, 6][6, 6][4, 6][1, 3]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[0, 1]
    5:[0, 5]
    6:[2, 3]
    
    Status: Computer is about to make a move. Press Enter to continue...
    >

**Example 2**
_Invalid input._

    ======================================================================
    Stock size: 14
    Computer pieces: 5
    
    [4, 4][2, 3][3, 4]
    
    Your pieces:
    1:[1, 2]
    2:[2, 6]
    3:[0, 4]
    4:[5, 6]
    5:[2, 5]
    6:[2, 4]
    
    Status: It's your turn to make a move. Enter your command.
    > Hello
    Invalid input. Please try again.
    >

**Example 3**
_Mid-game example. The "domino snake" exceeds six dominoes in length._

    ======================================================================
    Stock size: 7
    Computer pieces: 4
    
    [6, 6][6, 3][3, 0]...[4, 2][2, 3][3, 6]
    
    Your pieces:
    1:[0, 0]
    2:[1, 2]
    3:[5, 5]
    
    Status: It's your turn to make a move. Enter your command.

**Example 4**
_The player wins._

    ======================================================================
    Stock size: 13
    Computer pieces: 2
    
    [3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]
    
    Your pieces:
    1:[4, 4]
    
    Status: It's your turn to make a move. Enter your command.
    > 1
    ======================================================================
    Stock size: 13
    Computer pieces: 2
    
    [3, 5][2, 2][6, 6]...[0, 3][3, 4][4, 4]
    
    Your pieces:
    
    Status: The game is over. You won!
    
---
## Stage 4
### Description
You can't have a game without rules. It's time to introduce them!

Until now, the players were able to place their dominoes however they like. Now, it is considered a violation. According to the rules, the numbers on the ends of the two neighboring dominoes must match each other. This rule can also be described as a set of two requirements:

1.  A player cannot add a domino to the end of the snake if it doesn't contain the matching number.
2.  The orientation of the newly added domino ensures that the matching numbers are neighbors.

For example, consider the following situation:

We have a `[3,4],[4,4],[4,2]` snake and a `[1,2]` domino. The domino cannot be added to the left side of the snake because there is no 3 in `[1,2]`. However, the domino can be added to the right side of the snake because `[1,2]` contains a 2. If we were to place the domino on the right side of the snake, we would have to reorient it: `[3,4],[4,4],[4,2],**[2,1]**`.  
  
These two requirements are strict for both the player and the computer.

### Objectives
Add the following functionality to your code. When it's a player's turn, the program should:
1.  Verify that the move entered by the player is legal (requirement #1).  
    If not, request a new input with the following message: `Illegal move. Please try again.`.
2.  Place dominoes with the correct orientation (requirement #2).

When it's a computer's turn, the program should:
1.  Try random moves until it finds a legal one.  
    > A set of possible moves ranges from `-computer_size` to `computer_size` (where the `computer_size` is the number of dominoes the computer still has). Skipping a turn (move 0) is always legal.
2.  Place dominoes with the correct orientation.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1**
_Invalid move_

    ======================================================================
    Stock size: 14
    Computer pieces: 6
    
    [6, 6]
    
    Your pieces:
    1:[0, 5]
    2:[1, 5]
    3:[2, 4]
    4:[2, 6]
    5:[0, 1]
    6:[1, 6]
    7:[5, 6]
    
    Status: It's your turn to make a move. Enter your command.
    > 5
    Illegal move. Please try again.
    >

**Example 2**
_Valid move (with corrected domino orientation)_

    ======================================================================
    Stock size: 14
    Computer pieces: 6
    
    [6, 6]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[4, 6]
    5:[0, 1]
    6:[0, 5]
    7:[1, 6]
    
    Status: It's your turn to make a move. Enter your command.
    > 7
    ======================================================================
    Stock size: 14
    Computer pieces: 6
    
    [6, 6][6, 1]
    
    Your pieces:
    1:[0, 6]
    2:[5, 5]
    3:[4, 4]
    4:[4, 6]
    5:[0, 1]
    6:[0, 5]
    
    Status: Computer is about to make a move. Press Enter to continue...
    >
    
---
## Stage 5
### Description
Randomly made choices are hardly a sign of intelligence. Teach your computer to make educated decisions with the help of basic statistics. Here's how it works:

The primary objective of the AI is to determine which domino is the least favorable and then get rid of it. To reduce your chances of skipping a turn, you must increase the diversity of your pieces. For example, it's unwise to play your only domino that has a 3, unless there's nothing else that can be done. Using this logic, the AI will evaluate each domino in possession, based on the rarity. Dominoes with rare numbers will get lower scores, while dominoes with common numbers will get higher scores.

The AI should use the following algorithm to calculate the score:
1.  Count the number of 0's, 1's, 2's, etc., in your hand, and in the snake.
2.  Each domino in your hand receives a score equal to the sum of appearances of each of its numbers.

The AI will now attempt to play the domino with the largest score, trying both the left and the right sides of the snake. If the rules prohibit this move, the AI will move down the score list and try another domino. The AI will skip the turn if it runs out of options.

### Objectives
Replace the random move generator with the algorithm described above. Let's analyze how the computer will act in two example situations:

1\. The first case (see Example 1 below).

    Computer pieces: [2,5],[3,5],[0,5]
    Domino snake: [4,4],[4,2],[2,1],[1,0],[0,0],[0,2]

Count:

    0: 5
    1: 2
    2: 4
    3: 1
    4: 3
    5: 3
    6: 0

Scores:

    [2,5]: 4 + 3 = 7
    [3,5]: 1 + 3 = 4
    [0,5]: 5 + 3 = 8

Attempts:  
Domino `[0,5]` has the highest score. However, it cannot be played at this moment.  
Domino `[2,5]` has the second-highest score. We can play it by appending it to the right side of the snake.

The result:  
Play the `[2,5]` domino by appending it to the right side of the snake.


2\. The second case (see example 2 below).

    Computer pieces: [1,5],[3,5],[0,5]
    Domino snake: [4,4],[4,2],[2,1],[1,0],[0,0],[0,2]

Count:

    0: 5
    1: 3
    2: 3
    3: 1
    4: 3
    5: 3
    6: 0

Scores:

    [1,5]: 3 + 3 = 6
    [3,5]: 1 + 3 = 4
    [0,5]: 5 + 3 = 8

Attempts:  
Domino `[0,5]` has the highest score. However, it cannot be played at this moment.  
Domino `[1,5]` has the second-highest score. However, it cannot be played at this moment.  
Domino `[3,5]` is the last option. Unfortunately, it also cannot be played at this moment.

The result:  
Take an extra piece from the stock (if it's not empty) and skip a turn.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1**
_The Computer plays a domino._

    ======================================================================
    Stock size: 12
    Computer pieces: 3
    
    [4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]
    
    Your pieces:
    1:[2, 2]
    2:[3, 3]
    3:[5, 5]
    4:[6, 6]
    5:[4, 5]
    6:[3, 6]
    7:[5, 6]
    
    Status: Computer is about to make a move. Press Enter to continue...
    >
    ======================================================================
    Stock size: 12
    Computer pieces: 2
    
    [4, 4][4, 2][2, 1]...[0, 0][0, 2][2, 5]
    
    Your pieces:
    1:[2, 2]
    2:[3, 3]
    3:[5, 5]
    4:[6, 6]
    5:[4, 5]
    6:[3, 6]
    7:[5, 6]
    
    Status: It's your turn to make a move. Enter your command.
    >

**Example 2**
_The_ _Computer skips the turn._

    ======================================================================
    Stock size: 12
    Computer pieces: 3
    
    [4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]
    
    Your pieces:
    1:[2, 2]
    2:[3, 3]
    3:[5, 5]
    4:[6, 6]
    5:[4, 5]
    6:[3, 6]
    7:[5, 6]
    
    Status: Computer is about to make a move. Press Enter to continue...
    >
    ======================================================================
    Stock size: 11
    Computer pieces: 4
    
    [4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]
    
    Your pieces:
    1:[2, 2]
    2:[3, 3]
    3:[5, 5]
    4:[6, 6]
    5:[4, 5]
    6:[3, 6]
    7:[5, 6]
    
    Status: It's your turn to make a move. Enter your command.
    >