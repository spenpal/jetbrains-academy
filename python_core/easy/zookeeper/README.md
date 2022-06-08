# Zookeeper

## Stage 1
### Description
There are many animals in the zoo, and all of them need care. The animals must be fed, cleaned, surrounded by their kin, and kept happy. That is a difficult task for our large zoo, so one of your employers has suggested a more convenient way to keep track of everything. She wants to be able to pull up a video feed of any animal in the zoo with the help of a program. Being able to check on each habitat would help the zookeepers take care of our furry friends more efficiently!

In this project, you will create a program that helps the zookeepers check on the animals and make sure that they're doing well. Your product will be able to process commands from the zookeepers and display the animals on a monitor.

### Objectives
To begin with, you will develop a simple printer. Your program should display the text from the output example.

### Example
The output:

    I love animals!
    Let's check on the animals...
    The deer looks fine.
    The bat looks happy.
    The lion looks healthy.
    
---
## Stage 2
### Description
One of the most important parts of working with animals is keeping an eye on them. We need to see the animals on the screen to know how they are doing, right? Now we are ready to print something awesome: an image of an animal!

### Objectives
For the second stage, you will need to develop an animal printer. Your program should display the animal identified in the code field.

Please, don't remove the `r` character at the start of the code template. It's a part of the string and it's important. So, the string should start with the `r"""` sequence. This “r” at the beginning stands for “raw” and allows various characters to be used in a string without escaping. For instance, “\\” in a non-raw string should be escaped as follows: “\\\\”.

### Example

Your output should contain the following ASCII image:

    Switching on the camera in the camel habitat...
     ___.-''''-.
    /___  @    |
    ',,,,.     |         _.'''''''._
         '     |        /           \
         |     \    _.-'             \
         |      '.-'                  '-.
         |                               ',
         |                                '',
          ',,-,                           ':;
               ',,| ;,,                 ,' ;;
                  ! ; !'',,,',',,,,'!  ;   ;:
                 : ;  ! !       ! ! ;  ;   :;
                 ; ;   ! !      ! !  ; ;   ;,
                ; ;    ! !     ! !   ; ;
                ; ;    ! !    ! !     ; ;
               ;,,      !,!   !,!     ;,;
               /_I      L_I   L_I     /_I
    Look at that! Our little camel is sunbathing! Our little camel is sunbathing!
    
---
## Stage 3
### Description
The third stage requires you to increase the capabilities of your software. Now it should be able to recognize the number of a specific habitat from the input and show the animals living there.

Add all of the variables from the template to a single variable with the list type. The order of variables matters: they must appear on the list in the order in which they're defined in the code. The list must contain all of the variables with no duplicates.

### Objectives
In this stage your program should:

1.  Ask for the number of the desired habitat using the following phrase: `Please enter the number of the habitat you would like to view:`
2.  Use the input number as an index of your habitats to print its content.
3.  End with the following phrase:

```
---
You've reached the end of the program. To check another habitat, please restart the watcher.
```

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Notice that it's not part of the input.

**Example 1**

    Please enter the number of the habitat you would like to view: > 5

    Switching on the camera in the rabbit habitat...
             ,
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \
    \//\/      .- \
     Y        /    Y
     l       I     !
     ]\      _\    /"\
    (" ~----( ~   Y.  )
    It looks like we will soon have more rabbits!
    ---
    You've reached the end of the program. To check another habitat, please restart the watcher.

**Example 2**

    Please enter the number of the habitat you would like to view: > 4

    Switching on the camera in the bat habitat...
    _________________               _________________
     ~-.              \  |\___/|  /              .-~
         ~-.           \ / o o \ /           .-~
            >           \\  W  //           <
           /             /~---~\             \
          /_            |       |            _\
             ~-.        |       |        .-~
                ;        \     /        i
               /___      /\   /\      ___\
                    ~-. /  \_/  \ .-~
                       V         V
    This bat looks like it's doing fine.
    ---
    You've reached the end of the program. To check another habitat, please restart the watcher.
    
---
## Stage 4
### Description
Now it's time to make our project user-friendly. In this final stage, you'll make your software ready for the zoo staff to use. Your program should understand the habitat numbers, show the animals, and be able to work continuously without having to be restarted.

### Objectives
Your tasks at this point:

1.  Your program should repeat the behavior from the previous stage, but now in a loop.
2.  Do not forget to include an exit opportunity: inputting `exit` should end the program.
3.  When the program is done running, it should print: `See you later!`


### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.
The final version of the program should run like this:

**Example 1**

    Please enter the number of the habitat you would like to view: > 3
    
    Switching on the camera in the goose habitat...
    
                                        _
                                    ,-"" "".
                                  ,'  ____  `.
                                ,'  ,'    `.  `._
       (`.         _..--.._   ,'  ,'        \    \
      (`-.\    .-""        ""'   /          (  d _b
     (`._  `-"" ,._             (            `-(   \
     <_  `     (  <`<            \              `-._\
      <`-       (__< <           :
       (__        (_<_<          ;
        `------------------------------------------
    The goose is staring intently at you... Maybe it's time to change the channel?
    Please enter the number of the habitat you would like to view: > 1
    
    Switching on the camera in the lion habitat...
                                                   ,w.
                                                 ,YWMMw  ,M  ,
                            _.---.._   __..---._.'MMMMMw,wMWmW,
                       _.-""        '''           YP"WMMMMMMMMMb,
                    .-' __.'                   .'     MMMMW^WMMMM;
        _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
     ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
    ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
    WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
    "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
               /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
              /  .'             /  (       .'  /     Ww._     `.  `"
             /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
            (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
    The lion is roaring!
    Please enter the number of the habitat you would like to view: > exit
    See you later!