from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class PasswordManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(520), nullable=False)
    username = db.Column(db.String(520), nullable=False)
    email = db.Column(db.String(520), nullable=False)
    password = db.Column(db.String(520), nullable=False)
    
    def __repr__(self) -> str:
        return '<PasswordManager %r>' % self.id

@app.route('/')
def home():
    passwords = PasswordManager.query.all()
    return render_template("index.html", passwords=passwords)

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        # Retrieve form data
        service_name = request.form['service_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Create a new PasswordManager instance
        new_password_manager = PasswordManager(service_name=service_name, username=username, email=email, password=password)
        
        # Add the new instance to the database
        with app.app_context():
            db.session.add(new_password_manager)
            db.session.commit()
        
        return redirect("/")
    
@app.route('/update/<int:id>', methods=['POST','GET'])
def update_details(id):
    update_details = PasswordManager.query.get_or_404(id)
    if request.method == 'POST':
        update_details.service_name = request.form['service_name']
        update_details.username = request.form['username']
        update_details.email = request.form['email']
        update_details.password = request.form['password']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return ("There was a problem while updating")
    else:
        return render_template('update.html', update_details=update_details)

@app.route('/delete/<int:id>')
def delete_details(id):
    details_to_delete = PasswordManager.query.get_or_404(id)
    try:
        db.session.delete(details_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return ("There was a problem while deleting")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)