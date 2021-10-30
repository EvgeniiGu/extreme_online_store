from datetime import datetime
from flask import render_template, request, url_for
from FlaskWebProject1 import app
text = "q"
@app.route('/')
@app.route('/Main.html')
def home():
    return render_template('index.html')

@app.route('/Sign-in.html', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        username = request.form.get('text')  # запрос к данным формы
        password = request.form.get('text-1')
        print(username, password)
    return render_template('Sign-in.html')

@app.route('/About-us.html')
def abotus():
    return render_template('About-us.html')

@app.route('/Contacts.html')
def contacts():
    return render_template('Contacts.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.args.get('ent_text')
    print(text)
    return '''<html><body><h1>Ok</h1><h2>''' + text + '''</h2></body></html>'''



@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', forward_message=forward_message);