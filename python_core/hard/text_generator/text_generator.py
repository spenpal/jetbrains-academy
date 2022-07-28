# IMPORTS #
import random
from collections import Counter, defaultdict

from nltk import ngrams


# HELPER FUNCTION #
def iscapitalize(word):
    return word[0].isupper()


# CLASS #
class MarkovModel:

    def __init__(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            self.tokens = f.read().split()
            self.bigrams = list(ngrams(self.tokens, 2))
            self.trigrams = list(ngrams(self.tokens, 3))

        self.bigrams_dict = defaultdict(list)
        for head, tail in self.bigrams:
            self.bigrams_dict[head].append(tail)
        for head, tails in self.bigrams_dict.items():
            self.bigrams_dict[head] = Counter(tails).most_common()

        self.trigrams_dict = defaultdict(list)
        for head1, head2, tail in self.trigrams:
            self.trigrams_dict[(head1, head2)].append(tail)
        for head, tails in self.trigrams_dict.items():
            self.trigrams_dict[head] = Counter(tails).most_common()

        self.bigram_start_words = [word for word in self.bigrams_dict.keys() if
                                   iscapitalize(word) and word[-1] not in '.?!']
        self.trigram_start_words = [words for words in self.trigrams_dict.keys() if
                                    iscapitalize(words[0]) and words[0][-1] not in '.?!']

    def enquire_model(self):
        while (word := input()) != 'exit':
            try:
                print('Head:', word)
                tails = self.bigrams_dict[word]
                for tail, count in tails:
                    print(f'Tail: {tail}\tCount: {count}')
                print()
            except KeyError:
                print('Key Error. The requested word is not in the model. Please input another word.')

    def enquire_text(self):
        while (i := input()) != 'exit':
            try:
                idx = int(i)
                head, tail = self.bigrams[idx]
                print(f'Head: {head}\tTail: {tail}')
            except TypeError:
                print('Type Error. Please input an integer.')
            except IndexError:
                print('Index Error. Please input a value that is not greater than the number of all bigrams.')
            except ValueError:
                print('Value Error. Please input an integer.')

    def print_stats(self, *, tokens=False, unique_tokens=False, bigrams=False):
        print('Corpus statistics')
        if tokens:          print('All tokens:', len(self.tokens))
        if unique_tokens:   print('Unique tokens:', len(set(self.tokens)))
        if bigrams:         print('Number of bigrams:', len(self.bigrams))
        print()

    def get_random_text(self, sentence_count=10, token_count=10):
        prev_word = random.choice(self.tokens)
        sentences = []

        for _ in range(sentence_count):
            sentence = []
            for _ in range(token_count):
                next_words, weights = list(zip(*self.bigrams_dict[prev_word]))
                next_word = random.choices(next_words, weights=weights)[0]
                sentence.append(next_word)
                prev_word = next_word
            sentences.append(' '.join(sentence))

        return '\n'.join(sentences)

    def get_psuedo_sentences(self, sentence_count=10):
        sentences = []

        for _ in range(sentence_count):
            starting_word = random.choice(self.bigram_start_words)
            sentence = [starting_word]

            while not (len(sentence) >= 5 and sentence[-1][-1] in '.?!'):
                next_words, weights = list(zip(*self.bigrams_dict[sentence[-1]]))
                next_word = random.choices(next_words, weights=weights)[0]
                sentence.append(next_word)
            sentences.append(' '.join(sentence))

        return '\n'.join(sentences)

    def get_sentences(self, sentence_count=10):
        sentences = []

        for _ in range(sentence_count):
            starting_words = random.choice(self.trigram_start_words)
            sentence = list(starting_words)

            while not (len(sentence) >= 5 and sentence[-1][-1] in '.?!'):
                prev_words = (sentence[-2], sentence[-1])
                next_words, weights = list(zip(*self.trigrams_dict[prev_words]))
                next_word = random.choices(next_words, weights=weights)[0]
                sentence.append(next_word)

            sentences.append(' '.join(sentence))

        return '\n'.join(sentences)


# MAIN #
model = MarkovModel(input())
print(model.get_sentences())
