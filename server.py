from flask import Flask
from trie import *
app = Flask(__name__)


@app.route('/add/<keyword>')
def add_keyword(keyword):
    add(keyword)
    return {"status": "Operation successful..."}


@app.route('/remove/<keyword>')
def remove_keyword(keyword):
    if not remove(keyword, 0, None):
        return {"status": "Keyword not found..."}
    return {"status": "Operation successful..."}


@app.route('/suggest/<keyword>')
def suggest_keyword(keyword):
    suggest(keyword, 0, '', None)
    return {"status": '\n'.join(suggestions)}


@app.route('/display')
def show():
    return {"status": display()}


@app.route('/check/<keyword>')
def check_keyword(keyword):
    if check(keyword, 0, None):
        return {"status": f"True, keyword \"{keyword}\" is stored in trie."}
    return {"status": f"False, keyword \"{keyword}\" is not stored in trie."}


if __name__ == '__main__':
    app.run(threaded=True)
