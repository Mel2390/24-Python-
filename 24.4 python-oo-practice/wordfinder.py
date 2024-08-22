"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """A class to read words from a file and return a random word."""
    
    def __init__(self, filepath):
        """Initialize with the path to a file and read words from it.
        
        Args:
            filepath (str): The path to the file containing words.
        """
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")

    def read_words(self, filepath):
        """Read words from the file and return them as a list.
        
        Args:
            filepath (str): The path to the file containing words.
        
        Returns:
            list: A list of words read from the file.
        """
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """Return a random word from the list of words.
        
        Returns:
            str: A random word from the list.
        """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """A subclass of WordFinder that handles comments and blank lines."""

    def read_words(self, filepath):
        """Load words from the file, ignoring blank lines and lines starting with '#'."""
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]
