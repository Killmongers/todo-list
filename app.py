from flask import Flask,render_template,redirect,url_for,request
from pymongo import MongoClient
from bson import ObjectId
client=MongoClient("mongodb://localhost:27017")
db=client['todo']
collection=db['list']

app=Flask(__name__)

@app.route('/')
def index():
    complete=db.collection.find({'complete':True})
    incomplete=db.collection.find({'complete':False})
    return render_template('index.html',incomplete=incomplete, complete=complete)

@app.route('/add',methods=['POST'])
def add():
    todo=request.form['todoitem']
    db.collection.insert_one({'text':todo, 'complete':False})
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    db.collection.update_one({"_id":ObjectId(id)},{"$set":{"complete":True}})

    return redirect(url_for('index'))

@app.route('/remove',methods=['POST'])
def remove():
    db.collection.delete_many({'complete':True})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)