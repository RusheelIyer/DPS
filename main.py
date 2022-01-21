# [START app]
from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/')
def reroute():
    return "Send a post request to the /predict endpoint"

@app.route('/predict', methods=['POST'])
def return_prediction():

    request_data = request.get_json()

    year = request_data['year']
    month = request_data['month']
    feature = str(year)+str(month)

    linear_model = pickle.load(open("linear_model.pkl", 'rb'))
    prediction = {"prediction": linear_model.predict(np.asarray([feature]).reshape(1, -1))[0][0]}

    return jsonify(prediction)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    return 'An internal error occurred.', 500

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
# [END app]