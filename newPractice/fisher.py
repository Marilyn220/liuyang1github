from flask import Flask

from newPractice import helper

app =Flask(__name__)

__author__='Marilyn'
app.config.from_object('config')
@app.route('/book/search/<q>/<page>')
def search(q,page):
    """
        q:普通关键字 isbn
        page
    """
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9的数字组成，含有一些’_'
    isbn_or_key=helper.is_isbn_or_key(q)

    pass
#app.add_url_rule('/hello',view_func=hello)
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)