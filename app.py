from flask import Flask,request
import pickle


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app=Flask(__name__)

@app.route('/ping',methods=['GET'])
def ping():
    return {'msg':'hello'}

@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    print(data)
    if data:
        print('in')
        if data['Gender']=='Male':
            Gender=1
        else:
            Gender=0
        
        if data['Married']=='Yes':
            Married=1   
        else:
            Married=0
        
        loan_status=model.predict([[Gender,Married,data['ApplicantIncome'],data['LoanAmount'],data['Credit_History']]])
        if (int(loan_status[0])==1):
            status='Loan accepted'
        else:
            status='Loan rejected'
        return {'response':status}

    else:
        return '<h1>Data not received</h1>'
        

if __name__=='__main__':
    app.run(debug=True)