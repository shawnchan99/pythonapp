from flask import Flask
app = Flask(__name__)

# update version of Flask requires Werkzeug==2.2.2
# specify the required version of Werkzeng to be 2.2.2 in requirements.txt

@app.route("/")
def hello():
   return "Hello World!"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
