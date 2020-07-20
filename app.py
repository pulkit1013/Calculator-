from flask import Flask,render_template,request
import re

#Declare the app

app=Flask(__name__)

#Start an app route
@app.route('/')

#Declare the main function
def main():
    return render_template('app.html')

#Form submission URL
@app.route('/calc', methods=['POST',"GET"])
def send(sum=sum):
    if request.method=='POST':
        #Start Pulling DATA from form input
        value1=request.form['value1']
        value2=request.form['value2']
        operation=request.form['operation']

        #Calculation
        if operation=='+':
            sum=float(value1)+float(value2)
            return render_template('app.html',sum=sum)

        elif operation=='-':
            sum=float(value1)-float(value2)
            return render_template('app.html',sum=sum)

        elif operation=='*':
            sum=float(value1)*float(value2)
            return render_template('app.html',sum=sum)

        else:
            return render_template('app.html')

    else:
        
        value1=request.args['value1']
        value2=request.args['value2']
        # operation=request.args['operation']
        url=request.url
        operation=url[-1]

        #Calculation
        if operation=='-':
            sum=float(value1) - float(value2)
            return render_template('app.html',sum=sum)

        elif operation=='+':
            sum=float(value1)+float(value2)
            return render_template('app.html',sum=sum)

        elif operation=='*':
            sum=float(value1)*float(value2)
            return render_template('app.html',sum=sum)

        else:
            return render_template('app.html')


