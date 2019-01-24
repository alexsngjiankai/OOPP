from flask import *
from persistence1 import *
from persistence import *
import functools
from alexpersistance import *
from medication import *
#from datetime import datetime
#rr
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)
#tt
@app.route('/schemeform',  methods=('GET', 'POST'))
def schemeform():
    if request.method == 'POST':
        age = int(request.form['age'])
        income = int(request.form['income'])

        return render_template("JinAnn/schemeform.html", age=age, income=income)

    age =0
    income=0
    return render_template('JinAnn/schemeform.html', age=age, income=income)


@app.route('/appointment', methods=('GET', 'POST'))
def appointment():
    if request.method == 'POST':
        location  = str(request.form['location'])
        date = str(request.form['date'])
        time = str(request.form['time'])
        reason = str(request.form['reason'])
        referral = appointment.querySelector('input[name="referral"]:checked').value
        return render_template("JinAnn/AppointmentList.html", )

    return render_template('JinAnn/Appointment.html')


@app.route('/appointmentlist')
def appointmentstorage():



    return render_template('JinAnn/AppointmentList.html')

@app.route('/scheme')
def scheme():
    return render_template('JinAnn/scheme.html')
@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/contacthelp")
def contacthelp():
    return render_template('contacthelp.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')




@app.route("/medselection", methods=('GET','POST'))
def medselection():
    if request.method == 'POST':
        user=session["user_name"]
        name = str(request.form['medname'])
        amount = str(request.form['medamount'])
        description = str(request.form['MedDescription'])
        add_medinfo(user, name, amount, description)
        return redirect(url_for("medList"))
    return render_template("medselection.html")

@app.route('/medList')
def medList():
    user=session["user_name"]
    list_med=return_list_med(user)
    return render_template('medList.html', list_med=list_med)




@app.route('/tester')
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
        return render_template('homepage.html')
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


@app.route('/CalculationGame')#step2
def goToCalculator():
    delete_All()
    save_The_Time(180)
    Store_game_name("Cal")
    return render_template("ace/calculatorGame.html")

@app.route('/Game/Easy', methods=('GET', 'POST'))
def chooseEasy():



        if give_App_Name()=="Cal":
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

                    store(E1, E2,"Easy")
                    save_The_Time(int(countingdown))
                    storeUserAnswer(UAns)# store all the 10 + 10
                return redirect(url_for('chooseEasy'))

            if total == 0:
                store(E1, E2,"Easy")
            currentQ = total + 1
            Q1=giveE1()
            Q2=giveE2()
            taketime=give_Back_Time()
            Signs = give_Sign()
            checkIfCorrect=checkrange()
            whichgame=give_App_Name()

            return render_template("ace/CalGameStart.html",total=total,currentQ=currentQ,tomtom=tomtom,Q1=Q1,Q2=Q2
                                   ,checkIfCorrect=checkIfCorrect,howManyQ=howManyQ,Signs=Signs,taketime=taketime,whichgame=whichgame)

        #guessing game ==================================================
        elif give_App_Name()=="Guess":


            whichgame=give_App_Name()
            diff = 'Easy'
            generate_Guess(1,99,diff)
            question=send_guess_num()
            timer=10
            totalQ=5
            current_list_now =send_guess_list_amount()
            if request.method == 'POST':
                count=0
                testing_list=[]

                for i in range(totalQ):
                    test=request.form[str(count)]
                    testing_list.append(test)
                    count+=1



                error = None
               # if not UAns:
                 #   error = 'Number is required.'
                if error is not None:
                    flash(error)
                else:

                    store_answer(testing_list)

                    return redirect(url_for('results'))


            return render_template("ace/CalGameStart.html",whichgame=whichgame,question=question,timer=timer,totalQ=totalQ,current_list_now=current_list_now,diff=diff)


