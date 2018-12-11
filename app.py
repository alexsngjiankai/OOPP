from flask import Flask, render_template

app = Flask(__name__)


@app.route('/medselection')
def medselection():
    return render_template("medselection.html")

@app.route("/medList")
def medList():
    return render_template("medList.html")


if __name__ == '__app__':
    app.run()





