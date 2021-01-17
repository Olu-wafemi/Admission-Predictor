from flask import Flask, render_template,request,redirect,flash
app = Flask(__name__)

app.config['SECRET_KEY'] = '\x81G.kt!==\xf5\x06\x85\xd7(\r\xbaS\x9a;\xdb\t\x91\xb53#'
import pickle
import os
Model = pickle.load(open('chair.pkl','rb'))

@app.route("/",methods=["POST","GET"])
@app.route("/predict",methods=["POST","GET"])	

def posts():
    if request.method == 'POST':
        GRE_SCORE = float(request.form.get('GRE Score'))
        TOEFL_SCORE  = float(request.form.get('TOEFL Score'))
        University = float(request.form.get('University Rating'))
        SOP =   float(request.form.get('SOP'))
        LOR =   float(request.form.get('LOR '))
        CGPA =   float(request.form.get('CGPA'))
        Research =   float(request.form.get('Research'))
        data=[[GRE_SCORE,TOEFL_SCORE,University,SOP,LOR,CGPA,Research]]
        prediction = Model.predict(data)[0]
        flash(f'The Chance of Admission is {prediction}')
    return render_template('index.html')

        

        
        
        

if __name__=="__main__":
	app.run()