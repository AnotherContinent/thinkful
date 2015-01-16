from flask import Flask, render_template

app = Flask(__name__)

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
  first2 = first[:2]
  last3 = last[:3]
  return "Your Jedi name is {}{}".format(last3, first2)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)