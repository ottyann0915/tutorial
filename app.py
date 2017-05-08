from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # 「templates/index.html」のテンプレートを使う
    # 「message」という変数に"Hello"と代入した状態で、テンプレート内で使う
    return render_template('index.html', message=titles(), mokuji=mokuji())

def titles():
    bs0 =  Main.tester()
    for line in bs0.findAll("title"):
        result = line.get_text()
    return result

def mokuji():
    bs0 = Main.tester()
    for line in bs0.findAll("", {"class":"index-navi-sub-list"}):
        result =  "<p>" + line.get_text() + "</p>"
    result = result.replace("\n", "</p><p>")
    return result

class Main:
    def bs0bj_com(files):
        f = open(files, "rb")
        s = f.read()
        bs0 = BeautifulSoup(s, "lxml")
        return bs0
    
    def tester():
        url = "http://pinky-media.jp/I0006485"
        html = urlopen(url)
        html = html.read()
        bs0 = BeautifulSoup(html, "lxml")
        return bs0

if __name__ == "__main__":
    app.run(debug=True)
