from flask import Flask, render_template, redirect, request


app = Flask(__name__)

@app.route('/')
def signIn():
    return render_template('signIn.html')

@app.route('/signInError')
def signInError():
    errMsg = 1
    return render_template('signIn.html',errMsg=errMsg)

@app.route('/homepage',methods=['POST','GET'])
def homepage():
    users = [('john.doe@noaa.org', 'password'),('volunteer@volunteer.org', '123456'),('professional@professional.org','asdfjkl')]
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        for user in users:
            if user[0] == username:
                if user[1] == password:
                    return render_template('homepage.html')        
        return redirect('/signInError')
    return render_template('homepage.html')

@app.route('/homepage/mySchedule')
def mySchedule():
    return render_template('mySchedule.html')

@app.route('/homepage/eventList')
def eventList():
    return render_template('eventList')

@app.route('/homepage/eventMap')
def eventMap():
    return render_template('eventMap')

@app.route('/logoutSuccess')
def logoutSuccess():
    return render_template('logoutSuccess.html')

@app.route('/portfolio')
def portfolio():
    return render_template('indexOld.html')



if __name__ == '__main__': app.run(debug=True)
