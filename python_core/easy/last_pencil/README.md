# Last Pencil

## Stage 1
### Description
You and your friend decided to play a simple pen-and-paper game. There's one catch — you have only pencils but no paper; the last piece of paper is gone for your beautiful drawings. As a joke, your friend pulls all the pencils out of the case onto the table and says: "Your turn!"

### Objectives
In this stage, your program should print one phrase to the console output. The `print()` function seems to be very useful for this. Your program should print one line with several vertical bar symbols representing pencils and one `Your turn` substring.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:**

    ||||||||
    Your turn! 

**Example 2:**

    |||
    Your turn:
    
---
## Stage 2
### Description
Your friend's suggestion surprised you a little bit. After a couple of "No, you" retaliations, you decided that it would be more convenient to input the initial conditions to determine who goes first, and how many pencils there are on the table.

### Objectives
Write a program that will satisfy the conditions below:

1.  Ask users to input the number of pencils with the `How many pencils` substring. Don't forget to read that number;
2.  Ask users to input who goes first from the two players provided beforehand. To do it, output a substring in the following format: `Who will be the first (*Name1*, *Name2*)`. Don't forget to read that name.
3.  Print two lines: one with the number of pencils, the other with the `*NameX* is going first` substrings

You don't need to input players' names, just change the `*Name1*` and `*Name2*` substrings. Names can consist of the letters of the English alphabet and numbers only.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:**

    How many pencils would you like to use:
    > 5
    Who will be the first (John, Jack):
    > John
    |||||
    John is going first!

**Example 2:**

    How many pencils would you like to use:
    > 20
    Who will be the first (John, Jack):
    > Jack
    ||||||||||||||||||||
    Jack is going first!
    
---
## Stage 3
### Description
An interesting idea has come to your mind. Let's change the rules of game. Players take turns taking `X` pencils until none of them remain.

### Objectives
Expand your program by creating a loop. Each player takes turns removing pencils until 0 pencils remain on the table. Each iteration prints 2 lines: lines with pencils (vertical bars) and whose turn is now by printing the `*NameX*'s turn` substring.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:**

    How many pencils would you like to use:
    > 5
    Who will be the first (John, Jack):
    > John
    |||||
    John's turn:
    > 2
    |||
    Jack's turn:
    > 1
    ||
    John's turn:
    > 2

**Example 2:**

    How many pencils would you like to use:
    > 15
    Who will be the first (John, Jack):
    > John
    |||||||||||||||
    John's turn:
    > 8
    |||||||
    Jack's turn:
    > 7
    
---
## Stage 4
### Description
The game was interesting, but it went sour. No one was playing a fair game! You've taken 10 pencils, your friend decided that it is unfair and somehow took a negative number! Moreover, you both can't decide which of you won. Maybe, it's time to add new rules to the game?

### Objectives
In this stage, your task is to add a new level of control over the game. Check the input. If it's incorrect, print the reason why. Also, limit the possible amount of pencils taken. Let's say that players can remove not more than 3 pencils at a time.

Here are possible errors and their feedback:

1.  The initial number of pencils is not a numeric string, so it can't be converted to an integer — `The number of pencils should be numeric`;
2.  The initial number of pencils is equal to `0` _—_ `The number of pencils should be positive`;
3.  If the input is a negative amount, apply condition (1), as the minus sign is not a numeric;
4.  If the chosen first player is not `*Name1*` or `*Name2*` — `Choose between *Name1* and *Name2*`;
5.  One of the players has taken the number of pencils that differs from `1`, `2`, or `3` — `Possible values: '1', '2' or '3'`;
6.  One of the players has taken more pencils than there are on the table — `Too many pencils were taken`.

If one of the errors occurs, ask for input once again.

Don't forget to help determine the winner of the game. The player who takes the last pencil loses the game. Print out the result at the end of the game with the line `*Winner-name* won!`

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:**

    How many pencils would you like to use:
    > a
    The number of pencils should be numeric
    > 5
    Who will be the first (John, Jack):
    ...

