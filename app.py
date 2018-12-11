from flask import *

app = Flask(__name__)


@app.route('/medselection')
def medselection():
    return render_template("Alex/medselection.html")

@app.route("/medList")
def medList():
    return render_template("Alex/medList.html")


if __name__ == '__app__':
    app.run()



#asd

