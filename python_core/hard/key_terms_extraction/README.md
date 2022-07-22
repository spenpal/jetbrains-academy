# Key Terms Extraction

## Stage 1
### Theory
**Key term extraction**, also known as **keyword extraction**, is an important **Natural Language Processing (NLP)** task that makes it possible to automatically identify terms that best describe the subject of a document.

Key term extraction is the core of the content-based advertising systems used by search engines. This approach is used to find the relevant keywords on a webpage and then show the ads based on those keywords. The extraction quality is a cornerstone for these tasks. A 10% improvement in quality leads to an almost 10% increase in click-through rate, directly increasing the advertisement performance.

What words can describe the subject of a piece of text accurately? It's safe to assume that they are the most frequent words, but it can be a little more complicated than that!

### Description
In this stage, you will be working with an XML file containing news stories and headlines. You need to find the most frequent words in each news story. The news text must be divided into tokens, use tokenization tools implemented in the `nltk` library.

Tokenization is an essential step for NLP. There are lots of ways to do it, from using regular expressions to machine learning. You need to use the `word_tokenize()` function from `nltk` to successfully complete this task. It returns a list of tokens (including words and punctuation) and divides a word `cat's` into two parts: `cat` and `'s` (do not remove the second token).

Sometimes, depending on the type of tokenization, you need to rewrite the text in lowercase letters. You need to tokenize the texts as shown below.

    nltk.tokenize.word_tokenize(text.lower())

Find the five most common tokens for each news story and print them together with the story's title.

If the frequencies for some tokens are the same, then sort them by their names in descending order. For example, for the following dictionary, where the keys are the names of fruits, and the values of the frequency of their occurrence:

    {"apple": 5, "lemon": 6, "banana": 5, "grapefruit": 1, "pineapple": 5, "watermelon": 3, "melon": 4, "dragonfruit": 5}

After sorting, the dictionary should look the following way:

    {"lemon": 6, "pineapple": 5, "dragonfruit": 5, "banana": 5, "apple": 5, "melon": 4, "watermelon": 3, "grapefruit": 1}

Mind the output formatting! You need to follow it so that the system can check the solution! Display the titles and keywords in the same order as the news items in the file.

