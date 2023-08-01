from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
# global num
# num = 0
app = Flask(__name__)
model = pickle.load(open('random_forest_classifier_BalancedData1_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')



@app.route('/feedbackform',methods=['GET'])
def feedbackform():
    return render_template('feedbackform.html')

@app.route('/learnmore',methods=['GET'])
def learnmore():
    return render_template('learnmore.html')

@app.route('/valid',methods=['GET'])
def valid():
    return render_template('valid.html')

@app.route('/Contacthtml',methods=['GET'])
def Contacthtml():
    return render_template('Contacthtml.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        BQ= float(request.form['BQ'])
        ESS=float(request.form['ESS'])
        BMI=float(request.form['BMI'])
        #Kms_Driven2=np.log(Kms_Driven)
        Weight=float(request.form['Weight'])
        Height=float(request.form['Height'])
        Head=float(request.form['Head'])
        Neck=float(request.form['Neck'])
        Waist=float(request.form['Waist'])
        Buttock=float(request.form['Buttock'])
        Age=int(request.form['Age'])
        M=float(request.form['M'])
        prediction=model.predict([[BQ,ESS,BMI,Weight,Height,Head,Neck,Waist,Buttock,Age,M
]])
        prediction=round(prediction[0],4)
        if prediction<0:
            return render_template('valid.html',prediction_texts="No{}") 
        elif prediction==0:
            return render_template('normal.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : NORMAL") 
        elif prediction==1:
            return render_template('mild.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : MILD ")   
        elif prediction==2:
            return render_template('moderate.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : MODERATE ")
        elif prediction ==3:
            return render_template('severe.html',prediction_text= "OBSTRUCTIVE SLEEP APNEA CONDITION : SEVERE")  
    else:
        return render_template('valid.html')
    
# global num

standard_to = StandardScaler()
@app.route("/feedback", methods=['POST'])
def feedback():
    # num = num+1
    if request.method == 'POST':
        name = str(request.form['name'])
        email = str(request.form['email'])
        msg = str(request.form['about'])
        phoneNumber = int(request.form['phoneNumber'])
        zipcode = int(request.form['zipcode'])
        gender = str(request.form['gender'])
        lst = [name,email,msg,phoneNumber,zipcode,gender]
        with open('files/'+str(phoneNumber)+'text','w') as f:

            for item in lst:
                f.write(str(item)+'\n')

        # num+=1
        return render_template('thankyou.html')
    
    return render_template('error.html',text="error")



if __name__=="__main__":
    app.run(debug=True)