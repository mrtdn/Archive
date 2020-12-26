sentence = 'The quick brown fox jumps over the lazy dog'
piecesList = sentence.split()
filteredList = [word for word in piecesList if word.casefold() != 'the']
lengthOfWords = [len(word) for word in filteredList]
print(lengthOfWords)