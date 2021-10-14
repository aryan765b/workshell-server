from flask import Flask,jsonify
import time as t
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/reqa/<string:pswd>')
def reqa(pswd):
	opswd = open("cred","r").read()
	if opswd == pswd:
		return "1"
	else:
		return "0"
@app.route("/run/<string:cmd>")
def run(cmd):
	try:
		result =  os.popen(cmd,"r",1).read().replace("\n","!@#$")
		logs = open("logs.txt","a")
		logs.write(f"\n{'_'*10}\n@cmd: {cmd}\n@result :{result}\n@time :{t.ctime()}\n{'_'*10}\n")
		return jsonify({"status":1,"res":result})
	except:
		return  jsonify({"status":0,"res":"error"})

if __name__ == '__main__':
	app.run(debug=True)
	