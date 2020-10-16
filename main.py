from flask import Flask,render_template,request

app = Flask(__name__)

#test port  9000
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get/<name>/',methods=['GET'])
def getname(name):
    return render_template('get.html',name=name)

@app.route('/request/',methods=['GET']) #用 request 取得使用者的 User-agent 和使用者的真實IP
def requests():
    user_agent = request.headers.get('User-agent')
    user_ip = request.headers.getlist("X-Forwarded-For")[0]
    return "<center><p>Your browser is {}</p><br></br><p>Your IP is :{}</p></center>".format(user_agent,user_ip)