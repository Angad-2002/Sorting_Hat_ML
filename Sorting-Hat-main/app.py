from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Render the form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        O = float (request.form['ll1'])
        C = float (request.form['ll2'])
        E = float (request.form['ll3'])
        A = float (request.form['ll4'])
        N = float (request.form['ll5'])

        values = [O, C, E, A, N]

        def calc(x, max):
            return (x/max)*50
        
        for m in range(len(values)):
            values[m] = calc(values[m], 120)

        with open("model.bin", "rb") as file:
            model = pickle.load(file)
            
        P = model.predict ([values])

        return jsonify (user_name=P[0])

@app.route('/page2')
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True)

