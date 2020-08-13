pages = []
index = 0

while (index < 5):
    rows = {}

    rows['index'] = index

    word = ""
    if ( index == 0 ):
        word = "cat"
        language = 'en'
    elif ( index == 1 ):
        word = 'gatto'
        language = 'it'
    elif ( index == 2 ):
        word = 'gato'
        language = 'pt'
    elif ( index == 3 ):
        word = 'gato'
        language = 'es'
    elif ( index == 4 ):
        word = 'chat'
        language = 'fr'
    elif ( index == 5 ):
        word = 'dog'
        language = 'en'

    rows['language'] = language
    rows['word'] = word

    pages.append(rows)
    index += 1
print(pages)