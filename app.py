from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create the extension
db = SQLAlchemy()
db.init_app(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

def __repr__(self) -> str:
    return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect('/', code=303) 
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/', code=303) 
    updateTodo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', updateTodo=updateTodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    deleteTodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(deleteTodo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main___':
    app.run(debug=True)