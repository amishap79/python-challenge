import re




sentence_word_count_list = []
number_of_words_in_sentence = 0
number_of_words_in_paragraph = 0
sentence_count = 0
sentence_word_count = 0
average_sentence_length = 0

txtfile = open("raw_data/paragraph_2.txt")
read = txtfile.read()

# find the number of sentences in the paragraph
sentences = re.split("(?<=[.!?]) +",  read)
sentence_count = len(sentences)
print(sentence_count)

# calculate words in a sentence and total words in the paragraph
for sentence in sentences:
    for word in re.findall(r'\w+', sentence):
        number_of_words_in_sentence += 1
        number_of_words_in_paragraph += 1
    sentence_word_count_list.append(number_of_words_in_sentence)
    number_of_words_in_sentence = 0 

print(sentence_word_count_list)

# calculate sum of all words in paragraph
for count in sentence_word_count_list:
    sentence_word_count += count

# calculate average number of word in a sentence
average_sentence_length = sentence_word_count/len(sentence_word_count_list)
print(average_sentence_length)


print(f'Paragraph Analysis')
print(f'-----------------------------')
print(f'Approximate Word Count: {number_of_words_in_paragraph} ')
print(f'Approximate Sentence Count: {sentence_count}')
print(f'')
print(f'Average Sentence Length: {average_sentence_length}')
