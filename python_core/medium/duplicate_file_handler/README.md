# Duplicate File Handler

## Stage 1
### Theory
Let's get straight to the point. For our task, we need the `os.walk` method. The Tutorial's Point [guide](https://www.tutorialspoint.com/python3/os_walk.htm) can shed some light on how to use it.

### Description
A computer is a great thing. It helps us store and manage tons of information. Every user knows how to work with folders. In this step, we will learn how to get a list of files and folders within a specific directory.

### Objectives
In this stage, your program should:

1.  Accept a command-line argument that is a root directory with files and folders. Print `Directory is not specified` if there is no command-line argument;
2.  Iterate over folders and print file names with their paths. The direction of the slashes in the printed out paths do not matter. Tests are platform independent, so different style of slashes ("/" or "\\") are valid.

### Example
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:**

Suppose, you have the following set of files and folders:

    +---[root_folder]
        |
        +---wall.png
        +---pass.txt
        +---[docs]
        |   |
        |   +---project.py
        |   +---calc.xls
        |   +---tutorial.mp4
        |   +---[res]
        |       |
        |       +---data.json
        |   +---[output]
        |       |
        |       +---result.json
        +---[masterpiece]
            |
            +---rick_astley_never_gonna_give_you_up.mp3

Program output:

    > python handler.py root_folder
    
    root_folder/wall.png
    root_folder/pass.txt
    root_folder/docs/project.py
    root_folder/docs/calc.xls
    root_folder/docs/tutorial.mp4
    root_folder/docs/res/data.json
    root_folder/docs/output/result.json
    root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
    
---
## Stage 2
### Description
In this stage, we start by identifying files of the same size in bytes. The `os.path` module allows you to get access to file extension and size. The [Official Documentation](https://docs.python.org/3/library/os.path.html#module-os.path) can help you with that.

Of course, we cannot be absolutely sure that files of the same size and format are duplicates. This will help us, however, narrow down the search. It is also important to keep track of the scanned files. Add an ability to search for files of a specific file format and then sort the found files by size.

Hint: Use dictionaries with size as keys and a list of full paths as each key's value.

### Objectives
Keep the functionality from the previous stage. To complete this stage, your program should:

1.  Accept a command-line argument that is a root directory with files and folders. Print `Directory is not specified` if there is no command-line argument;
2.  Read user input that specifies the file format (see examples). Empty input should match any file format;
3.  Print a menu with two sorting options: `Descending` and `Ascending`. They both represent the respective order by size of groups of files. Read the input. Print `Wrong option` if any other input is entered. Repeat until a correct input is provided;
4.  Iterate over folders and print the information about files of the same size: their size, path, and names.

Please note: you should use full path to file **from root directory** when printing or reading.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:**
Suppose, you have the following set of files and folders:

    +---[root_folder]
        +---gordon_ramsay_chicken_breast.avi /4590560 bytes
        +---[audio]
        |   |
        |   +---voice.mp3 /2319746 bytes
        |   +---sia_snowman.mp3 /4590560 bytes
        |   +---nea_some_say.mp3 /3232056 bytes
        |   +---[classic]
        |   |   |
        |   |   +---unknown.mp3 /3422208 bytes
        |   |   +---vivaldi_four_seasons_winter.mp3 /9158144 bytes
        |   |   +---chopin_waltz7_op64_no2.mp3 /9765504 bytes
        |   +---[rock]
        |       |
        |       +---smells_like_teen_spirit.mp3 /4590560 bytes
        |       +---numb.mp3 /5786312 bytes
        +---[masterpiece]
            |
            +---rick_astley_never_gonna_give_you_up.mp3 /3422208 bytes

Program output:

    > python handler.py root_folder

    Enter file format:
    >mp3
    
    Size sorting options:
    1. Descending
    2. Ascending
    
    Enter a sorting option:
    > 3
    
    Wrong option
    
    Enter a sorting option:
    > 2
    
    3422208 bytes
    root_folder/audio/classic/unknown.mp3
    root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
    
    4590560 bytes
    root_folder/audio/rock/smells_like_teen_spirit.mp3
    root_folder/audio/sia_snowman.mp3
    
---
## Stage 3
### Theory
Now we have a list of files of the same size. The next step is to check the files with the help of the [Hashlib module](https://docs.python.org/3/library/hashlib.html). Why do we need to use hash here? The answer is very simple — it's convenient! As you may know, a hash function can take **any** input of **any length**. It produces several strings as output.

A hash function has the following main features:

*   easy to compute
*   unique output
*   small and fixable output

So, a file type or size plays a minor role. We can get a hash of any file and compare it against a hash of another file.  
We will work with an MD5 hash function of the [Hashlib module](https://docs.python.org/3/library/hashlib.html). Take a look at some useful functions:

*   `md5()` creates a hash object
*   `update()` updates a hash object
*   `hexdigest()` gets the HEX digest

### Description
In this stage, we need to get hashes of files of the same size and check whether they are the same file. Remember that **hash works with byte-like objects only**, so pay attention to the file read mode (the `rb` mode).

### Objectives
Keep the functionality from the previous stages. To complete the stage, your program should:

1.  Ask for duplicates check;
2.  Read user input: `yes` or `no` . Print `Wrong option` if any other input is received. Repeat until a user provides a valid answer. If the input is `yes`, get the hash of files of the same size; group the files of the same hash, assign numbers to these files. Otherwise, the program should stop the operation;
3.  Assign numbers to lines with files after hashing. You should assign numbers to files based on the total number of files in output. It is needed for the purpose of the next stage.
4.  Print the information about the duplicate files along with their hashes (see example). Sort the group of files by size as in the previous stage. You don't have to sort hash subgroups.

Please note: you should use full path to file **from root directory** when printing or reading.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

Suppose you have the following set of files and folders:

    +---[root_folder]
        +---gordon_ramsay_chicken_breast.avi /4590560 bytes
        +---poker_face.mp3 /5550640 bytes
        +---poker_face_copy.mp3 /5550640 bytes
        +---[audio]
        |   |
        |   +---voice.mp3 /2319746 bytes
        |   +---sia_snowman.mp3 /4590560 bytes
        |   +---nea_some_say.mp3 /3232056 bytes
        |   +---[classic]
        |   |   |
        |   |   +---unknown.mp3 /3422208 bytes
        |   |   +---vivaldi_four_seasons_winter.mp3 /9158144 bytes
        |   |   +---chopin_waltz7_op64_no2.mp3 /9765504 bytes
        |   +---[rock]
        |       |
        |       +---smells_like_teen_spirit.mp3 /4590560 bytes
        |       +---numb.mp3 /5786312 bytes
        +---[masterpiece]
            |
            +---rick_astley_never_gonna_give_you_up.mp3 /3422208 bytes
            +---the_magic_flute_queen_of_the_night_aria.mp3 /3422208 bytes
            +---the_magic_flute_queen_of_the_night_aria_copy.mp3 /3422208 bytes

Program output:

    > python handler.py root_folder
    
    Enter file format:
    >
    
    Size sorting options:
    1. Descending
    2. Ascending
    
    Enter a sorting option:
    > 1
    
    5550640 bytes
    root_folder/poker_face.mp3
    root_folder/poker_face_copy.mp3
    
    4590560 bytes
    root_folder/gordon_ramsay_chicken_breast.avi
    root_folder/audio/sia_snowman.mp3
    root_folder/audio/rock/smells_like_teen_spirit.mp3
    
    3422208 bytes
    root_folder/audio/classic/unknown.mp3
    root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
    root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria.mp3
    root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria_copy.mp3
    
    Check for duplicates?
    > yes
    
    5550640 bytes
    Hash: 909ba4ad2bda46b10aac3c5b7f01abd5
    1. root_folder/poker_face.mp3
    2. root_folder/poker_face_copy.mp3
    
    3422208 bytes
    Hash: a7f5f35426b927411fc9231b56382173
    3. root_folder/audio/classic/unknown.mp3
    4. root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
    Hash: b6d767d2f8ed5d21a44b0e5886680cb9
    5. root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria.mp3
    6. root_folder/masterpiece/the_magic_flute_queen_of_the_night_aria_copy.mp3
    
---
## Stage 4
### Description
During previous stages, we have created a program that can find file duplicates. In this stage, we need to add the ability to delete files and print the information about them.

### Objectives
Keep the functionality from the previous stages. To complete this stage, your program should do the following:

1.  Ask a user whether they want to delete files. Expect either `yes` or `no` as the answer. Print `Wrong option` if it receives any other input. Repeat until a user provides a valid answer. If `yes`, read what files a user wants to delete and then delete them. Otherwise, abort the program;
2.  Read a sequence of files that a user wants to delete and then delete them. Input should contain only file numbers separated by spaces. Print `Wrong format` if it receives empty string or any other input. Repeat until a user provides a valid answer;
3.  Print the total freed up space in bytes.

Please note: you should use full path to file **from root directory** when printing or reading.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:**
Suppose, you have the following set of files and folders:

    +---[root_folder]
        +---gordon_ramsay_chicken_breast.avi /4590560 bytes
        +---poker_face.mp3 /5550640 bytes
        +---poker_face_copy.mp3 /5550640 bytes
        +---[audio]
        |   |
        |   +---voice.mp3 /2319746 bytes
        |   +---sia_snowman.mp3 /4590560 bytes
        |   +---nea_some_say.mp3 /3232056 bytes
        |   +---[classic]
        |   |   |
        |   |   +---unknown.mp3 /3422208 bytes
        |   |   +---vivaldi_four_seasons_winter.mp3 /9158144 bytes
        |   |   +---chopin_waltz7_op64_no2.mp3 /9765504 bytes
        |   +---[rock]
        |       |
        |       +---smells_like_teen_spirit.mp3 /4590560 bytes
        |       +---numb.mp3 /5786312 bytes
        +---[masterpiece]
            |
            +---rick_astley_never_gonna_give_you_up.mp3 /3422208 bytes

Program output:

    > python handler.py root_folder
    
    Enter file format:
    >
    
    Size sorting options:
    1. Descending
    2. Ascending
    
    Enter a sorting option:
    > 1
    
    5550640 bytes
    root_folder/poker_face.mp3
    root_folder/poker_face_copy.mp3
    
    4590560 bytes
    root_folder/gordon_ramsay_chicken_breast.avi
    root_folder/audio/sia_snowman.mp3
    root_folder/audio/rock/smells_like_teen_spirit.mp3
    
    3422208 bytes
    root_folder/audio/classic/unknown.mp3
    root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
    
    Check for duplicates?
    > yes
    
    5550640 bytes
    Hash: 909ba4ad2bda46b10aac3c5b7f01abd5
    1. root_folder/poker_face.mp3
    2. root_folder/poker_face_copy.mp3
    
    3422208 bytes
    Hash: a7f5f35426b927411fc9231b56382173
    3. root_folder/audio/classic/unknown.mp3
    4. root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
    
    Delete files?
    > yes
    
    Enter file numbers to delete:
    > 1 2 5
    
    Wrong format
    
    Enter file numbers to delete:
    > 1 2 4
    
    Total freed up space: 14523488 bytes