from textblob import TextBlob as tb

text = tb("Because robots are people too i hate you")
print(text)
print(text.sentiment)
print(text.sentiment.polarity)
print(text.sentiment.subjectivity)

text = tb("Because robots are people too i love you")
print(text)
print(text.sentiment)
print(text.sentiment.polarity)
print(text.sentiment.subjectivity)

text = tb("Because robots are people too")
print(text)
print(text.sentiment)
print(text.sentiment.polarity)
print(text.sentiment.subjectivity)