**Example 2:**

    How many pencils would you like to use:
    > 0
    The number of pencils should be positive
    > 20
    Who will be the first (John, Jack):
    ...

**Example 3:**

    How many pencils would you like to use:
    > 5
    Who will be the first (John, Jack):
    > JohnJack
    Choose between 'John' and 'Jack'
    > John
    |||||
    John's turn!
    ...

**Example 4:**

    HHow many pencils would you like to use:
    > 5
    Who will be the first (John, Jack):
    > John
    |||||
    John's turn!
    > 4
    Possible values: '1', '2' or '3'
    > 1
    ||||
    Jack's turn!
    ...

**Example 5:**

    How many pencils would you like to use:
    > 5
    Who will be the first (John, Jack):
    > John
    |||||
    John's turn!
    > a
    Possible values: '1', '2' or '3'
    > 1
    ||||
    Jack's turn!
    ...

**Example 6:**

    How many pencils would you like to use:
    > 5
    Who will be the first (John, Jack):
    > John
    |||||
    John's turn!
    > 3
    ||
    Jack's turn!
    > 3
    Too many pencils were taken
    > 2
    John won!
    
---
## Stage 5
### Description
You've played a couple of games with your friend. After a while, you both found out that if there are 2, 3, or 4 pencils left on the table, you automatically win. It happens because a player can take 1, 2, or 3 pencils and leave the other player with only one. The other player has nothing left but to take the last pencil and lose the game.

On the other hand, if you have 5 pencils on the table, you lose. It will again lead to the situation described above but vice-versa.

The same thing happens when there are 6, 7, or 8 pencils left on the table. It will eventually repeat all over again.

It's easier to get a grasp of it with a line of 10 red-green pencils. In this example, we can be sure that if both players know the winning strategy, the first one will be the winner. Here is a game process:

**`||||||||||`**

The first player has an advantage and takes 1 pencil:

**`|||||||||`**

The second player has a disadvantage, so if the second player takes any number of pencils from 1 to 3, the first player is left with a winning strategy:

*   1: **`||||||||`**
*   2: **`|||||||`**
*   3: **`||||||`**

The first player stands in a winning position and takes that number. It will lead to a losing position for the second player:

**`|||||`**

The second player stands in a losing position — if the second player takes any number of pencils from 1 to 3, the first player will be left in a winning position:

*   1: **`||||`**
*   2: **`|||`**
*   3: **`||`**

The first player stands in a winning position and takes the right number of pencils. It leaves the second player with one pencil:

**`|`**

Your friend came up with the idea of creating a bot for the game a bit more replayable. Instead of taking input from two players, you need to program a bot that follows a winning strategy. If the bot's position isn't the winning one, you can program it to take any number of pencils (1, 2, or 3) at random. You can also come up with any pattern of your own for the losing position.

### Objectives
Implement the bot for the second player. For example, `(Who will be the first (John, Jack)`. In this case, `John` is the user, and `Jack` is the bot. So, if the player chooses Jack as the first player, after that input, there should be printed bot's move.

Your final objective is to expand your program. Write a solution, that can be executed for any initial number of pencils. Check each iteration whose turn is now. If it is the bot, instead of requiring input from the second player, output one line that contains the bot's move (`1`, `2` or `3`) that follows the winning strategy. If the bot is not in the winning position, make it follow any pattern of your liking, as the tests check only the bot's winning position.

### Examples
**Example 1:**

    How many pencils would you like to use:
    > 10
    Who will be the first (John, Jack):
    > Jack
    ||||||||||
    Jack's turn:
    1
    |||||||||
    John's turn!
    > 2
    |||||||
    Jack's turn:
    2
    |||||
    John's turn!
    > 1
    ||||
    Jack's turn:
    3
    |
    John's turn!
    > 1
    Jack won!

**Example 2:**

    How many pencils would you like to use:
    > 6
    Who will be the first (John, Jack):
    > John
    ||||||
    John's turn!
    > 1
    |||||
    Jack's turn:
    2
    |||
    John's turn!
    > 2
    |
    Jack's turn:
    1
    John won!