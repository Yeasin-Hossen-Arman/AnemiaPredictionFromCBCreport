from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


app = Flask(__name__)


# Load dataset and train model
DATA_PATH = 'anemia.csv'
df = pd.read_csv(DATA_PATH)
X = df.drop("Result", axis=1)
y = df['Result']
x_train,x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
logistic = LogisticRegression()
logistic.fit(x_train, y_train)

# Gender = [0,1,1,1,0,1],
# Haemoglobin = [6.9,11.8,11,11,10.7,16.2],  
# MCH = [28.1,16.3,26,25.2,21.3,17.2],
# MCHC = [32.5,30.9,32.2,30.9,29.1,32.2],
# MCV = [94.6,78.7,98.9,83.2,78.7,78.4]


# result = logistic.predict([[Gender,Haemoglobin,MCH,MCHC,MCV]])











@app.route('/', methods=['GET', 'POST'])
def index():


    Gender = None,
    Haemoglobin = None,
    MCH = None,
    MCHC = None,
    MCV = None
    result = None

    if request.method == 'POST':
        

        Gender = float(request.form['Gender'])
        Haemoglobin = float(request.form['Haemoglobin'])
        MCH = float(request.form['MCH'])
        MCHC = float(request.form['MCHC'])
        MCV = float(request.form['MCV'])




        result = logistic.predict([[Gender,Haemoglobin,MCH,MCHC,MCV]])[0]

        if result == 1:
            result = 'Anemia Detect'
        else :
            result = 'Anemia Not Detect'


    return render_template('index.html', result= result)




if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))  # 5000 is a fallback for local runs
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)