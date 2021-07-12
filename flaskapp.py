import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from flask import Flask, render_template, request 

hscores=pd.read_csv("student_scores.csv")

X=hscores['Hours']
Y=hscores['Scores']

X_train, X_test, Y_train, Y_test = train_test_split(X.values.reshape(-1,1), Y)

hmarks_model=LinearRegression().fit(X_train,Y_train)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",prev=1.0)

@app.route("/predict",methods=["POST"])
def predict():
    number=float(request.form["hours"])

    prediction = hmarks_model.predict([[number]])[0]

    if(prediction>100):
        prediction=100
    if(prediction<0):
        prediction=0
    
    prediction = "The predicted score for %.1f hours of studying is %.2f"%(number,prediction)

    return render_template("index.html",prev=number,score=prediction)

if(__name__=="__main__"):
    app.run(debug=True,port=4000,host="localhost")