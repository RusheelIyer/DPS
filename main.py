# [START app]
from flask import Flask
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


@app.route('/')
def return_prediction():
    linear_model = pickle.load(open("linear_model.pkl", 'rb'))
    message = str(linear_model.predict(np.asarray([202101]).reshape(1, -1))[0][0])
    return message


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    return 'An internal error occurred.', 500

if __name__ == '__main__':
     app.run(host='localhost', debug=False)

# [END app]