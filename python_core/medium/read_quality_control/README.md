# Read Quality Control

## Stage 1
### Description
We see the enthusiasm in your eyes. Let's get started to dig into bioinformatics data!

Bioinformaticians obtain the data from a device called the **sequencer**. A sequencer is a magic machine that can transform genetic material into text. For instance, you can transform your DNA into a set of letters — **A**, **T**, **C**, and **G**. In this project, we will work with bacterial DNA data sequencing.

The first data type you need to deal with is lightly-processed sequencing data from the [Illumina](https://www.youtube.com/watch?v=fCd6B5HRaZ8&ab_channel=Illumina) sequencer. Such data is stored in text files of the FASTQ format.

A FASTQ file includes four-line parts and looks like a huge text file. To get things straight, let's take a look at one four-line part of a FASTQ file. This part is called a **read:**

![](https://ucarecdn.com/66a4939f-0a55-4ed8-a3d4-9997b8fd8dd6/)

The first line collects information about the instrument ID, run number, flowcell ID, lane, tile, x-pos (the X-coordinate of a cluster), y-pos, UMI, read number, filtering status, control number, and index of the read. The second line is the sequence constructed from **nucleotides** (letters `A`, `T`, `C`, and `G`). The third line starts with a `+` presenting the same data as the first line or can store additional information about the read. Finally, the last line shows information about the quality of each nucleotide in a special format. If you feel curious, [this Wikipedia article](https://en.wikipedia.org/wiki/FASTQ_format) can help you delve deeper.

### Objectives
*   Take the input path to the FASTQ file with data;
*   Open the file and print all the information relevant only to the first read (see the Example section for the output format).

### Example
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _contents of the test.fastq file_

    @SRR16506265.1071862 1071862 length=76
    CGCTGGGTCTGTCGCTGGTCACCCTGTTGTTTATGACTACCGCCCTGCTGGGCTGGTACTACGTTTTGCCGTTCGT
    +SRR16506265.1071862 1071862 length=76
    C9CCC>CGEG9ECEDFGGEFCD@8FGFGGGCGEEGFFGFFCFGGGGGFFGGGCDGGDG9F998FF@EECF@C:FGF
    @SRR16506265.1071863 1071863 length=76
    GTGTGGGCCAGCGTCATATCAACCTGTGACGCCCCCAAATCACCAAAACGGAATACACGCACTGGCTGCCAGCGTT
    +SRR16506265.1071863 1071863 length=76
    CCCC@--CF;-@:FC@EAFFFGGGGGGGGGGGEEFGGGGGGGGFGGGGGGEGGFGGGGGGGGGFGGGGGGGGFGFD

_Program output_

    > test.fastq
    @SRR16506265.1071862 1071862 length=76
    CGCTGGGTCTGTCGCTGGTCACCCTGTTGTTTATGACTACCGCCCTGCTGGGCTGGTACTACGTTTTGCCGTTCGT
    +SRR16506265.1071862 1071862 length=76
    C9CCC>CGEG9ECEDFGGEFCD@8FGFGGGCGEEGFFGFFCFGGGGGFFGGGCDGGDG9F998FF@EECF@C:FGF

---

## Stage 2
### Description
Great! You now have a first impression of how reads are stored. The next parameter is the length. The longer a read sequence, the easier it is to assemble. Sequences can have different sizes depending on the sequencing type. Their length can vary even within the same file. You may have noticed that information about the length is sometimes present on the line with the sequence identifier. Nevertheless, it is always better to double-check this data. Now, let's create a read counter.

### Objectives
*   Take the input path to the FASTQ file with data;
*   Calculate the number of reads\* based on their length.  
    \*Remember to delete the newline character before calculating the read length.

> In your answer, indicate how many reads are found in a file and their individual length. Next, evaluate the average length for all file's reads. Round up the average length to the nearest whole number. For instance, if the average is `65.4`, your answer should be `65`.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _contents of test1.fastq_

    @SRR12345678.5
    ATGCAAGATTCCATTCTGACGACCGTAGTGAAAGATATCGACGGTGAAGTGACCACGCTTGCGAAGTTCTCCTGTT
    +SRR12345678.5
    -ABC@EF<FFFF9FFFGCAFF7FF7F,,B,,,,,,C,CE,,@++B,,,,<,,<@,:,7B,,,++++:<C,<C,,:,
    @SRR12345678.6
    ATATTGAAGGTGGCCTGGAGATGAAGTACGGCTCCTGGTTCGGCCTGATTTACGTCTCCGGCTGGCCCTTGCATT
    +SRR12345678.6
    -A<CCDC<CCE98CFF8<8<8CC9<<C<E,+@@CFF8,CFE++@@F,,CCE9C,,;,,,++88+,,9:,:,:,,,
    @SRR12345678.7
    GTATTGGCGCTGATTAACAAACGCAATAGATAATGTTTTACCGGAACTGCTCGGTTCATCAATGTTGTAGTTGTTT
    +SRR12345678.7
    -A<CCD@FCGG7+EE<9E9<,E7C7+C99,<,,C,CFFFAEC,+++@C,@CC,+8@@,<<,,9,<C,:,,<C,,::
    @SRR12345678.8
    GTGCCGGACAGCCGCAGCATGAATCTGTCCAATGCGGTGTCGGTCGTTTTGTATTAATCCTTTCTTCTTTTTTTTT
    +SRR12345678.8
    -8-ACF7+@:<EF+@++@<E,,,CEF,CF@,,<,;++B+BC,+8,+8,,6,:,<,,,,<<C,,:,,<,,6<,+++8
    @SRR12345678.9
    TCAGCATACTCGCCGCCTCTGCTGCGGAAATCCCCGGCAGCGTCGCTGGCATATACAACCAGTCTCCTTCATTTAT
    +SRR12345678.9
    -8A-ACFCFGGCFE@FCCED8CF@D7++++;CCCD7+@++@+B@++8,+8,C,C,<,,:,,,9:,<?C6C,CC,,6
    @SRR12345678.10
    TCGTTACGAGAGTGTTCTCTGAACTCTATATGCGATTCATCTGCTGATCGCTCAATTACATGTCGAACTCTTTT
    +SRR12345678.10
    -A<CCFGEC@77C9FFFGGG,,,CEEF9E,<,C,,CDC,CCC,<C,,;,,866+,,<,<,,,<,,,,;,6<C,<

_Program output_

    > test1.fastq
    Reads in the file = 6:
          with length 74 = 1
          with length 75 = 1
          with length 76 = 4
    
    Reads sequence average length = 76

**Example 2:** _contents of test2.fastq_
    
    @SRR98765432.1071861 1071861
    CCCATAAAGATATACTGTTTTTTTTTCTTTCCCTCTTTTCTTCTTTTTCCTTCCCCCTTA
    +SRR98765432.1071861 1071861
    -88-8,-,--;-<,<,,,,,,9++++;,;;;;;,;,,;,,,,<;,,6,,;,;6,;,8+,,
    @SRR98765432.1071862 1071862
    CGCTATGACCATTTCGCCCTCCTCTTCGGCAACCTTTCCATCCCTTCCCTCTCACAATATT
    +SRR98765432.1071862 1071862
    8-8-,8-,;C,;C,-,8,8+;,;C<,;,,+++,,;6,;,,,,,;;C,;;,,;;,;,,;,<,
    @SRR98765432.1071863 1071863
    CTTCATCGCTGCCCGTTTCTTGTTCCAGAAACTTTTTCCACGGTTATCCCCTCACCATAA
    +SRR98765432.1071863 1071863
    AACC,CC,BC,@@C-+;;CCC,;C@C,,,,,;C,,<;,;,;,+,,,;;;;,,8,;;,;,,
    @SRR98765432.1071864 1071864
    CTTTTCTGCCTTCACGTTCCATCCTTCTCCGTCTTTCTTTCCGTTCCCCTCTCCTTACTT
    +SRR98765432.1071864 1071864
    -8,-8C-,<;E-;,;,,;;;,,;;6CC,;C+:,,,<;,,,<;,,,;;,,,,,;;,;,;<C

_Program output_

    > test2.fastq
    Reads in the file = 4:
          with length 60 = 3
          with length 61 = 1
    
    Reads sequence average length = 60

---

## Stage 3
### Description
The next notion we're going to discuss in this project is the **GC-content**. You know that a DNA sequence is formed by adenine (A), thymine (T), cytosine (C), and guanine (G) nucleotides. In a FASTQ file, you see only one DNA strand. However, in nature, any DNA is **double-stranded**. There are two bonds between A and T and three bonds between C and G (see figure). Depending on the number of G and C nucleotides, DNA may have different properties. That's the reason why the GC-content is necessary to evaluate.

The evaluation of GC-content can be useful in:

*   Bacterial classification during the separation of a high-level bacterial group;
*   Laboratory experiments if you work with the so-called wet DNA to properly plan your experiment;
*   Genome assembly when you intend to assemble a genome "puzzle" with the highest quality.

![](https://ucarecdn.com/f6704b30-533a-41ac-ace0-32005da0b045/)

To guess the quality of your data or to advise your colleagues on how to plan an experiment, you need to calculate the GC-content. Usually, this parameter is measured as a percentage (GC%). As the name of this parameter implies, the GC-content can be counted as follows:

![](https://i.gyazo.com/6a35523200a629a6f5682ca6047bb575.png)

\# denotes the number of elements. For instance, \#C is the number of C nucleotides in a sequence. If you encounter unknown nucleotides (N) in the sequence, add them to the denominator.

To measure the total GC content:

*   Calculate average GC for every read and round to two decimal,
*   Then count mean for all average rounded values.

Let's see an example to make it all clear. If you have the following DNA: `AATGCTNGCG`, then the GC-content value will be:

![](https://i.gyazo.com/9618588228c853294d08e7959f3f9c44.png)

According to the [Targeted Hybrid Capture for Inherited Disease Panels](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/gc-content) study by Sami S. Amr and Birgit Funke, the optimal GC-content level for a genome assembly lies in a range from 50 to 60% if we talk about bioinformatics applications.

### Objectives
*   Take the input path to the FASTQ file with data;
*   Calculate the mean value of the GC-content for all reads in the FASTQ file.

It is guaranteed that the file contains only four-line reads.

> Round the GC-content value to two decimal places. Don't forget to separate an average length from the GC-content mean by a newline character.

### Examples
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _contents of test1.fastq_

    @SRR12345678.1 1 length=75
    GCACACAACCGTGATGCTGAGCTGGCGTCGGTGGTATCAAATATGTCCAGCGAGCCGCACGTTACCCCTCCACTT
    +SRR12345678.1 1 length=75
    -ABCCGGFGGGGG9FFFEACFFGC<FEBC++8,+C9FG9<,C,CEFEFC,C@++8:+++8+C@,89C@,8,,,99
    @SRR12345678.2 2 length=76
    CACTGACTGGGATTTTTTGCAGCGAGTTTGCCAGCAGGTGGGATTTTCACCGGTTGTTATTCGCGAAGTTAATGAA
    +SRR12345678.2 2 length=76
    @BCCCGGGGGGGGGGGGGGGGGGGDGFGGCFG9EFCFDGG?7,CFFFFCFF7+@C+BC,CCC,:++++:C,,<,,,

_Program output_

    > test1.fastq
    Reads in the file = 2
    Reads sequence average length = 76
    
    GC content average = 51.69%

**Example 2:** _contents of test2.fastq_

    @SRR98765432.1 1 length=71
    CGGTAATAGTCACGGTGCTCATGCTTGCTCCTTAAGGGCGTTAACACGCAAAGTAACGGCATTTTTGTGGT
    +SRR98765432.1 1 length=71
    ACCCCGGGGGGGGFGGGGGGGGGGGGGGGGGGGCAEFDFEEFDFFFF7B:+@8F9,C,+8+@EFFF+C,,,
    @SRR98765432.2 2 length=76
    GTTTCCCGCTTCGTGCACTGAAATTTTATGATAACGATGGTGCGCGGCAGGAAGTGATTTCCGAAGCCTTTAAATT
    +SRR98765432.2 2 length=76
    -ACCCGGGGEGGGGFGGFGFCCDFFGGGGF,C@EF@7FDDE,C+@+::++6,,,:,,<<,<6,,,+86C,:,,,,6
    @SRR98765432.3 3 length=53
    GTGGATGACGGCCCATAACATCGCCTTCGTCGTGGTCAATATCAATATTAACT
    +SRR98765432.3 3 length=53
    -CCCCGGGGGGGGGGGGGGGGGGGGGGGGGGGGDGGFCFFAFFC,F9EF9<EE
    @SRR98765432.4 4 length=75
    TGGCAGAACAGCTTGATCAGATGGGCGGCGAGCAGCTGCGTCGCAAAATCGAAAGTATTTGCTTGCGCTTTCACA
    +SRR98765432.4 4 length=75
    @@CCCGGGGGFGGGGFFFGCFGGFCFCDF7@+@FAEFCF+BF@C:C7CFE7,,,+C,C,,,<,C,:+7+?D<,C,

_Program output_

    > test2.fastq
    Reads in the file = 4
    Reads sequence average length = 69
    
    GC content average = 47.48%

---

## Stage 4
### Description

The sequencer has imperfections. Sometimes, it can sequence the same part twice or even more. As a result, a FASTQ file may contain several reads with the same nucleotide order. Of course, it makes it harder to assemble a puzzle when you have identical details. In this light, it is necessary to catch the repeated reads to clear the data for further processing.

Repeated reads can appear as a result of the bacterial natural repeat sequencing, but for the sake of simplicity, we do not take this feature into account.

##### Objectives

*   Download the file [here](https://www.dropbox.com/s/o1i5ssuv1uvtqhx/SRR16506265_1.fastq?dl=0);
*   Place it in your working directory;
*   In your code, input path to the FASTQ file;
*   Find all repeated reads\* in this file and print their total number.  
    \* Repeats are the extra reads. For example, if the sequence of the same read occurs three times in the file, then the number of repeats is two.

> Your final program should input the path to the FASTQ file and print the information about it (see the Examples section).

##### Examples

The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _contents of test\_1.fastq_

    @SRR12345678.1
    GAGCCATATGACCACGCCGGAGAATCTCGCCAAGCAGGCAAAGCTGATGGAAGGCTACGGTGCGCCCTGTTTTTAT
    +SRR12345678.1
    -@CCCGGGGFFGGCFGGGEEDFDFFGDFCEE,:@FDC8FE8,@FC8<F<,<,8,CC8C,,C,:++8@C,:,6:C,9
    @SRR12345678.2
    GTCGATGGCCTGAACTACTCACGCTTCGAGAAGCAGATGCCTGCGCTGGCAGGTTTTGCTGAGCAAAATATTTCGT
    +SRR12345678.2
    -ACCCGFFGGGFCFGGGGGGCGCFGEGD8C878EAFGGCEFFEF7CFC7@,@+CEFD,CF,,,:,,,,:,<CCE,:
    @SRR12345678.3
    CGTCTGCGTCGAATCGACGCTACGCGACGGCTTTTTTCTGGAGTATTTCGGCGTGGTGCTTGAAGACGCAACTCT
    +SRR12345678.3
    @ACCCFFFFGGGFFGF?E@@FEGEGDCFC7CCEGGCGEFE,,,C,CE@E,+@+@++:,6CE,,,,,:,4++899,
    @SRR12345678.4
    CGCAGAACCTGCACAGGAAAGCGACGAGCTGATCGTTAAAGATGCTAACGGCAATCTGCTGGCTGACGGCGACAG
    +SRR12345678.4
    @@CCCGGGGGGGGGGGDF@CGGCEGDD>FFC,EFDFGE@FA,C9CE99F@7B7+CCE,CF,,6C,,C,+8++8++
    @SRR12345678.5
    CTTTATGCCCCCACAGTGCGATCAGGAAGTACATCGGCACCAGCATCATTTCCCAGAAGAAGAAGAACATGAACAT
    +SRR12345678.5
    CCCCCGFGGGGGDGDCFCFEDFEEDC?CDE9FAFGECF>FF8,C,FE8CEEFFF,,,,,,,,,,,,,C,,,,,:,:
    @SRR12345678.6
    GTCGATGGCCTGAACTACTCACGCTTCGAGAAGCAGATGCCTGCGCTGGCAGGTTTTGCTGAGCAAAATATTTCGT
    +SRR12345678.6
    -ACCCGFFGGGFCFGGGGGGGGCFGEGD8C878FAFGGCEFFEF7CFC7@,A+CEFD,CF,,,:,,,,:,<CCD,:

_Program output_

    > test_1.fastq
    Reads in the file = 6
    Reads sequence average length = 76
    
    Repeats = 1
    
    GC content average = 52.65%

**Example 2:** _contents of test\_2.fastq_

    @SRR12345678.11 11 length=74
    TTACATCATCATCGGTCACTCTGAACGTCGTACTTACCACAAAGAATCTGACGACCTGATCGCGAAACAATTCG
    +SRR12345678.11 11 length=74
    -8ACCGGGGGGGGGDFGGGGGGFFFGFGFDF?EGGGGCFGC,<,<,CCF,,C,,+8@,,;C,8+++++,,:CC,
    @SRR12345678.12 12 length=76
    CCCATCGGCACGCTTTCTGGTGGCAATCAGCAAAAAGTGGTGATCGGTCGTTGGGTCTATGCTGCCAGCCAGTTTT
    +SRR12345678.12 12 length=76
    B@CCCGGGGGGGGGGGFFFFGFGGGGGFFFGG@8,FEFAFGC,EFGDGCC@C<@+C@F,E<@F9E<,,66,,,<C@
    @SRR12345678.13 13 length=74
    TCTGGAACAACTCGGCTTTACGCTGGCGAAGTTACCCGCAGGGTTAAATTCCAGCCCCCGTCCGTCTCCACTCC
    +SRR12345678.13 13 length=74
    -AC9C9EFGGGFGC7ECCFFF7FE>@F@++6CF<CAEEE@+++;@<9,<,CC,,:C,,++88++,,:,,,:,6:
    @SRR12345678.14 14 length=74
    TTACATCATCATCGGTCACTCTGAACGTCGTACTTACCACAAAGAATCTGACGACCTGATCGCGAAACAATTCG
    +SRR16506265.14 14 length=74
    -8ACCGGGGGGGGGDFGGGGGGFFFGFGFDF?EGGGGCFGC,<,<,CCF,,C,,+8@,,;C,8+++++,,:CC,
    @SRR12345678.15 15 length=76
    CGACAGGACCGGACGTGTACTGCTTAATCAGTTTGTTTCTGCCGCTGTTTCCGCGATGACTACCAATGTGGCACGT
    +SRR12345678.15 15 length=76
    @CCCCGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGFFECGGGGGGGEG7+8,,:E,CE,,C,C,,:,C,:
    @SRR12345678.16 16 length=74
    TTACATCATCATCGGTCACTCTGAACGTCGTACTTACCACAAAGAATCTGACGACCTGATCGCGAAACAATTCG
    +SRR12345678.16 16 length=74
    -8ACCGGGGGGGGGDFGGGGGGFFFGFGFDF?EGGGGCFGC,<,<,CCF,,C,,+8@,,;C,8+++++,,:CC,

_Program output_

    > test_2.fastq
    Reads in the file = 6
    Reads sequence average length = 75
    
    Repeats = 2
    
    GC content average = 49.75%

---

## Stage 5
### Description
Repeats aren't the only problem with our sequencer. Sometimes the sequencer cannot identify a nucleotide and decipher it correctly. In this case, we will see the `N` letter (compare it with the traditional nucleotides `A`, `T`, `C`, or `G`). Here, `N` stands for an **undefined nucleotide**. The number of such nucleotides varies, depending on the quality of the original DNA and the sequencing type. When you encounter read sequences with a lot of `N`s, consider these reads to be of a low quality.

### Objectives
You have a FASTQ file with a set of reads. All these reads are of the same length.

*   Take the input path to the FASTQ file with data;
*   Calculate the percentage of the undefined nucleotides ( `N` ) per sequence, the number of such reads, and the average Ns percentage per read sequence for Ns-containing reads. Round the Ns% per sequence value to two decimal places.

The formula to count Ns% per sequence is

![](https://i.gyazo.com/fb8490f87b4980de3a90809c4894861d.png)

To check your code, you can use test files [test1.fastq](https://stepik.org/media/attachments/lesson/608059/test1.fastq) and [test2.fastq](https://stepik.org/media/attachments/lesson/608059/test2.fastq).

### Example
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

**Example 1:** _contents of test.fastq_

    @SRR1234567.1 length=101
    GGTTGCAGATTCGCAGTGTCGCTGTTCCAGCGCATCACATCTTTGATGTTCACGCCGTGGCGTTTAGCAATGCTTGAAAGCGAATCGCCTTTGCCCACACG
    +
    @?:=:;DBFADH;CAECEE@@E:FFHGAE4?C?DE<BFGEC>?>FHE4BFFIIFHIBABEECA83;>>@>@CCCDC9@@CC08<@@BB@9:CC#######
    @SRR1234567.4 length=101
    GTATGAGGTTTTGCTGCATTCTCTGNGCGAATATTAACTCCNTNNNNNTTATAGTTCAAAGCAAGTACCTGTCTCTTATACACATCTCCGAGCCCACGAGC
    +
    @@<?=D?D==?<AFGDF+AIHEACH#22<:?E8??:9??GG#0#####000;CF=C)4.==CA@@@)=7?C7?E37;3@>;(.;>AB#############
    @SRR1234567.10 length=101
    GCTTCTCTTAACTGAGGTCACCATCATGCCGTTAAGTCCCTACCTCTCTTTTGCCGGTAACTGTTCCGCCGCGATTGCCTTTTATCTGTCTCTTATACACC
    +
    ??<DBD;4C2=<BB>:AC;<CF<CE@FE9@E1C@891CD*9:?:3D@DD4D<DD:0;@A=AEIDDA##################################

_Program output_

    > test.fastq
    Reads in the file = 3
    Reads sequence average length = 101
    
    Repeats = 0
    Reads with Ns = 1
    
    GC content average = 47.52%
    Ns per read sequence = 2.31%
    
---

## Stage 6
### Description
Good job! It's time to complete the task.

The HR dept. sent you three archives in the _.gz_ format. These archives can be opened by the `gunzip` command. Another way is to get access to the FASTQ file without extraction is the `import gzip` Python command. Choose one of these options or use other tools as you see fit.

### Objectives
*   Take input paths to three data archives with FASTQ files;
*   Extract the archives. For each archive, calculate the total number of reads, read sequences with `N`s, average read sequence length, GC content, Ns% per read sequence, and the number of repeats;
*   Compare the quality of data archives and conclude which data is the best;
*   Print the data quality parameters for the selected best archive only.

To test your code, you can use [data1.gz](https://stepik.org/media/attachments/lesson/608059/data1.gz), [data2.gz](https://stepik.org/media/attachments/lesson/608059/data2.gz), [data3.gz](https://stepik.org/media/attachments/lesson/608059/data3.gz). Use your knowledge to determine which archive is the best (for example, it should have a minimum of repeats and unknown nucleotides).

### Example
**Example 1:** _contents of data1.gz_

    @HWI-ST745_0097:7:1101:1009:1000#0/1
    ATTCTGACTGCANNGGGCAATATGTCTTTGTGTGGATTAAAGAAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTA
    +HWI-ST745_0097:7:1101:1009:1000#0/1
    -8A-ACFCFGGC##@FCCED8CF@D7++++;CCCD7+@++@+B@++8,+8,C,C,<,,:,,,9:,<?C6C,CC,,6
    @HWI-ST745_0097:7:1101:1010:1000#0/1
    CTNTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATACCAGCTCGTGAAGTGGTTAC
    +HWI-ST745_0097:7:1101:1010:1000#0/1
    --#A<CCFGEC@77C9FFFGGG,,,CEEF9E,<,C,,CDC,CCC,<C,,;,,866+,,<,<,,,<,,,,;,6<C,<
    @HWI-ST745_0097:7:1101:1011:1000#0/1
    TCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACC
    +HWI-ST745_0097:7:1101:1011:1000#0/1
    --BCCCFDFGGGGGGFGGFGGC@8BFA9F9,C,F7++@<99EF7CFF8EFE9,C,,:,:C,+8B@+CF,,,<CCE,

_Contents of data2.gz_

    @HWI-ST745_0097:7:1101:1016:1000#0/1
    CTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGGTTCTGAACTGGTTACCTGCCG
    +HWI-ST745_0097:7:1101:1016:1000#0/1
    BBBCCCGGGFE9FAF9DFEGFFG7+CFC@FECFF9F7C@ECE+C,,,CF,@CF,+++6+8,:9,+8@+<,<C,,,,
    @HWI-ST745_0097:7:1101:1017:1000#0/1
    TTCAACGGGCAATATGTCTCTGTGTGGATTAGAAAAAGAGTGTCTGATAGCAGCCTCTGAACTGGTTACCTGCCGT
    +HWI-ST745_0097:7:1101:1017:1000#0/1
    --@ACCFGFFFCEF7FE7@C7F7CFFG?ECF,+@::FF8EF9CF,,,B+,;C:+,:+,7++8+8CB,,,:,,,9:4
    @HWI-ST745_0097:7:1101:1018:1000#0/1
    GCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCTGCTTCTGAACTGGTTACCCGCCGTG
    +HWI-ST745_0097:7:1101:1018:1000#0/1
    --6A<CGEGGCDFGGGC87,@<;888EFFGAEF,CF8FF8CC+CF+++++,;,,,:C,8CCCF,69C@E,,,:CC,

_Contents of data3.gz_

    @HWI-ST745_0097:7:1101:1025:1000#0/1
    GCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAAT
    +HWI-ST745_0097:7:1101:1025:1000#0/1
    AABB@CGGGGGGGGGGF9,CFGEFFDFDF99,<EDFCF@8E9C,EF9CEF++@+@,,,,;,,,;,C,CE,,,:CCE
    @HWI-ST745_0097:7:1101:1026:1000#0/1
    CAANNNGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGAAAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATT
    +HWI-ST745_0097:7:1101:1026:1000#0/1
    -AC###GCGGGGGGGGGFGGGCFFGG7BEFFG?88FF@7F7@7F777EE,C,@7++8@EFEFEE+,6>88,:,,<,
    @HWI-ST745_0097:7:1101:1027:1000#0/1
    AATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCNTCAGAACTGGTTACCTGCCGTGAGTAAATTA
    +HWI-ST745_0097:7:1101:1027:1000#0/1
    BBBBCCGGGGGGFDF9FFGFCFFE?FDC7F8,C7FC;@CFFG9C#+@+++@@@FFECF,CCC,EE8?C,BCEE,,8

_Program output_

    > data1.gz
    > data2.gz
    > data3.gz
    
    Reads in the file = 3
    Reads sequence average length = 76
    
    Repeats = 0
    Reads with Ns = 0
    
    GC content average = 46.49%
    Ns per read sequence = 0%