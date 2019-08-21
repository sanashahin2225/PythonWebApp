from flask import Flask, request
from flask import render_template
import json
import requests
import time

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
   return render_template('index.html')


@app.route('/login',methods=["GET","POST"])
def login():
	params = (
	    ('GitHubURL', request.form["GitHubURL"]),
	    ('GitHubBranch', request.form["GitHubBranch"]),
	    ('command', request.form["command"])
	)
	
	response = requests.post('http://3.81.112.177:8080/job/ParameterizedJob/buildWithParameters', params=params, auth=('sanashahin2225', '117a2003d333a244d05d504a90791089fc'))
	time.sleep(15)
	response1 = requests.get('http://3.81.112.177:8080/job/ParameterizedJob/lastBuild/api/json', auth=('sanashahin2225', '117a2003d333a244d05d504a90791089fc'))
	data = json.loads(response1.text)
	id=data['id']

	if data['result'] == "SUCCESS":
		return render_template('output.html',output="Successfully Build",id=id)
	else:
		return render_template('output.html',output="Failure")

if __name__ == '__main__':
    app.run(debug=True)
