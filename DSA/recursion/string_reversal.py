def reverse_string(sentence):
    if sentence == '':
        return sentence
    # what is the smallest amount of work I can do in each iteration?
    return reverse_string(sentence[1:]) + sentence[0]

if __name__ == '__main__':
    print(reverse_string('Hello world!'))
