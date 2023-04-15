
import gzip,dill
from flask import Flask, request, render_template, redirect
app=Flask(__name__, template_folder="template")

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "my ML model"

@app.route('/predict', methods=["GET","POST"])
def predict():
    if request.method=="GET":
        tweet=request.args.get("tweet")
    else:
        tweet=request.form["text"]
    with gzip.open("sentiment_model.dill.gz", "rb") as f:
        model=dill.load(f)
    proba=model.predict_proba([tweet])[0,1]
    return "positive sentiment: {}".format(proba)
    

if __name__=="__main__":
    app.run()
