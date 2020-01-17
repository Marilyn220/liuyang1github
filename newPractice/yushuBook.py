from newPractice.http import HTTP

class YuShuBook:
    isbn_url='http://t.yushu.im/v2/book/isbn/{}'
    keyword_url='http://t.yushu.im/v2/book/search?q={}&count{}&start={}'

    @classmethod
    def serch_by_isbn(self,isbn):
        url=YuShuBook.isbn_url.format(isbn)
        result =HTTP.get(url)
        return result

    @classmethod
    def search_by_keyworld(self,keyword):
        url = YuShuBook.isbn_url.format(keyword)
        result = HTTP.get(url)
        return result