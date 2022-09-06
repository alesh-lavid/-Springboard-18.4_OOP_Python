"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:

    def __init__(self, word_file):
        self.word_file = word_file
        self.word_list = self.read_file([])
        self.word_count = self.count_words()

        print(f"{self.word_count} words read")

    def read_file(self, lst):
        """Open and read each line inside a text file then append to class variable list

        Args:
            lst list: Accepts empty list

        Returns:
            list: returns list with each word found within the text file
        """
        file = open(self.word_file)

        for line in file:
            lst.append(line)
        
        file.close()
        return lst

    def count_words(self):
        """Number count each word found in class list (word_list)

        Returns:
            int: returns number of words inside class list (word_list)
        """
        return len(self.word_list)

    def random(self):
        """Returns random word from class list

        Returns:
            str: random word from class list
        """
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Extends WordFinder class with the new ability to parse a file by removing whitespacing and line starting with #

    Args:
        WordFinder (str)
    """
    def __init__(self, word_file):
        super().__init__(word_file)

    def parse_file(self, word_file):
        return [word_file.strip() for word in word_file
                if word.strip() and not word.startswith("#")]
    