You can take a look at the [news file](https://stepik.org/media/attachments/lesson/395600/news.xml) to see what you will be working with.

### Objectives
Your program should:

1.  Read an XML file containing news stories and headlines.
2.  Extract the headers and the text.
3.  Tokenize the texts.
4.  For each story, find the most frequent tokens that appear in it.
5.  Print the headline of each news story and the five most frequent tokens in descending order. Take a look at a sample below. Also, display the titles and keywords in the same order they are presented in the file.

### Example
**Example 1:** _an example of the input_

    <?xml version='1.0' encoding='UTF8'?>
    <data>
      <corpus>
        <news>
          <value name="head">New Portuguese skull may be an early relative of Neandertals</value>
          <value name="text">Half a million years ago, several different members of our genus, Homo, had spread throughout Europe and Asia, where some would eventually evolve into Neandertals.
              But which ones has been the subject of intense debate.
              A newly discovered partial skull is offering another clue to help solve the mystery of the ancestry of Neandertals.
              Found in 2014 in the Gruta da Aroeira cave in central Portugal with ancient stone hand axes, the skull (3D reconstruction pictured) is firmly dated to 400,000 years old and an archaic member of our genus, according to a study published today in the Proceedings of the National Academy of Sciences.
              The skull shows a new mix of features not seen before in fossil humans-it has traits that link it to Neandertals, such as a fused brow ridge, as well as some primitive traits that resemble other extinct fossils in Europe.
              This new combination of features on a well-dated skull may help researchers sort out how different fossils in Europe are related to each other-and which ones eventually evolved into Neandertals.</value>
        </news>
        <news>
          <value name="head">Loneliness May Make Quitting Smoking Even Tougher</value>
          <value name="text">Being lonely may make it harder to quit smoking, a new British study suggests.
              Using genetic and survey data from hundreds of thousands of people, researchers found that loneliness makes it more likely that someone will smoke.
              This type of analysis is called Mendelian randomization.
              'This method has never been applied to this question before and so the results are novel, but also tentative,' said co-lead author Robyn Wootton, a senior research associate at the University of Bristol in the United Kingdom.
              'We found evidence to suggest that loneliness leads to increased smoking, with people more likely to start smoking, to smoke more cigarettes and to be less likely to quit,' Wootton said in a university news release.
              These data mesh with an observation that during the coronavirus pandemic, more British people are smoking.
              Senior study author Jorien Treur said, 'Our finding that smoking may also lead to more loneliness is tentative, but it is in line with other recent studies that identified smoking as a risk factor for poor mental health.
              A potential mechanism for this relationship is that nicotine from cigarette smoke interferes with neurotransmitters such as dopamine in the brain.'
              Treur is a visiting research associate from Amsterdam UMC.
              The researchers also looked for a connection between loneliness and drinking but found none.
              Still, if loneliness causes people to smoke, it is important to alert smoking cessation services so they can add this factor as they help people to quit, the study authors said.
              The report was published June 16 in the journal Addiction.</value>
        </news>
      </corpus>
    </data>

_An example of the output:_

    New Portuguese skull may be an early relative of Neandertals:
    of the , in a
    
    Loneliness May Make Quitting Smoking Even Tougher:
    , to . the that 
    
---

## Stage 2
### Theory
We need to improve the results because they don't really look like keywords. There are dots, commas, articles, and conjunctions. To do this, we need to process the news text by removing punctuation marks and function words. We will calculate the frequency once again and output the five most frequent words.

First, you should tokenize your text. After tokenization, you need to **lemmatize** the words using `WordNetLemmatizer()` from the `nltk` library. By default, the `WordNetLemmatizer` lemmatizes only nouns. In this stage, you do NOT need to deal with the lemmatization of words of other parts of speech.

Articles, conjunctions, and some other words belong to the **stop-words** group. These words do not have a particular meaning, but they are extremely common in text and can influence the result significantly. In the `nltk` library, you can get a list of these words by using:

    stopwords.words('english')

You can import the stopwords in the following way:

    from nltk.corpus import stopwords

How can we get rid of punctuation? There are a lot of methods: from iterating through every character to using regular expressions. In this project, we suggest using the `string` library. This line of code will enable you to get a list of punctuation marks:

    list(string.punctuation)

Once you have the summaries for each piece of news, you should print them as you did in the first stage.

### Description
In this stage, you need to convert the text, tokenize it, perform lemmatization, and get rid of stop words and punctuation marks. You will then be able to see how the results have changed. Sometimes, depending on the type of tokenization, you need to rewrite the text in lowercase letters to get rid of the stop words in a proper way. You need to tokenize the texts as shown below.

    nltk.tokenize.word_tokenize(text.lower())

For each news item, find the five most common tokens and print them together with the title. Mind that the `word_tokenize()` function might identify such contractions as `'s` as separate tokens. if any, you do NOT need to remove such contractions from the lists of frequent tokens.

If the frequencies for some tokens are the same, then sort them in descending order. For example, for the following dictionary, where the keys are the names of fruits, and the values of the frequency of their occurrence:

    {"apple": 5, "lemon": 6, "banana": 5, "grapefruit": 1, "pineapple": 5, "watermelon": 3, "melon": 4, "dragonfruit": 5}

After sorting, the dictionary should be

    {"lemon": 6, "pineapple": 5, "dragonfruit": 5, "banana": 5, "apple": 5, "melon": 4, "watermelon": 3, "grapefruit": 1}

> Mind the output formatting! You need to follow it so that the system can check the solution! Display the titles and keywords in the same order as the news items in the file.

Take look at the attached [news file](https://stepik.org/media/attachments/lesson/395600/news.xml). Please use it in your project.

We asked you to leave the contractions as they are for now. Working on this project, you're bound to stumble upon some weird lemmatization we also don't want you to do anything about. Let us explain ourselves. Although projects are primarily educational, they also serve as practice for real ones, so you could get a little taste of the reality of being a programmer. Unfortunately, in real life, the expected results are not always the same as the ones you actually get, especially when you use external tools and libraries. And often you just have to work with what you have. Though we asked you not to do anything about these imperfections for now, it doesn't mean that you cannot approach such cases creatively in your future projects. Another useful point is that sometimes there is no need to waste your time, energy, and performance of your program on things that will later eliminate themselves (you may suppose what such things are or find it out empirically). We hope you agree that such an approach makes sense if the final result is going to be just the one you need without any additional trouble on your part. For now, you just have to trust us and mark our word that those contractions will be naturally sorted out in the later stages of the project. If you feel the urge to do something about them, just be patient. Please keep this information in mind for the rest of the project, and maybe you will find it useful in your future work.

### Objectives
Your program should:

1.  Read an XML file containing news stories and headlines.
2.  Extract the headers and the text.
3.  Tokenize each text.
4.  Lemmatize each word in the story.
5.  Get rid of punctuation and stopwords with the help of NLTK.
6.  For each news story, find the most frequent tokens.
7.  Print each story's headline and five most frequent tokens in descending order. Take a look at the sample below. Display the titles and keywords in the same order they are presented in the file.

##### Example

**Example 1:** _Input file structure_

    <?xml version='1.0' encoding='UTF8'?>
    <data>
      <corpus>
        <news>
          <value name="head">New Portuguese skull may be an early relative of Neandertals</value>
          <value name="text">Half a million years ago, several different members of our genus, Homo, had spread throughout Europe and Asia, where some would eventually evolve into Neandertals.
              But which ones has been the subject of intense debate.
              A newly discovered partial skull is offering another clue to help solve the mystery of the ancestry of Neandertals.
              Found in 2014 in the Gruta da Aroeira cave in central Portugal with ancient stone hand axes, the skull (3D reconstruction pictured) is firmly dated to 400,000 years old and an archaic member of our genus, according to a study published today in the Proceedings of the National Academy of Sciences.
              The skull shows a new mix of features not seen before in fossil humans-it has traits that link it to Neandertals, such as a fused brow ridge, as well as some primitive traits that resemble other extinct fossils in Europe.
              This new combination of features on a well-dated skull may help researchers sort out how different fossils in Europe are related to each other-and which ones eventually evolved into Neandertals.</value>
        </news>
        <news>
          <value name="head">Loneliness May Make Quitting Smoking Even Tougher</value>
          <value name="text">Being lonely may make it harder to quit smoking, a new British study suggests.
              Using genetic and survey data from hundreds of thousands of people, researchers found that loneliness makes it more likely that someone will smoke.
              This type of analysis is called Mendelian randomization.
              'This method has never been applied to this question before and so the results are novel, but also tentative,' said co-lead author Robyn Wootton, a senior research associate at the University of Bristol in the United Kingdom.
              'We found evidence to suggest that loneliness leads to increased smoking, with people more likely to start smoking, to smoke more cigarettes and to be less likely to quit,' Wootton said in a university news release.
              These data mesh with an observation that during the coronavirus pandemic, more British people are smoking.
              Senior study author Jorien Treur said, 'Our finding that smoking may also lead to more loneliness is tentative, but it is in line with other recent studies that identified smoking as a risk factor for poor mental health.
              A potential mechanism for this relationship is that nicotine from cigarette smoke interferes with neurotransmitters such as dopamine in the brain.'
              Treur is a visiting research associate from Amsterdam UMC.
              The researchers also looked for a connection between loneliness and drinking but found none.
              Still, if loneliness causes people to smoke, it is important to alert smoking cessation services so they can add this factor as they help people to quit, the study authors said.
              The report was published June 16 in the journal Addiction.</value>
        </news>
      </corpus>
    </data>

_A sample of the output_:

    New Portuguese skull may be an early relative of Neandertals:
    skull neandertal fossil europe year 
    
    Loneliness May Make Quitting Smoking Even Tougher:
    smoking people loneliness study smoke
---

## Stage 3
### Theory
Hooray! The output from the last stage looks so much better! We can still improve the results, though: adverbs and adjectives don't always reflect the essence of the text. Nouns are very useful with this. In this stage, we will improve the result by using **part-of-speech tagging** **(a POS-tag)** to mark nouns as keywords.

### Description
The task is similar to the previous ones: tokenize, lemmatize, and eliminate meaningless words. In addition to removing punctuation and stop words, remove all the non-noun words. You can use `averaged_perceptron_tagger` for this. You need to load it first:

    nltk.download('averaged_perceptron_tagger')

Let's look at a simple example. To find out a POS-tag of the word `cat`, we need to write the following line of code:

    nltk.pos_tag(['cat'])[0][1]

This gives the following:

    "NN"

This tag denotes a noun. You can see a list of other tags using the command:

    nltk.help.upenn_tagset()

In our project, we need the `"NN"` tag **only**.

Sometimes, depending on the type of tokenization, you need to rewrite the text in lowercase letters to get rid of the stopwords in a proper way. You need to tokenize the texts as shown below.

    nltk.tokenize.word_tokenize(text.lower())

If the frequencies for some tokens are the same, then sort them in descending order. For example, for the following dictionary, where the keys are the names of fruits, and the values of the frequency of their occurrence:

    {"apple": 5, "lemon": 6, "banana": 5, "grapefruit": 1, "pineapple": 5, "watermelon": 3, "melon": 4, "dragonfruit": 5}

After sorting, the dictionary should be

    {"lemon": 6, "pineapple": 5, "dragonfruit": 5, "banana": 5, "apple": 5, "melon": 4, "watermelon": 3, "grapefruit": 1}

> Attention! We ask you to apply the POS-tag for each word, and not for the entire text of the news!

Take a look at the attached [news file](https://stepik.org/media/attachments/lesson/395600/news.xml). Please, use it in this stage.

### Objectives
In this stage, your program should:

1.  Read an XML-file containing news stories and headlines.
2.  Extract the headers and the text.
3.  Tokenize each text.
4.  Lemmatize each word in the story.
5.  Get rid of punctuation and the stopwords provided by NLTK.
6.  For each news story, find the most frequent nouns.
7.  Print each story's headline and the five most frequent nouns in descending order. Take a look at the sample below. Display the titles and keywords in the same order they are presented in the file.

### Examples
**Example 1:** _Input file structure_

    <?xml version='1.0' encoding='UTF8'?>
    <data>
      <corpus>
        <news>
          <value name="head">New Portuguese skull may be an early relative of Neandertals</value>
          <value name="text">Half a million years ago, several different members of our genus, Homo, had spread throughout Europe and Asia, where some would eventually evolve into Neandertals.
              But which ones has been the subject of intense debate.
              A newly discovered partial skull is offering another clue to help solve the mystery of the ancestry of Neandertals.
              Found in 2014 in the Gruta da Aroeira cave in central Portugal with ancient stone hand axes, the skull (3D reconstruction pictured) is firmly dated to 400,000 years old and an archaic member of our genus, according to a study published today in the Proceedings of the National Academy of Sciences.
              The skull shows a new mix of features not seen before in fossil humans-it has traits that link it to Neandertals, such as a fused brow ridge, as well as some primitive traits that resemble other extinct fossils in Europe.
              This new combination of features on a well-dated skull may help researchers sort out how different fossils in Europe are related to each other-and which ones eventually evolved into Neandertals.</value>
        </news>
        <news>
          <value name="head">Loneliness May Make Quitting Smoking Even Tougher</value>
          <value name="text">Being lonely may make it harder to quit smoking, a new British study suggests.
              Using genetic and survey data from hundreds of thousands of people, researchers found that loneliness makes it more likely that someone will smoke.
              This type of analysis is called Mendelian randomization.
              'This method has never been applied to this question before and so the results are novel, but also tentative,' said co-lead author Robyn Wootton, a senior research associate at the University of Bristol in the United Kingdom.
              'We found evidence to suggest that loneliness leads to increased smoking, with people more likely to start smoking, to smoke more cigarettes and to be less likely to quit,' Wootton said in a university news release.
              These data mesh with an observation that during the coronavirus pandemic, more British people are smoking.
              Senior study author Jorien Treur said, 'Our finding that smoking may also lead to more loneliness is tentative, but it is in line with other recent studies that identified smoking as a risk factor for poor mental health.
              A potential mechanism for this relationship is that nicotine from cigarette smoke interferes with neurotransmitters such as dopamine in the brain.'
              Treur is a visiting research associate from Amsterdam UMC.
              The researchers also looked for a connection between loneliness and drinking but found none.
              Still, if loneliness causes people to smoke, it is important to alert smoking cessation services so they can add this factor as they help people to quit, the study authors said.
              The report was published June 16 in the journal Addiction.</value>
        </news>
      </corpus>
    </data>

_An example of the output:_

    New Portuguese skull may be an early relative of Neandertals:
    skull fossil europe year trait 
    
    Loneliness May Make Quitting Smoking Even Tougher:
    smoking loneliness study smoke quit
---

## Stage 4
### Theory
In this stage, we will take a closer look at the **TF-IDF** approach. It is used to calculate how important a word is for a document in a text collection. Search engines use this measure to score and rank the documents according to a user's query. It is also frequently used for text classification and text summarization, fundamental NLP tasks. The method is not computationally expensive and yields excellent results for such tasks.

The technique is based on two assumptions:

1.  Frequent words have more weight in the document.
2.  The smaller the number of documents that contain the word, the more important the word is for the document that contains it.

For this project, we need to calculate the TF-IDF for every word in **all** news stories! To make the task of this stage more clear, let's remind ourselves that TF-IDF is used for a collection of documents. In our case, this collection consists of the news which means that each news article should be treated as a separate document. Each one should be tokenized, lemmatized, cleared of anything but nouns. This way you can get the final collection of documents you'll be able to apply TF-IDF to.

Use `TfidfVectorizer` from `sklearn` to solve this task. You may also find the function `toarray()` useful. It converts a sparse matrix that `sklearn` uses to an ordinary n-dimensional array, so, using indexation, you may access the terms and their scores in a more familiar way. Check out the [Machine Learning Master tutorial](https://machinelearningmastery.com/prepare-text-data-machine-learning-scikit-learn/) on how to encode the text data for machine learning.

### Description
In this stage, you will get familiar with some of the theories behind this method and work with `sklearn`, one of the most popular Python machine learning libraries. Mind that sometimes, depending on the type of tokenization, you need to rewrite the text in lowercase letters to get rid of the stop words in a proper manner.

Take a look at the attached [news file](https://stepik.org/media/attachments/lesson/395600/news.xml). Please use it in your project.

 > Remember that you only need to select nouns, i.e. words with the tag "NN". Thus, the word "say" doesn't fit, because its tag is "VB".
>    `nltk.pos_tag(['say'])[0][1]  # VB`

### Objectives
In this stage, your program should:

1.  Read an XML-file containing stories and headlines.
2.  Extract the headers and the text.
3.  Tokenize _**each text**_.
4.  Lemmatize each word in _**each story**_.
5.  Get rid of punctuation, stopwords, and non-nouns with the help of NLTK.
6.  Count the TF-IDF metric for each word in _**all**_ stories, i.e. apply it to the whole collection of news documents.
7.  Pick the five best scoring words.
8.  Print each story's headline and the five most frequent words in descending order. Take a look at the sample output below. Display the titles and keywords in the same order they are presented in the file.

> If you have two words with equal TF-IDF scores, for example, «day», 0.375 and «cloud», 0.375, they should be sorted in reverse order, i.e. «day» should come first.

### Examples
**Example 1:** _Input file structure_

    <?xml version='1.0' encoding='UTF8'?>
    <data>
      <corpus>
        <news>
          <value name="head">New Portuguese skull may be an early relative of Neandertals</value>
          <value name="text">Half a million years ago, several different members of our genus, Homo, had spread throughout Europe and Asia, where some would eventually evolve into Neandertals.
              But which ones has been the subject of intense debate.
              A newly discovered partial skull is offering another clue to help solve the mystery of the ancestry of Neandertals.
              Found in 2014 in the Gruta da Aroeira cave in central Portugal with ancient stone hand axes, the skull (3D reconstruction pictured) is firmly dated to 400,000 years old and an archaic member of our genus, according to a study published today in the Proceedings of the National Academy of Sciences.
              The skull shows a new mix of features not seen before in fossil humans-it has traits that link it to Neandertals, such as a fused brow ridge, as well as some primitive traits that resemble other extinct fossils in Europe.
              This new combination of features on a well-dated skull may help researchers sort out how different fossils in Europe are related to each other-and which ones eventually evolved into Neandertals.</value>
        </news>
        <news>
          <value name="head">Loneliness May Make Quitting Smoking Even Tougher</value>
          <value name="text">Being lonely may make it harder to quit smoking, a new British study suggests.
              Using genetic and survey data from hundreds of thousands of people, researchers found that loneliness makes it more likely that someone will smoke.
              This type of analysis is called Mendelian randomization.
              'This method has never been applied to this question before and so the results are novel, but also tentative,' said co-lead author Robyn Wootton, a senior research associate at the University of Bristol in the United Kingdom.
              'We found evidence to suggest that loneliness leads to increased smoking, with people more likely to start smoking, to smoke more cigarettes and to be less likely to quit,' Wootton said in a university news release.
              These data mesh with an observation that during the coronavirus pandemic, more British people are smoking.
              Senior study author Jorien Treur said, 'Our finding that smoking may also lead to more loneliness is tentative, but it is in line with other recent studies that identified smoking as a risk factor for poor mental health.
              A potential mechanism for this relationship is that nicotine from cigarette smoke interferes with neurotransmitters such as dopamine in the brain.'
              Treur is a visiting research associate from Amsterdam UMC.
              The researchers also looked for a connection between loneliness and drinking but found none.
              Still, if loneliness causes people to smoke, it is important to alert smoking cessation services so they can add this factor as they help people to quit, the study authors said.
              The report was published June 16 in the journal Addiction.</value>
        </news>
      </corpus>
    </data>

_An example of the output:_

    New Portuguese skull may be an early relative of Neandertals:
    skull fossil europe trait genus
    
    Loneliness May Make Quitting Smoking Even Tougher:
    smoking loneliness smoke quit lead 