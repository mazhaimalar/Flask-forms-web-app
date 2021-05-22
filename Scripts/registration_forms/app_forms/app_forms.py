
from flask import Flask
from flask import render_template,redirect,url_for
from flask import request
import csv
from csv import reader
import pandas as pd
import tablib
import os
import webbrowser

app = Flask(__name__)




@app.route('/')
def form():
    return render_template('forms.html')

@app.route("/forms", methods = ['GET','POST'])
def formsubmittion():
    
    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        gender = request.form['gender']
        city = request.form['city']
        state = request.form['state']
        email_id = request.form['email_id']
        qualification = request.form['qualification']
        stream = request.form['stream']

        fieldnames = ['student_id', 'student_name','gender','city','state','email_id','qualification','stream']

        with open('nameList.csv','a', newline='') as inFile:
             writer = csv.DictWriter(inFile, fieldnames=fieldnames)
             writer.writerow({'student_id': student_id, 'student_name': student_name,'gender':gender,'city':city,'state':state,'email_id':email_id,'qualification':qualification,'stream':stream})
             return redirect(url_for('form'))

@app.route("/search/")
def search():
     return render_template("studentsearch.html")

@app.route("/studentid/",methods=['POST','GET'])
def studentid():
    
    
    if request.method == 'POST':
         stuSearch=request.form.get('stuSearch')
         
    with open('nameList.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
           csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
           for row in csv_reader:
               if row[0]==stuSearch:
                   stocklist=[[i for i in row]]
        # row variable is a list that represents a row in csv
           print(stocklist)
           return render_template('view.html', stocklist=stocklist)



                
                               


      

@app.route("/display/")
def display():
     data = pd.read_csv('nameList.csv')
     stocklist = list(data.values)
     return render_template('view.html', stocklist=stocklist)
    
   
    



if __name__ == "__main__":
    app.run()

       








