from textblob import TextBlob as tb

text = tb("Because robots are people too i love you")
print(text)
print(text.sentiment)
