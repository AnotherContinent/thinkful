from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello_world.html', name=name)
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)