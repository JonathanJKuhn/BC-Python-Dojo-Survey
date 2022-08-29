from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Super Secrect Session Key'

sessionArr = {
    'name' : '',
    'location' : '',
    'language' : '',
    'satisfaction' : '',
    'reason' : '',
    'comment' : ''
}

def addToSession(sessionArr:dict):
    for item in sessionArr:
        session[item] = sessionArr[item]

@app.route('/')
def home():
    locations = ['seattle', 'online', 'burbank', 'bellvue']
    languages = ['html', 'css', 'javascript', 'python', 'csharp', 'java']
    satScale = [1,2,3,4,5]
    reasons = [
        { 'title' : 'Career Change', 'value' : 'change'},
        { 'title' : 'Career Advancement', 'value' : 'advancement'},
        { 'title' : 'Personal Interest', 'value' : 'personal'},
        { 'title' : 'Other', 'value' : 'other'}
    ]

    if 'isActive' not in session:
        addToSession(sessionArr)
    
    return render_template('index.html', locations=locations,languages=languages,satScale=satScale,reasons=reasons)

@app.route('/process', methods=['POST'])
def process():
    sessionArr = {
        'name' : request.form['nameInput'],
        'location' : request.form['locationInput'],
        'language' : request.form['languageInput'],
        'satisfaction' : request.form['satisfactionInput'],
        'comment' : request.form['commentInput']
    }
    if 'otherReasonInput' in request.form:
        sessionArr['otherReason'] = request.form['otherReasonInput']

    sessionArr['reason'] = request.form.getlist('reasonInput')

    session.clear()
    addToSession(sessionArr)
    session['isActive'] = True
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)