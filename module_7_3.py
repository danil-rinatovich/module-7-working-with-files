class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        file = 'test_file.txt'
        char_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        list_ = []

        with open(file, encoding='utf-8') as self.file_names:
            for line in self.file_names:
                for ch in char_:
                    line = line.replace(ch, '')
                text = line.lower().split()
                list_.extend(text)
                all_words[file] = list_
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_[name] = words.index(word.lower()) + 1
        return dict_

    def count(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_[name] = words.count(word.lower())
        return dict_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))