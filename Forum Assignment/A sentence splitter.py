#import textblob
sentences = "Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones jr. thanks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
#a = textblob.TextBlob(sentences)
#b = a.sentences
#print(b)

punc = ['.', '!', '?']
word = ''
for a in range (len(sentences)-1):
    if sentences[a] in punc:
        if sentences[a-2] == "M" and sentences[a-1] == 'r':
            print(sentences[a], end='')
        elif type(sentences[a+1]) is int:
            print(sentences[a], end='')
        elif sentences[a+1] is not ' ':
            print(sentences[a], end='')
        elif sentences[a+1] is ' ' and ord(sentences[a+2]) > 96:
            print(sentences[a], end='')
        else:
            print(sentences[a])
    else:
        print(sentences[a], end='')