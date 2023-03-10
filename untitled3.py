# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dENaqXORHOtriluE7ilypEKTxFgS8-Ai
"""

import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/mamtawardhani/Datasets-for-linear-and-logistic-regression/main/score-accepted.csv")

score_list = df['Score'].tolist()
accepted_list = df['Accepted'].tolist()

print(score_list)

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

import numpy as np

X = np.reshape(score_list,(len(score_list),1))
Y = np.reshape(accepted_list,(len(accepted_list),1))

lr = LogisticRegression()
lr.fit(X,Y)

def model(x):
  return 1/(1+np.exp(-x))

chances = model(X * lr.coef_ * lr.intercept_).ravel()

user_score = float(input("Enter your marks here : "))
chances = model(X * lr.coef_ + lr.intercept_).ravel()[6]
if chances <= 0.01 :
  print("The student will not get accepted")
elif chances >=1 : 
  print("Student will get accepted ")
elif chances <0.5:
  print("The student might not get accepted")
else :
  print("The student might get accepted")



