
class Genre(Enum):
    pass

def find_book():
    book = input("Please provide book address: \n")


def count_words(book): 
    with open(book) as f:
        for line in f:
            line = line.strip()
            line = line.lower()
            return len(line.split(" "))

def recurrence_words(book):
    d = {}
    with open(book) as f:
        for line in f:
            line = line.strip()
            line = line.lower()
            words = line.split(" ")
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                d[word] = 1
    return d

def reading_time_estimate():
    pass