@app.route('/Game/Normal', methods=('GET', 'POST'))
def chooseNormal():
    if give_App_Name() == "Cal":
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

                store(E1, E2, "Normal")
                save_The_Time(int(countingdown))
                storeUserAnswer(UAns)  # store all the 10 + 10
            return redirect(url_for('chooseNormal'))

        if total == 0:
            store(E1, E2, "Normal")
        currentQ = total + 1
        taketime=give_Back_Time()
        Q1 = giveE1()
        Q2 = giveE2()
        Signs = give_Sign()
        checkIfCorrect = checkrange()
        whichgame = give_App_Name()
        return render_template("ace/CalGameStart.html", total=total, currentQ=currentQ, tomtom=tomtom, Q1=Q1, Q2=Q2,
                               checkIfCorrect=checkIfCorrect, howManyQ=howManyQ,taketime=taketime,Signs=Signs,whichgame=whichgame)

    elif give_App_Name() == "Guess":
        whichgame = give_App_Name()
        diff = 'Normal'
        generate_Guess(1, 99,diff)
        question = send_guess_num()
        timer = 10
        totalQ = 8
        current_list_now = send_guess_list_amount()
        if request.method == 'POST':
            count = 0
            testing_list = []

            for i in range(totalQ):
                test = request.form[str(count)]
                testing_list.append(test)
                count += 1

            error = None
            # if not UAns:
            #   error = 'Number is required.'
            if error is not None:
                flash(error)
            else:

                store_answer(testing_list)


                return redirect(url_for('results'))

        return render_template("ace/CalGameStart.html", whichgame=whichgame, question=question, timer=timer,
                               totalQ=totalQ, current_list_now=current_list_now,diff=diff)

@app.route('/Game/Hard', methods=('GET', 'POST'))
def chooseHard():
    if give_App_Name() == "Cal":
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

                store(E1, E2, "Hard")
                save_The_Time(int(countingdown))
                storeUserAnswer(UAns)  # store all the 10 + 10
            return redirect(url_for('chooseHard'))

        if total == 0:
            store(E1, E2, "Hard")
        currentQ = total + 1

        Q1 = giveE1()
        Q2 = giveE2()
        Signs = give_Sign()
        checkIfCorrect = checkrange()
        whichgame = give_App_Name()
        return render_template("ace/CalGameStart.html", total=total, currentQ=currentQ, tomtom=tomtom, Q1=Q1, Q2=Q2,
                               checkIfCorrect=checkIfCorrect, howManyQ=howManyQ,taketime=taketime,Signs=Signs,whichgame=whichgame)

    elif give_App_Name() == "Guess":
        whichgame = give_App_Name()
        diff='Hard'
        generate_Guess(1, 99,diff)
        question = send_guess_num()
        timer = 5
        totalQ = 10
        current_list_now = send_guess_list_amount()
        if request.method == 'POST':
            count = 0
            testing_list = []

            for i in range(totalQ):
                test = request.form[str(count)]
                testing_list.append(test)
                count += 1

            error = None
            # if not UAns:
            #   error = 'Number is required.'
            if error is not None:
                flash(error)
            else:

                store_answer(testing_list)


                return redirect(url_for('results'))

        return render_template("ace/CalGameStart.html", whichgame=whichgame, question=question, timer=timer,
                               totalQ=totalQ, current_list_now=current_list_now,diff=diff)

@app.route("/Game/Challage" , methods=('GET', 'POST'))
def challage_All():
    app_name=give_App_Name()
    if give_App_Name()=="Cal":
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
                return redirect(url_for('StartingChallenge'))

            # if not UAns:



        return render_template("ace/Challage.html",app_name=app_name)
    elif give_App_Name()=="Guess":
        if request.method == "POST":
            UStart = request.form['Start']
            UEnd = request.form['End']
            URange = request.form['Range']
            UTime = request.form['Time']

            error = None

            if error is not None:
                flash(error)
            else:
                settingChallage(UStart, UEnd, URange, UTime)
                return redirect(url_for('StartingChallenge'))



        return render_template("ace/Challage.html",app_name=app_name)

