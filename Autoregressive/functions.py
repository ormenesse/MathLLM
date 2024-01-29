import re
class Vocabulary:
    PAD_token = 0     # Used for padding short sentences
    SOS_token = 1     # Start-of-sentence token
    EOS_token = 2     # End-of-sentence token
    def __init__(self, name, sentence_trim=50):
        self.PAD_token = 0     # Used for padding short sentences
        self.SOS_token = 1     # Start-of-sentence token
        self.EOS_token = 2     # End-of-sentence token
        self.NEW_WORD = 3
        self.START_NUMBER = 4
        self.END_NUMBER = 5
        self.name = name
        self.word2index = { 
            "new_word" : self.NEW_WORD,
            "PAD" : self.PAD_token,
            "SOS" : self.SOS_token,
            "EOS" : self.EOS_token,
            "<num>" : self.START_NUMBER,
            "</num>" : self.END_NUMBER
        }
        self.word2count = {
            "new_word" : 1,
            "PAD" : 1,
            "SOS" : 1,
            "EOS" : 1,
            "<num>" : 1,
            "</num>" : 1
        }
        self.index2word = {
            self.PAD_token: "PAD",
            self.SOS_token: "SOS",
            self.EOS_token: "EOS",
            self.NEW_WORD : "new_word",
            self.START_NUMBER: "<num>",
            self.END_NUMBER: "</num>"
        }
        self.num_words = 6
        self.num_sentences = 0
        self.longest_sentence = 0
        self.sentence_number = []
        self.sentence_trim = sentence_trim

    def add_word(self, word):
        if word not in self.word2index:
            # First entry of word into vocabulary
            self.word2index[word] = self.num_words
            self.word2count[word] = 1
            self.index2word[self.num_words] = word
            self.num_words += 1
        else:
            # Word exists; increase word count
            self.word2count[word] += 1

    def add_sentence(self, sentence):
        sentence_len = 0
        sentence = sentence.replace('|',' | ').replace(',',' , ').replace(':',' : ').replace('\n','').strip()
        numbers = re.findall('([-\d\.]+)',sentence)
        formattedSentence = []
        for word in sentence.split(" "):
            if word in numbers:
                word = ["<num>"] + [ c for c in word ] + ["</num>"]
                for c in word:
                    formattedSentence.append(c)
            else:
                formattedSentence.append(word.lower())
        for word in formattedSentence:
            sentence_len += 1
            self.add_word(word)
        if sentence_len > self.longest_sentence:
            # This is the longest sentence
            self.longest_sentence = sentence_len
        # Count the number of sentences
        self.num_sentences += 1
        self.sentence_number.append(sentence_len)

    def to_word(self, index):
        return self.index2word[index]

    def to_index(self, word):
        return self.word2index[word.lower()]

    def sentence_to_index(self, sentence, padding=False):
        sentence = sentence.replace('|',' | ').replace(',',' , ').replace(':',' : ').replace('\n','').strip()
        numbers = re.findall('([-\d\.]+)',sentence)
        formattedSentence = []
        for word in sentence.split(" "):
            if word in numbers:
                    word = ["<num>"] + [ c for c in word ] + ["</num>"]
                    for c in word:
                            formattedSentence.append(c)
            else:
                    formattedSentence.append(word.lower())
        array = []
        array.append(self.SOS_token)
        for tok in formattedSentence:
            try:
                    array.append(self.to_index(tok))
            except:
                    #self.add_word(tok.text)
                    #array.append(self.to_index(tok.text))
                    array.append(self.to_index("new_word"))
        array.append(self.EOS_token)
        if padding:
            for i in range(len(array),self.sentence_trim):
                    array.append(self.PAD_token)
            return array[:self.sentence_trim]
        else:
            return array