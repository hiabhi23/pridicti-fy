from tkinter import Scale
from django.http import HttpResponse
from django.shortcuts import render 
import numpy as np
import pickle
import streamlit as st
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score







def home(request):
    return render(request,"diabetes.html")

def result(request):
    loaded_model = pickle.load(open("C:/Users/areeb/OneDrive/Desktop/Django/DeployModel-project/trained_model_Diabetes (1).sav",'rb'))
    
    
    lis=[]
    lis.append(request.GET['Pregnancies'])
    lis.append(request.GET['Glucose'])
    lis.append(request.GET['BloodPressure'])
    lis.append(request.GET['SkinThickness'])
    lis.append(request.GET['Insulin'])
    lis.append(request.GET['BMI'])
    lis.append(request.GET['DiabetesPredigreeFunction'])
    lis.append(request.GET['Age'])
    
    
# Change into numpy array

    
    input_data_as_numpy_array=np.asarray(lis)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    if (prediction[0]== 0):
        return render(request,"result.html",{'ans':'THE PERSON IS NOT DIABETIC'})
    else:
        return render(request,"result.html",{'ans':'THE PERSON IS DIABETIC'})
    



def home_two(request):
    return render(request,'heart.html')



def result_two(request):
    loaded_model_two = pickle.load(open("C:/Users/areeb/OneDrive/Desktop/Django/DeployModel-project/trained_model_Heart.sav",'rb'))
    
    
    list=[]
    list.append(request.GET['age'])
    list.append(request.GET['sex'])
    list.append(request.GET['cp'])
    list.append(request.GET['trestbps'])
    list.append(request.GET['chol'])
    list.append(request.GET['fbs'])
    list.append(request.GET['restecg'])
    list.append(request.GET['thalach'])
    list.append(request.GET['exang'])
    list.append(request.GET['oldpeak'])
    list.append(request.GET['slope'])
    list.append(request.GET['ca'])
    list.append(request.GET['thal'])
    

 
 
# Change into numpy array

    
    input_data_as_numpy_array=np.asarray(list)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model_two.predict(input_data_reshaped)
    
    if (prediction[0]== 0):
        return render(request,"result_two.html",{'ans':'THE PERSON IS NOT HAVING HEART PROBLEMS'})
    else:
        return render(request,"result_two.html",{'ans':'THE PERSON IS HAVING HEART PROBLEMS '})
 
      
    
def feedbackForm(request):
    return render(request,'feedbackForm.html')

def rating(request):
    return render(request,'rating.html')

def remediesD(request):
    return render(request,'remediesD.html')

def remediesH(request):
    return render(request,'remediesH.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appointmentH(request):
    return render(request,'appointmentH.html')

def appointmentD(request):
    return render(request,'appointmentD.html')

