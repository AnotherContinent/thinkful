from flask import Flask, render_template

app = Flask(__name__)

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
  first3 = first[:3]
  last2 = last[:2]
  return "Your Jedi name is {}{}".format(first3, last2)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)