@app.route("/Game/Challenge/running" , methods=('GET', 'POST'))
def challageStart():
    if give_App_Name()=="Cal":
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


        if total==0:
            ChallageStartInP()
        currentQ = total + 1


        Q1 = giveE1()
        Q2 = giveE2()
        Signs=give_Sign()
        taketime = give_Back_Time()
        howManyQ=int(get_NumberOfQ())+1
        checkIfCorrect = checkrange()
        whichgame=give_App_Name()

        return render_template("ace/CalGameStart.html", total=total, currentQ=currentQ, tomtom=tomtom, Q1=Q1, Q2=Q2,
                               checkIfCorrect=checkIfCorrect, howManyQ=howManyQ,Signs=Signs,taketime=taketime,whichgame=whichgame)
    elif give_App_Name()=="Guess":
        whichgame = give_App_Name()
        start_challage_guess()
        question = send_guess_num()
        timer = give_back_time_guess()
        totalQ = int(give_back_range_guess())
        current_list_now = send_guess_list_amount()
        diff="Challange"
        if request.method == 'POST':
            count = 0
            testing_list = []

            for i in range(totalQ):
                test = request.form[str(count)]
                testing_list.append(test)
                count += 1

            error = None
            # if not UAns:
            #   error = 'Number is required.'
            if error is not None:
                flash(error)
            else:

                store_answer(testing_list)

                return redirect(url_for('results'))

            ount = 0
            testing_list = []

            for i in range(totalQ):
                test = request.form[str(count)]
                testing_list.append(test)
                count += 1

            error = None
            # if not UAns:
            #   error = 'Number is required.'
            if error is not None:
                flash(error)
            else:

                store_answer(testing_list)

                return redirect(url_for('results'))

        return render_template("ace/CalGameStart.html", whichgame=whichgame, question=question, timer=timer,
                               totalQ=totalQ, current_list_now=current_list_now,diff=diff)


@app.route("/Game/results")
def results():
    #testIfITWorks=test_print()
    if give_App_Name()=="Cal":
        if len(test_print())!=0:
            tomtom=test_print()
            checkIfCorrect = checkrange()
            id=session["user_name"]
            App_name=give_App_Name()
            StoreHistory(id)
            delete_All()
            return render_template( "ace/maybe_combine.html",tomtom=tomtom,checkIfCorrect=checkIfCorrect,App_name=App_name)

        else:
            return render_template("ace/maybe_combine.html")
    elif give_App_Name() == "Guess":
        id=session["user_name"]

        App_name=give_App_Name()
        tomtom = test_print()

        storeGuessHistory(id)
        return render_template("ace/maybe_combine.html",tomtom=tomtom,App_name=App_name)



@app.route("/History")
def history():
    id = session["user_name"]

    history_cal=give_history_cal(id,"Cal")

    history_Guess=give_history_cal(id,"Guess")

    return render_template("ace/History.html",history_cal=history_cal,history_Guess=history_Guess)

@app.route("/Guess_The_Number")
def GotoGuess():
    delete_All()
    Store_game_name("Guess")
    return render_template("ace/Guess_The_Number.html")



@app.route("/startingEasy")
def StartingEasy():
    App_name = give_App_Name()

    return render_template("Ace/StartEasyButton.html",App_name=App_name)

@app.route("/startingNormal")
def StartingNormal():
    App_name = give_App_Name()

    return render_template("Ace/NormalStartButton.html",App_name=App_name)

@app.route("/startingHard")
def StartingHard():
    App_name = give_App_Name()

    return render_template("Ace/HardStartButtton.html",App_name=App_name)

@app.route("/startingChallenge")
def StartingChallenge():
    if give_App_Name() =="Cal":
        App_name = give_App_Name()

        #need add a lot more /// no statics
        taketime = give_Back_Time()
        howManyQ = int(get_NumberOfQ())
        return render_template("Ace/ChallengeStartButton.html",App_name=App_name,taketime=taketime,howManyQ=howManyQ)

    elif give_App_Name()=="Guess":
        App_name = give_App_Name()
        timer = give_back_time_guess()
        totalQ = int(give_back_range_guess())
        return render_template("Ace/ChallengeStartButton.html", App_name=App_name, timer=timer,totalQ=totalQ)


#=======================================================================================================================testting

@app.route("/testing" , methods=('GET', 'POST'))
def testingLookAtPics():
    if request.method == 'POST':
        Img = request.form['sendingImg']
        sendImgToTem(Img)
        return redirect(url_for('testtest'))


    return render_template("ace/test.html")

@app.route("/seetest")
def testtest():
    testshow=testShowImg()
    return render_template("ace/test2.html" , testshow=testshow)
#=====================================================================================================================testing ended
#End ace
if __name__ == '__main__':
    app.run()



