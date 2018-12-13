from flask import *
from persistence1 import *
from persistence import *
import functools
from medication import *
from datetime import datetime

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/scheme2')
def base():
    return render_template('JinAnn/scheme2.html')


@app.route('/scheme')
def scheme():
    return render_template('JinAnn/scheme.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/contacthelp")
def contacthelp():
    return render_template('contacthelp.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/medselection", methods=['GET', 'POST'])
def medForm():
    med_form = medForm()
    if request.method =='GET':
        return render_template('medselection.html', med_form=med_form)
    elif request.method =='POST':
        return render_template('medList.html', med_form=med_form)

@app.route('/medList')
def medList():
    return render_template("medList.html")

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view

@app.route('/init')
def init():
    init_db()
    return 'db initialised'

@app.route('/')
def index():
    if 'id' in session:
        posts = get_blogs()
        return render_template('index.html', posts = posts)
    else:
        return render_template('login.html')


@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('index'))
        flash(error)
    return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html')

@app.route('/<string:id>/update', methods=('GET', 'POST'))
def update(id):
    post = get_blog(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            update_blog(post)
            return redirect(url_for('index'))

    return render_template('update.html', post=post)

@app.route('/<string:id>/delete', methods=('GET', 'POST'))
def delete(id):
    delete_blog(id)
    posts = get_blogs()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            create_blog(session['user_name'], title, body)
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/gameSelection')
def goToGameSelection():#step1
    return render_template("ace/game_Selection.html")

@app.route('/calculatorGame')#step2
def goToCalculator():
    delete_All()
    save_The_Time(180)

    return render_template("ace/calculatorGame.html")
@app.route('/calculatorGame/Easy', methods=('GET', 'POST'))
def chooseEasy():
    #cal=diffcuity("calculatorGame",diff)

    E1 = 1
    E2 = 25
    tomtom = test_print()
    total = len(tomtom)

    howManyQ=11 ############################ how many Q but if choose 5 need plus 1
    if request.method == 'POST':
        UAns = request.form['userA']
        countingdown = request.form['countdown']
        error = None
       # if not UAns:
         #   error = 'Number is required.'
        if error is not None:
            flash(error)
        else:

            store(E1, E2)
            save_The_Time(int(countingdown))
            storeUserAnswer(UAns)# store all the 10 + 10
        return redirect(url_for('chooseEasy'))

#hello3
    if total == 0:
        store(E1, E2)


    currentQ = total + 1
    Q1=giveE1()
    Q2=giveE2()
    taketime=give_Back_Time()
    Signs = give_Sign()
    checkIfCorrect=checkrange()


    return render_template("ace/CalGameStart.html",total=total,currentQ=currentQ,tomtom=tomtom,Q1=Q1,Q2=Q2
                           ,checkIfCorrect=checkIfCorrect,howManyQ=howManyQ,Signs=Signs,taketime=taketime)



@app.route('/calculatorGame/Normal', methods=('GET', 'POST'))
def chooseNormal():

    #cal=diffcuity("calculatorGame",diff)
    E1 = 25
    E2 = 50

    tomtom = test_print()
    total = len(tomtom)
    howManyQ =16  ############################ how many Q but if choose 5 need plus 1
    if request.method == 'POST':
        UAns = request.form['userA']
        countingdown = request.form['countdown']
        error = None
        # if not UAns:
        #   error = 'Number is required.'
        if error is not None:
            flash(error)
        else:

            store(E1, E2)
            save_The_Time(int(countingdown))
            storeUserAnswer(UAns)  # store all the 10 + 10
        return redirect(url_for('chooseNormal'))

    if total == 0:
        store(E1, E2)
    currentQ = total + 1
    taketime=give_Back_Time()
    Q1 = giveE1()
    Q2 = giveE2()
    Signs = give_Sign()
    checkIfCorrect = checkrange()

    return render_template("ace/CalGameStart.html", total=total, currentQ=currentQ, tomtom=tomtom, Q1=Q1, Q2=Q2,
                           checkIfCorrect=checkIfCorrect, howManyQ=howManyQ,taketime=taketime,Signs=Signs)


@app.route('/calculatorGame/Hard', methods=('GET', 'POST'))
def chooseHard():

    #cal=diffcuity("calculatorGame",diff)
    E1 = 50
    E2 = 100
    taketime = give_Back_Time()
    tomtom = test_print()
    total = len(tomtom)
    howManyQ = 21  ############################ how many Q but if choose 5 need plus 1
    if request.method == 'POST':
        UAns = request.form['userA']
        countingdown = request.form['countdown']
        error = None
        # if not UAns:
        #   error = 'Number is required.'
        if error is not None:
            flash(error)
        else:

            store(E1, E2)
            save_The_Time(int(countingdown))
            storeUserAnswer(UAns)  # store all the 10 + 10
        return redirect(url_for('chooseHard'))

    if total == 0:
        store(E1, E2)
    currentQ = total + 1

    Q1 = giveE1()
    Q2 = giveE2()
    Signs = give_Sign()
    checkIfCorrect = checkrange()

    return render_template("ace/CalGameStart.html", total=total, currentQ=currentQ, tomtom=tomtom, Q1=Q1, Q2=Q2,
                           checkIfCorrect=checkIfCorrect, howManyQ=howManyQ,taketime=taketime,Signs=Signs)

@app.route("/calculatorGame/Challage" , methods=('GET', 'POST'))
def challage_All():

    if request.method == 'POST':
        UStart = request.form['Start']
        UEnd=request.form['End']
        URange=request.form['Range']
        UTime=request.form['Time']

        error = None

        if error is not None:
            flash(error)
        else:
            settingChallage(UStart,UEnd,URange,UTime)
            return redirect(url_for('challageStart'))

        # if not UAns:
    return render_template("ace/Challage.html")

@app.route("/calculatorGame/Challage/GO" , methods=('GET', 'POST'))
def challageStart():

    tomtom = test_print()
    total = len(tomtom)

    if request.method == 'POST':
        UAns = request.form['userA']
        countingdown = request.form['countdown']
        error = None
        # if not UAns:
        #   error = 'Number is required.'
        if error is not None:
            flash(error)
        else:
            ChallageStartInP()
            save_The_Time(int(countingdown))
            storeUserAnswer(UAns)  # store all the 10 + 10
        return redirect(url_for('challageStart'))
    range=""

    if total==0:
        ChallageStartInP()
    currentQ = total + 1


    Q1 = giveE1()
    Q2 = giveE2()
    Signs=give_Sign()
    taketime = give_Back_Time()
    howManyQ=int(get_NumberOfQ())+1
    checkIfCorrect = checkrange()

    return render_template("ace/CalGameStart.html", total=total, currentQ=currentQ, tomtom=tomtom, Q1=Q1, Q2=Q2,
                           checkIfCorrect=checkIfCorrect, howManyQ=howManyQ,Signs=Signs,taketime=taketime)

@app.route("/calculatorGame/test/results")
def results():
    #testIfITWorks=test_print()
    if len(test_print())!=0:
        tomtom=test_print()
        checkIfCorrect = checkrange()
        delete_All()
        return render_template( "ace/maybe_combine.html",tomtom=tomtom,checkIfCorrect=checkIfCorrect)
    else:
        return render_template("ace/maybe_combine.html")

if __name__ == '__main__':
    app.run()



