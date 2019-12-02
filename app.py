from flask import Flask, render_template, redirect, request
from time import sleep
from random import randint, seed

reports = [['Brittany B', 'Southport Beach', 'Whale', 'Beached whale, 10 feet from the current water level', 0, ''], ['Chris F', 'Eastport Beach', 'Stingray', 'Stringrapy on the shore, one person has been stung', 2, 'Eastport Stingray'], ['Manda Mandalay', 'Northport Beach', 'Seal', 'Family of seals, people are getting close to the animals', 0, '']]
#last integer in reports 0 = unprocessed, 1 = archived, 2 = in an event, 3 = event completed]

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/fileReport')
def fileReport():
    return render_template('fileReport.html')

@app.route('/reportSuccess',methods=['POST','GET'])
def reportSuccess():
    if request.method == 'POST':
        report = [request.form['name'], request.form['location'], request.form['type'], request.form['description'], 0, '']
        reports.append(report)
    return render_template('reportSuccess.html')

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/signInError')
def signInError():
    errMsg = 1
    return render_template('signIn.html',errMsg=errMsg)

@app.route('/homepage',methods=['POST','GET'])
def homepage(errMsg=0):
    users = [('john.doe@noaa.org', 'password'),('volunteer@volunteer.org', '123456'),('professional@professional.org','asdfjkl')]
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        for user in users:
            if user[0] == username:
                if user[1] == password:
                    if "@noaa.org" in user[0]:
                        return redirect('/homepageNOAA')
                    return render_template('homepage.html')        
        return redirect('/signInError')
    return render_template('homepage.html', errMsg=errMsg)

@app.route('/homepageNOAA')
def homepageNOAA():
    return render_template('homepageNOAA.html')

@app.route('/homepage/mySchedule')
def mySchedule():
    return render_template('mySchedule.html')

@app.route('/homepage/eventList')
def eventList():
    return render_template('eventList.html')

@app.route('/homepage/eventMap')
def eventMap():
    return render_template('eventMap.html')

@app.route('/homepage/settings')
def settings():
    return render_template('settings.html')

@app.route('/logoutSuccess')
def logoutSuccess():
    seed()
    randomTimeout = randint(1,5)
    if randomTimeout%5 == 0:
        sleep(2)
        errMsg = 1
        homepage(errMsg)
    return render_template('logoutSuccess.html')

@app.route('/portfolio')
def portfolio():
    return render_template('indexOld.html')



if __name__ == '__main__': app.run(debug=True)
