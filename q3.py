def wordCount(t):
    """
    fetch data from textfile.txt and returns a dictonary where the keys are unique words and values are lists of line number where each word is found
    """
    word_occurrences = {}  # Dictonary to stora word occurance
    
    with open(t, 'r') as file: #opening file to read
        for line_num, line in enumerate(file, start=1): # iterate over each line in file
            words = line.strip().split() #splitting the line into words
            for word in words:
                if word not in word_occurrences: #checking if the word is not already in the dictonary
                    word_occurrences[word] = [line_num] # addinf word with line number
                else:
                    word_occurrences[word].append(line_num)

    return word_occurrences

result = wordCount('textfile.txt')
print(result)
