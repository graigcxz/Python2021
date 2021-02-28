# -*- coding:utf-8 -*-

# 10-10：常见单词

filenames = ['A Tale of Two Cities - Charles Dickens.txt',
             'Alice\'s Adventures in Wonderland - Lewis Carroll.txt',
             'Jane Eyre - Charlotte Bronte.txt']

for filename in filenames:
    with open(filename) as file_object:
        contents = file_object.read()
    words = contents.split()
    num_words = len(words)
    number_of_the = contents.lower().count('the')
    ratio = number_of_the / num_words
    print("There are " + str(number_of_the) + " times that 'the' appeared.")
    print("There are " + str(num_words) + " in the file--" + filename + '.')
    print("The ratio of 'the' is {:.2f}%.".format(ratio))
