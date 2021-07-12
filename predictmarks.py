import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hscores=pd.read_csv("student_scores.csv")

print(hscores.head(5))

plt.scatter(data=hscores,x="Hours",y="Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores obtained")
plt.title("Hours studied vs Scores obtained")

plt.show()

X=hscores['Hours']
Y=hscores['Scores']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X.values.reshape(-1,1), Y)

from sklearn.linear_model import LinearRegression
hmarks_model=LinearRegression().fit(X_train,Y_train)

plt.scatter(X_train,Y_train,color="blue")
plt.plot(X_train,hmarks_model.predict(X_train),color="black")
plt.xlabel("Hours Studied")
plt.ylabel("Scores obtained")
plt.title("Hours studied vs Scores obtained")

plt.show()

score_for_7_hours=hmarks_model.predict([[7]])[0]
print("The predicted score for seven hours is : ",score_for_7_hours)