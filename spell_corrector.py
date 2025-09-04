from textblob import TextBlob

def correct_spelling(text):
    blob = TextBlob(text)
    return str(blob.correct())

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Corrected:", correct_spelling(sentence))
