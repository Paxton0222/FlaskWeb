from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get/<name>',methods=['GET'])
def getname(name):
    return render_template('get.html',name=name)