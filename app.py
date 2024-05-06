from flask import Flask,render_template
from pymongo import MongoClient

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add',methods=['POST'])
def add():
    return render_template('index.html')

@app.route('/complete/<id>')
def complete():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)