""" Parser """


class Parser():

    def __init__(self, sentence=None):
        """ Take a french sentence as parameters.
            Return a keyword.

            sentence              (str ): french sentence only.
            sentence_min_lenght   (int ): min sentence caracters lenght.
            sentence_max_lenght   (int ): max sentence catacters lenght.
            sentence_words        (list): sentence words.
            sentence_words_info   (list): sentence words informations. """

        self.sentence = sentence

        self.sentence_min_lenght = 10
        self.sentence_max_lenght = 100
        self.sentence_words = []
        self.sentence_words_info = []

        self.french_keywords = ["adresse", "trouve", "situe", "est"]
        self.request_keywords = ""

    def sentence_parsing(self):
        """ Start parsing """

        if self.sentence_lenght() is True:
            self.sentence_split()
            self.sentence_words_clean()
            self.sentence_words_analysis()
            self.sentence_keywords()

    def sentence_lenght(self):
        """ Take a self argument "sentence".
            Count the number of sentence caraters.
            Check that the sentence is neither too big nor too small.

            sentence_lenght (int ): lenght of self sentence.
            checking        (bool): Function result. """

        sentence_lenght = len(self.sentence)
        checking = False

        if sentence_lenght < self.sentence_min_lenght:
            checking = False
        elif sentence_lenght > self.sentence_max_lenght:
            checking = False
        else:
            checking = True

        return checking

    def sentence_split(self):
        """ Cut the sentence between each space.
            Fill a list of lists with each sentence words recovered. """

        self.sentence_words = self.sentence.split()

        return self.sentence_words

    def sentence_words_clean(self):
        """ Clean sentence words.
            Retire l'article défini singulier "l'" """

        i = 0
        for word in self.sentence_words:

            article = False
            word_save = []
            word_clean = None

            for caracter in word:

                word_save.append(caracter)

                if caracter == "'":
                    article = True

            if article is True:

                del word_save[0]
                del word_save[0]
                word_clean = "".join(word_save)

                self.sentence_words[i] = word_clean

            i += 1

        return self.sentence_words

    def sentence_words_analysis(self):
        """ Analysis sentence words.
            Get the position of words in sentence.
            Get the lenght of words.
            Mark the words that are uppercase. """

        # Get the position of words in sentence.
        i = 0
        for word in self.sentence_words:

            sentence_word = []

            sentence_word.append(i)
            sentence_word.append(len(word))

            word_caracter_test = word[0].upper()
            uppercase = False

            # Second condition for ponctuation
            if word_caracter_test == word[0] and len(word) > 1:
                if len(word) > 1:
                    uppercase = True

            sentence_word.append(uppercase)
            i += 1

            self.sentence_words_info.append(sentence_word)

        return self.sentence_words_info

    def sentence_keywords(self):
        """ Use self sentence_words_info and sentence_words to get
            the subject of user request. """

        req_keywords = []

        container_start = None
        container_end = None

        # Search if an french_keywords exist in sentence
        i = 0
        for word in self.sentence_words:
            for french_keyword in self.french_keywords:
                if word == french_keyword:
                    container_start = i + 1
                if word == "?":
                    container_end = i

            i += 1

        for word in self.sentence_words[container_start:container_end]:

            req_keywords.append(word)

        self.request_keywords = "%20".join(req_keywords)

        return self.request_keywords
