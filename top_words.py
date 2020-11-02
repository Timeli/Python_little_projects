import string

punctuation = string.punctuation

text_old = open('your text.txt')
text_old = str(text_old.read()).lower()


def top_words(text, numb):
    """ Finds the top most used words in the
        text and displays their number.
        text: lowercase text without punctuation
        numb: number of most popular words
    """
    text_new = ''
    for i in text:
        if i in punctuation:
            i = ' '
        text_new += i
    text_new = text_new.split()

    A = {}
    count = 1
    for i in text_new:
        if i in A:
            count = A[i]
            A[i] = count + 1
            count = 1
        else:
            A[i] = count

    top_values = sorted(A.values())[-numb:]
    for key, value in A.items():
        if value in top_values:
            print(key, value, sep=': ')


top_words(text_old, 5)