from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    pass

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)