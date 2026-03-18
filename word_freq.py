#
# Word frequency.
# Your name:
#  - <Daníel Darri Ragnarsson>
#

from my_dict import MyDict

def read_in_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        return text

def word_frequency_alphabetical_pydict(text):
    """
    Returns a list of (word, frequency) tuples ordered alphabetically, with all words translated to lowercase,
    e.g., given the text "I am so so happy happy Happy" it returns [('am', 1), ('happy', 3), ('i', 1), ('so', 2)].
    Should be implemented using Python's build-in dictionary.
    :param text: text to process
    :return: list of word frequencies
    """
    freq = {}
    for word in text.lower().split():
        word = ''.join(c for c in word if c.isalpha())
        if word:
            freq[word] = freq.get(word, 0) + 1
    return sorted(freq.items())

def word_frequency_alphabetical_mydict(text):
    """
    Returns a list of (word, frequency) tuples ordered alphabetically, with all words translated to lowercase,
    e.g., given the text "I am so so happy happy Happy" it returns [('am', 1), ('happy', 3), ('i', 1), ('so', 2)].
    Should be implemented using your dictionary implementation (MyDict).
    :param text: text to process
    :return: list of word frequencies
    """
    freq = MyDict()
    for word in text.lower().split():
        word = ''.join(c for c in word if c.isalpha())
        if word:
            freq[word] = freq.get(word, 0) + 1
    
    result = []
    for key in freq:
        result.append((key, freq[key]))
    return result


if __name__ == "__main__":
    text = read_in_text('data/word1.txt')
    l_py = word_frequency_alphabetical_pydict(text)
    print(l_py)
    l_my = word_frequency_alphabetical_mydict(text)
    print(l_my)
    if l_py == l_my:
        print("Yes!")
    else:
        print("No!")
