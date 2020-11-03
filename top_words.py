import string

#   get punctuation list
punctuation = string.punctuation

text_into = open('your text.txt')
#   convert text to string and lowercase
text_old = str(text_into.read()).lower()
text_into.close()


def top_words(text, numb):
    """ Finds the top most used words in the
        text and displays their number.
        text: lowercase text without punctuation
        numb: number of most popular words
    """
    #   create a new list replacing punctuation with a space
    text_new = ''
    for i in text:
        if i in punctuation:
            i = ' '
        text_new += i
    text_new = text_new.split()
    #   create a dict where key is word and value is number
    A = {}
    count = 1
    for i in text_new:
        if i in A:
            count = A[i]
            A[i] = count + 1
            count = 1
        else:
            A[i] = count
    #   get a list of the most popular values in the dict
    top_values = sorted(A.values())[-numb:]
    for key, value in A.items():
        if value in top_values:
            print(key, value, sep=': ')


top_words(text_old, 5)