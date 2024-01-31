# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:08:13 2024

@author: ccm
"""

#Using Matplotlib
import matplotlib.pyplot as plt
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]
plt.plot(temp, react_conv)#(x=axis,y=axis)
plt.show()

#Labelling your plot axis
plt.xlabel("temperature")
plt.ylabel("reaction conversion")
plt.title("chemical experiment")
plt.show()

#Using plotly
import plotly.express as px
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]
fig = px.line(x=temp, y=react_conv)

#This creates a html file
#Import web browser
#web browser.open ("plothtml")To automatically open the html file
day1_attendees = [70, 20, 64, 90, 80]
day1_names = ["blessing", "mali", "pangi", "tafi", "shini"]
plt.bar(day1_names,day1_attendees)
plt.show ()
#Scatter plot
x_scatter = [1, 2, 3, 4, 5];
y_scatter = [2, 4, 6, 8, 10];
plt.scatter(x_scatter, y_scatter)
plt.show()

import pandas 
file= pandas.read_csv("iris.csv")
file["class"] =file["class"].str.replace("Iris-","")
plt.scatter(file["sepal_length"],file["sepal_width"])
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.show()
import seaborn as sns
sns.pairplot(file,hue="class")
plt.show()

class_count=file ['class'].value_counts()

                      

