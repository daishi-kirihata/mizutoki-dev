import string
import pandas

def filterByAsciiRate(text, threshold=0.9):
    asciiLetters = set(string.printable)
    rate = sum(c in asciiLetters for c in text) / len (text)
    return rate <= threshold

def loadDataset(fileName, n=5000, state=6):
    tsvFile = pandas.read_csv(fileName, sep='\t')

    isJP = tsvFile.review_body.apply(filterByAsciiRate)
    tsvFile = tsvFile[isJP]

    tsvFile = tsvFile.sample(frac=1, random_state=state)
    grouped = tsvFile.groupby('star_rating')
    tsvFile = grouped.head(n=n)
    return tsvFile.review_body.values, tsvFile.star_rating.values
