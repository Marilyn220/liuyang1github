
__auther__='Marilyn'

def is_isbn_or_key(word):
    if len(word)==13 and word.isdigit():
        isbn_or_key='isbn'
    short_q=word.replace('_','')
    if '_' in word and len(short_q)==10 and short_q.isdigit():
        isbn_or_key='isbn'
