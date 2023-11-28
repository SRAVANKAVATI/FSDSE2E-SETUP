

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify


app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")



@app.route('/predict',methods=["GET","POST"])
def predict_datapoints():
    if request.method == "POST":
        return render_template("form.html")
    

    else:
        pass





app.run()