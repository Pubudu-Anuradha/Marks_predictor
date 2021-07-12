# Marks_predictor
A program to predict the marks of a student according to the number of hours spent studying using ML.

## Program structure
- The colab notebook *PredictMarks.ipynb* and *predictmarks.py* demonstrates the model used for prediction.
- *student_scores.csv* containes the values used to train the linear regression model used in the program.
- *flaskapp.py* and the files in the directories **static** and **templates** are used for a flask webapp that predicts marks according to user input.

## Setting up Flask Webapp
After the following prerequisites are met, clone this repository and run the file flaskapp.py 
Use a webbrowser and navigate to [http://localhost:4000/](http://localhost:4000/) to use the app.

### Prereqisites for Flask webapp
The program was made with [Python 3.9.6](https://www.python.org/downloads).
The following pacakges need to be installed
- Pandas
- Scikit Learn
- Flask
Run the following command in a terminal to install them
'''
pip install pandas sklearn flask
'''