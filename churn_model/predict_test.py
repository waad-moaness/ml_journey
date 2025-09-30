import requests

url = 'http://localhost:9696/'

customer_id = 'xyz-123'
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 2,
    "monthlycharges": 29.85,
    "totalcharges": (29.85)
}

r= requests.post(url,json=customer)
result= r.json()

print(result)

if result['churn'] == True:
    print(f"customer churning send email/nchurn probability = {result['churnprob']}")
else:
    print(f"customer not churning don't send email /nchurn probability = {result['churnprob']}")