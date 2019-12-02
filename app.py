from flask import Flask, render_template, redirect, request
from time import sleep
from random import randint, seed


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/fileReport')
def fileReport():
    return render_template('fileReport.html')

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
                    return render_template('homepage.html')        
        return redirect('/signInError')
    return render_template('homepage.html', errMsg=errMsg)

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
