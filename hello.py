from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def source():
	html = 'Hello World!'
	return html

def application():
	answer = logic("Example Input")
	return answer

if __name__ == "__main__":
	app.run()