from flask import *
from persistence import *
app = Flask(__name__)


@app.route('/')
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
