# Create Glowing Bacteria

## Stage 1
### Description
To give the bacteria new properties, we have to start by modifying the plasmid.

Typically, a bacterial plasmid looks like a huge four-letter text (A, T, C, G). It has a header denoted by the symbol ">", in which you can find a description of the organism and key information about the sequence. Everything else is the sequence itself.

    >MK753227.1 Escherichia coli str. K-12, partial sequence
    GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTGTGCACTACCTCCTT
    GGTTGTCTATGCTATGCTGATCTACAACTGGCATGCGGTCAGTGCGTCCTGCTGATGTGCTCAGTATCTC
    TATCACTGATAGGGATGTCAATCTCTATCACTGATAGGGAAACGTTTCGCAGAAGCTTCCGCAAGGTACC
    ...

Now you are looking at a sequence of a bacterial plasmid. Alas, it's just a single **strand** (single DNA chain). Before modification, we need to create a second complementary strand. To get it, replace each element of the original sequence with its opposite according to the **complementarity principle**:

Adenine (A) <-> Thymine (T);  
Cytosine (C) <-> Guanine (G).

For instance, if the sequence is TTAGCGCA your answer should be AATCGCGT.

![](https://ucarecdn.com/c2ac2217-a1b1-4d08-a3c8-e484346274a3/)

### Objectives
At this stage, you will create the complementary plasmid strand. Use only the first line of the plasmid sequence above. It looks as follows:

    GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTGTGCACTACCTCCTT

1.  Input the sequence of the original strand;
2.  Print the complementary strand as an answer.

Advice: you may write a function that automates this action. It will be useful in the following stages. In your output, print only the sequence of the complementary plasmid strand.

##### Example
The greater-than symbol followed by a space (> ) represents the console input.

    > TTAGCGCA
    AATCGCGT # the output starts here
    
---
## Stage 2
### Description
In the previous stage, we obtained a double-strand bacterial plasmid. Now, you need to cut it at a certain place to make a gap. This particular place is called a **restriction site**. In nature, the cutting is provided by special enzymes called **restrictases**. They are like scissors. After cutting, **sticky ends** are formed. To get the sticky ends means to make a "diagonal" cut at the restriction site.

An example of a cut is shown below:

![](https://ucarecdn.com/3d1e9c73-09a6-41b9-8ecc-72f7b7241dc6/)  
  
More information about the mechanisms of cutting and restriction enzymes can be found in the [article](https://microbenotes.com/restriction-enzyme-restriction-endonuclease/) by Microbe Notes.

### Objectives
Use the double-stranded plasmid sequence from the first step and cut it at the site with the `CTGCAG` sequence between the 1st and 2nd nucleotides (letters) in the initial strand and between 5th and 6th nucleotides in the complementary one. So, your sequence for cutting is as follows:  
_original and complementary strands are separated by a space_

    GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTTATTTGTATAGTTCA CTGCAGACACGTTCATGATGACAAGACGTCAGTGAACTTAAGCTATGGGTCGACAATAAACATATCAAGT

To complete this stage you should:

1.  Input the original and the complementary strands separated by a space;
2.  Find the restriction site in the plasmid sequence;
3.  Cut the first DNA strand according to the first restriction site (between the first two nucleotides, which are `C` and `T`);
4.  Translate the original restriction site into a complementary one;
5.  In the complementary strand, find the complementary site and cut between the last two nucleotides to obtain the protruding ends;
6.  Print the two cut DNA strands.

In your answer, include the sequences of both strands and mark the place of the cut with a single space. Place each strand on a separate line. Use capital letters only.

### Example
The greater-than symbol followed by a space (> ) represents the console input.

**Example 1:** _The resulting cut along the_ `CTGCAG` _restriction site_

    > TGACTGCAGTTAG ACTGACGTCAATC
    TGAC TGCAGTTAG  # the output starts here
    ACTGACGT CAATC

---
## Stage 3
### Description
To make a bacterium glow, the **green fluorescent protein** (GFP) gene must be inserted into the bacterial plasmid. To combine the GFP gene with the plasmid, you need to get the sticky ends. Now, you need to obtain the complementary strand of the GFP gene. The algorithm is the same as for a plasmid.

##### Objectives
At this stage, you need to get the double-stranded GFP gene. You already know how to get a complementary strand. Now, use your knowledge to compose a function that automates this action.

Your program should:

1.  Input a sequence of an original strand;
2.  Create a complementary strand;
3.  Print the original and complementary strands, separated by a newline character (`\n`).

##### Examples
The greater-than symbol followed by a space (> ) represents the console input.

**Example 1:**

    > CTAGAGGATCCCCG
    CTAGAGGATCCCCG  # the output starts from this line
    GATCTCCTAGGGGC

**Example 2:**

    > ATGAAACAGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTA
    ATGAAACAGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTA  # the output starts from this line
    TACTTTGTCGTACTGAAAAAGTTCTCACGGTACGGGCTTCCAATACAT
    
---
## Stage 4
### Description
You have a double-stranded GFP sequence, excellent!

Now we need to prepare the GFP to be able to insert it into the plasmid. In order to insert GFP into the plasmid, we need to make sticky ends. The insertion occurs as follows:

![](https://ucarecdn.com/a8b60d3e-be08-4028-ae0e-a6de142433a0/)

We have already done step 1, and now we are at step 2. We need to cut the GFP sequence on both sides so that its ends fit the cut on the plasmid. If their cuts fit together, then we can insert the sequence into the plasmid in the next steps.

Unlike plasmid, GFP has two sticky ends on the left and right sides, `TGCA` and `ACGT` respectively, because the **insertion** occurs in the middle of a plasmid gap.

To visualize the process of restriction, you can watch the [video](https://www.youtube.com/watch?v=GJrAsW41a64&ab_channel=NicoleLantz) on YouTube by Nicole Lantz.

Now, you need to obtain GFP with sticky ends. For GFP, the best restriction site is `CTGCAG` from the left and `GTGCAC` from the right. Use them to avoid losing significant coding parts of the GFP gene. The positions are marked below:

    GCATGC_CTGCAG_GTCGACTCTAGAGGATCCCCGGGTACCTAGAATTAAAGAGGAGAAATTAAGCATGCGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCGGTTATGGTGTTCAATGCTTTGCGAGATACCCAGATCATATGAAACAGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAAAGGCCTGCAGCAAACGACGAAAACTACGCTTTAGTAGCTTAATAAGCTTAATTAGCTGACCTACTAGTCGGCCGTCTCGACATGAACGCAGGAAAGAACATGTGAGCAAAAGGCCAGCAAAAGGCCAGGAACCGTAAAAAGGCCGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGCTCAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCGTGCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGCGCTTTCTCAATGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTGGGCTGT_GTGCAC_GAACCCCCCGT

In your case, there will be no `_` character in the original sequence. Don't create your code around it.

If there are multiple restriction sites in the GFP sequence, always use the sites closest to the edges of the GFP sequence. This action will avoid cutting the functional part of the GFP gene and losing its functionality.

### Objectives
1.  Input the original GFP gene sequence and restriction sites from the console to cut GFP;
2.  To automate the action of getting the sticky ends in the GFP plasmid, we recommend implementing a function that will:
    *   Create complementary sequences for the GFP gene and for the restriction sites;
    *   Find the restriction site CTGCAG at the beginning of the sequence, and cut both strands: the original one between 1st and 2nd nucleotides, and the complementary one between 5th and 6th nucleotides. As a result of this step, we will get a protruding sticky end on the original GFP chain;
    *   Find the GTGCAC restriction site at the end of the sequence, and cut through it similarly to the previous point;
    *   Return the resulting GFP chains.
3.  As a result, print the double-strand GFP sequence with sticky ends. The original and complementary strands should be separated by a newline character (`\n`).

### Example
The greater-than symbol followed by a space (`>` ) represents the console input.

**Example 1:** _input of the original strand and the restriction sites_

    > CCTGCAGGTCGACTCTAGAGGATCCCCGGGTACCTAGAATTGCACGCA
    > CTGCAG TTGCAC
    TGCAGGTCGACTCTAGAGGATCCCCGGGTACCTAGAAT  # the output starts here
    CCAGCTGAGATCTCCTAGGGGCCCATGGATCTTAACGT
    
---
## Stage 5
### Description
You have the plasmid, and you have the GFP gene... Boom! The **ligation** has begun.  
Ligation is the process of gluing the complementary sticky ends together. It's time to insert the GFP with the sticky ends into the gap in the plasmid.

### Objective
Compose the function that performs the ligation. It should get the sequence of the plasmid with the sticky ends and the sequence of the GFP gene (with the sticky ends as well) from the file. Each GFP sticky end is complementary to the appropriate plasmid end. The function "stitches" the GFP and plasmid together by gluing the sticky ends.

To better understand the process take a look at the picture below:

![](https://ucarecdn.com/2b67207d-73f5-41c5-9bbe-58203815dfb5/)

The original plasmid strand is marked in black, the complementary plasmid strand in blue, the original GFP strand in green, and the complementary GFP strand in purple.

To complete the stage, your program should:

1.  Take _the file's name_ as input from the console and parse its contents;
2.  Perform the ligation by gluing each complementary plasmid end with the complementary GFP end. At this step, we recommend that you implement a function that returns the double-stranded ligation result so you can reuse it in the last stage;
3.  Print the double-stranded ligation result. Separate two sequences with a newline character (`\n`).

Additionally, we would like you to familiarize an input file structure:

*   The first line contains four parts: the first two are the original plasmid strand (the second part has the sticky end), and the last two belong to the complementary plasmid strand (the first part with the sticky end).
*   The second line contains two parts. The first part is the original GFP strand (sticky end on the left), and the last part is the complementary strand (sticky end on the right).

You have an example file [example.txt](https://stepik.org/media/attachments/lesson/560993/example.txt). Use it to test that your program takes _a file name_ as input and processes it correctly.

### Example
The greater-than symbol followed by a space (`>` ) represents the console input.

**Example 1:**
_example1.txt file content_

    ATCGTTCGTGTGCATGT TGCATCTGTATCTAGCGC TAGCAAGCACACGTACAACGT AGACATAGATCGCG
    TGCAXXXXXXXXXXXXX XXXXXXXXXXXXXACGT

_The output of your program_

    > example1.txt
    ATCGTTCGTGTGCATGTTGCAXXXXXXXXXXXXXTGCATCTGTATCTAGCGC
    TAGCAAGCACACGTACAACGTXXXXXXXXXXXXXACGTAGACATAGATCGCG
    
---
## Stage 6
### Description
Good job! You're almost at the finish line. We guess you're a little tired of doing every step by hand. Let's write a program that will modify the bacteria itself from the moment the data are received until all sequences are glued together.

### Objective
Write code that takes the file's name as input and automatically processes the data. The file content you can find below.  
Your code should create complementary strands for plasmid and GFP sequences, cut them according to restriction sites, and ligate the sticky parts together. The result should be a double-stranded modified plasmid with a GFP insertion. Do not forget to print it!

If there are multiple restriction sites in the GFP sequence, use the sites closest to the edges of the GFP sequence. This action will avoid cutting the functional part of the GFP gene and losing its functionality.

The input file content:

1.  The original plasmid strand;
2.  The restriction site for cutting the plasmid;
3.  The GFP original strand;
4.  Two left and right restriction sites for GFP cutting.

You have an example file [plasmid\_gfp\_example.txt](https://stepik.org/media/attachments/lesson/560993/plasmid_gfp_example.txt). Use it to test that your program takes _a file name_ as input and processes it correctly.

### Example
The greater-than symbol followed by a space (`>` ) represents the console input.

**Example 1:**
_example1.txt file content_

    ATGTGCTAGCTGATGCAAGGTATCGCATGCTAGCTAGCTAGCGATC
    AAGGTA
    GCATGCCTGCAGGTCGACTCTAGAGGATCCCCGGGTACCTAGAATTAAAGAGGAGAAATTAAGCATGCGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCGGTTATGGTGTTCAATGCTTTGCGAGATACCCAGATCATATGAAACAGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAAAGGCCTGCAGCAAACGACGAAAACTACGCTTTAGTAGCTTAATAAGCTTAATTAGCTGACCTACTAGTCGGCCGTCTCGACATGAACGCAGGAAAGAACATGTGAGCAAAAGGCCAGCAAAAGGCCAGGAACCGTAAAAAGGCCGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGCTCAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCGTGCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGCGCTTTCTCAATGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTGGGCTGTGTGCACGAACCCCCCGT
    CAGGTC TAGGTC

_The output of your program_

    > example1.txt
    ATGTGCTAGCTGATGCAAGGTCGACTCTAGAGGATCCCCGGGTACCTAGAATTAAAGAGGAGAAATTAAGCATGCGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCGGTTATGGTGTTCAATGCTTTGCGAGATACCCAGATCATATGAAACAGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAAAGGCCTGCAGCAAACGACGAAAACTACGCTTTAGTAGCTTAATAAGCTTAATTAGCTGACCTACTAGTCGGCCGTCTCGACATGAACGCAGGAAAGAACATGTGAGCAAAAGGCCAGCAAAAGGCCAGGAACCGTAAAAAGGCCGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGCTCAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCGTGCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGCGCTTTCTCAATGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTATCGCATGCTAGCTAGCTAGCGATC
    TACACGATCGACTACGTTCCAGCTGAGATCTCCTAGGGGCCCATGGATCTTAATTTCTCCTCTTTAATTCGTACGCATTTCCTCTTCTTGAAAAGTGACCTCAACAGGGTTAAGAACAACTTAATCTACCACTACAATTACCCGTGTTTAAAGACAGTCACCTCTCCCACTTCCACTACGTTGTATGCCTTTTGAATGGGAATTTAAATAAACGTGATGACCTTTTGATGGACAAGGTACCGGTTGTGAACAGTGATGAAAGCCAATACCACAAGTTACGAAACGCTCTATGGGTCTAGTATACTTTGTCGTACTGAAAAAGTTCTCACGGTACGGGCTTCCAATACATGTCCTTTCTTGATATAAAAAGTTTCTACTGCCCTTGATGTTCTGTGCACGACTTCAGTTCAAACTTCCACTATGGGAACAATTATCTTAGCTCAATTTTCCATAACTAAAATTTCTTCTACCTTTGTAAGAACCTGTGTTTAACCTTATGTTGATATTGAGTGTGTTACATATGTAGTACCGTCTGTTTGTTTTCTTACCTTAGTTTCAATTGAAGTTTTAATCTGTGTTGTAACTTCTACCTTCGCAAGTTGATCGTCTGGTAATAGTTGTTTTATGAGGTTAACCGCTACCGGGACAGGAAAATGGTCTGTTGGTAATGGACAGGTGTGTTAGACGGGAAAGCTTTCTAGGGTTGCTTTTCTCTCTGGTGTACCAGGAAGAACTCAAACATTGTCGACGACCCTAATGTGTACCGTACCTACTTGATATGTTTTCCGGACGTCGTTTGCTGCTTTTGATGCGAAATCATCGAATTATTCGAATTAATCGACTGGATGATCAGCCGGCAGAGCTGTACTTGCGTCCTTTCTTGTACACTCGTTTTCCGGTCGTTTTCCGGTCCTTGGCATTTTTCCGGCGCAACGACCGCAAAAAGGTATCCGAGGCGGGGGGACTGCTCGTAGTGTTTTTAGCTGCGAGTTCAGTCTCCACCGCTTTGGGCTGTCCTGATATTTCTATGGTCCGCAAAGGGGGACCTTCGAGGGAGCACGCGAGAGGACAAGGCTGGGACGGCGAATGGCCTATGGACAGGCGGAAAGAGGGAAGCCCTTCGCACCGCGAAAGAGTTACGAGTGCGACATCCATAGAGTCAAGCCACATCCATAGCGTACGATCGATCGATCGCTAG