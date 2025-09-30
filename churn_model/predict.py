import pickle
from flask import Flask
from flask import request
from flask import jsonify


with open('CustomerChurn.pkl','rb') as fin:
    model,dv,scaler = pickle.load(fin)

app = Flask(__name__)

@app.route('/',methods= ['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    X_scaled = scaler.transform(X)
    y_pred=model.predict_proba(X_scaled)[:,1]
    churn= (y_pred >=0.5)

    result = {
        "churnprob" : float(y_pred) ,
        "churn" : bool(churn)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)

