# Import the libraies
import numpy as np
from flask import Flask, request, render_template
import joblib

# Create the Flask app and load the trained model
app = Flask(__name__)
model = joblib.load('models/price_prediction_rf.pkl')

# Define the '/' root route to display the content from index.html
@app.route('/')
def home():
    return render_template('index.html')

# Define the '/predict' route to:
# - Get form data and convert them to float values
# - Convert form data to numpy array
# - Pass form data to model for prediction

@app.route('/predict',methods=['POST'])
def predict():

    form_data = [x for x in request.form.values()]
    features = [np.array(form_data)]
    prediction = model.predict(features)

	# Format prediction text for display in "index.html"
    return render_template('index.html', mp ='Moblile price range should be {}'.format(prediction[0]))

if __name__ == '__main__':
    app.run(debug=False)