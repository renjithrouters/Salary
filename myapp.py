from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('myhtml.html')

@app.route('/predict', methods=['POST'])
def predict():
	int_features = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	prediction=model.predict(final_features)
	return render_template('myhtml.html', prediction_text='Employee Salary should be Rs. {}'.format(prediction))

if __name__ == '__main__':
	app.run(debug=True)  
