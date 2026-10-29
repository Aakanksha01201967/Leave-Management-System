# import os
# from flask import Flask, render_template, request, redirect, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime



# print("Database Location:")
# print(os.path.abspath("leave.db"))

# app = Flask(__name__)
# app.secret_key = "leave_secret"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leave.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # User Table
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(50))
#     role = db.Column(db.String(20))

# # Leave Table
# class Leave(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50))
#     from_date = db.Column(db.String(20))
#     to_date = db.Column(db.String(20))
#     reason = db.Column(db.String(200))
#     leave_type = db.Column(db.String(50))
#     status = db.Column(db.String(20), default="Pending")

# class LeaveLedger(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100))
#     leave_type = db.Column(db.String(50))
#     days = db.Column(db.Integer)
#     transaction_type = db.Column(db.String(20))


# with app.app_context():

#     db.create_all()

#     admin = User.query.filter_by(
#         username='admin'
#     ).first()

#     if not admin:

#         admin = User(
#             username='admin',
#             password='admin123',
#             role='admin'
#         )

#         db.session.add(admin)
#         db.session.commit()

# # Home
# @app.route('/')
# def home():
#     return redirect('/login')

# # Registration
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         user = User(
#             username=username,
#             password=password,
#             role='user'
#         )

#         db.session.add(user)
#         db.session.commit()

#         casual = LeaveLedger(
#             username=username,
#             leave_type="Casual Leave",
#             days=10,
#             transaction_type="Credit"
#         )

#         maternity = LeaveLedger(
#             username=username,
#             leave_type="Maternity Leave",
#             days=0,
#             transaction_type="Credit"
#         )

#         privilage = LeaveLedger(
#             username=username,
#             leave_type="Privilage Leave",
#             days=15,
#             transaction_type="Credit"
#         )

#         lwp = LeaveLedger(
#             username=username,
#             leave_type="Leave Without Pay Leave",
#             days=4,
#             transaction_type="Credit"
#         )

#         compoff = LeaveLedger(
#             username=username,
#             leave_type="CompOff Leaves",
#             days=0,
#             transaction_type="Credit"
#         )

#         client = LeaveLedger(
#             username=username,
#             leave_type="Client Leave",
#             days=0,
#             transaction_type="Credit"
#         )

#         db.session.add(casual)
#         db.session.add(maternity)
#         db.session.add(privilage)
#         db.session.add(lwp)
#         db.session.add(compoff)
#         db.session.add(client)

#         db.session.commit()

#         all_users = User.query.all()

#         for u in all_users:
#             print(u.id, u.username, u.role)

#         flash("Registration Successful")
#         return redirect('/login')

#     return render_template('register.html')

# # Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():

#     if request.method == 'POST':

#         username = request.form['username']
#         password = request.form['password']

#         user = User.query.filter_by(
#             username=username,
#             password=password
#         ).first()

#         if user: 

#             session['username'] = user.username
#             session['role'] = user.role

#             if user.role == 'admin':
#                 return redirect('/admin_dashboard')
#             else:
#                 return redirect('/user_dashboard')

#         flash("Invalid Username or Password")

#     return render_template('login.html')

# # User Dashboard
# @app.route('/user_dashboard')
# def user_dashboard():

#     if 'username' not in session:
#         return redirect('/login')

#     total_leaves = Leave.query.filter_by(
#             username=session['username']
#         ).count()
    

#     leaves = Leave.query.filter_by(
#         username=session['username']
#     ).all()



#     # 3. Fetch leave ledger entries ONLY for THIS specific user
#     ledger_entries = LeaveLedger.query.filter_by(username=session['username']).all()
    
#     # 4. Calculate remaining balance for each leave type
#     leave_balances = {}
#     for entry in ledger_entries:
#         if entry.leave_type not in leave_balances:
#             leave_balances[entry.leave_type] = 0
        
#         if entry.transaction_type == "Credit":
#             leave_balances[entry.leave_type] += entry.days
#         elif entry.transaction_type == "Debit":
#             leave_balances[entry.leave_type] -= entry.days

#     return render_template(
#         'user_dashboard.html',
#         username=session['username'],
#         leaves=leaves, 
#         total_leaves=total_leaves,
#         leave_balances=leave_balances
#     )

#     # return render_template(
#     #     'user_dashboard.html',
#     #     leaves=leaves, total_leaves=total_leaves
#     # )




# # Apply Leave
# @app.route('/apply_leave', methods=['GET', 'POST'])
# def apply_leave():

#     if request.method == 'POST':

#         leave = Leave(
#             username=session['username'],
#              leave_type=request.form['leave_type'],
#             from_date=request.form['from_date'],
#             to_date=request.form['to_date'],
#             reason=request.form['reason']
#         )

#         db.session.add(leave)
#         db.session.commit()

#         return redirect('/user_dashboard')

#     return render_template('apply_leave.html')

# # Admin Dashboard
# @app.route('/admin_dashboard')
# def admin_dashboard():

#     if session.get('role') != 'admin':
#         return redirect('/login')

  

#     total_leaves = Leave.query.count()

#     leaves = Leave.query.all()

#     return render_template(
#         'admin_dashboard.html',
#         leaves=leaves,
#         total_leaves=total_leaves
#     )
# @app.route('/users')
# def users():

#     users = User.query.all()


#     approved = Leave.query.filter_by(
#     status='Approved'
#     ).count()

#     return render_template(
#         'users.html',
#         users=users,
       
#     )
    

# # Approve Leave
# @app.route('/approve/<int:id>')
# def approve(id):

#     leave = Leave.query.get(id)

#     leave.status = 'Approved'

#     db.session.commit()

#     return redirect('/admin_dashboard')

# # Reject Leave
# @app.route('/reject/<int:id>')
# def reject(id):


#     leave = Leave.query.get(id)

#     leave.status = 'Rejected'

#     db.session.commit()

#     return redirect('/admin_dashboard')

# # Logout
# @app.route('/logout')
# def logout():

#     session.clear()

#     return redirect('/login')

# if __name__ == "__main__":
#     app.run(debug=True)


import os
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

print("Database Location:")
print(os.path.abspath("leave.db"))

app = Flask(__name__)
app.secret_key = "leave_secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leave.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(20))

# Leave Table
class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    from_date = db.Column(db.String(20))
    to_date = db.Column(db.String(20))
    reason = db.Column(db.String(200))
    leave_type = db.Column(db.String(50))
    status = db.Column(db.String(20), default="Pending")

class LeaveLedger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    leave_type = db.Column(db.String(50))
    days = db.Column(db.Integer)
    transaction_type = db.Column(db.String(20))

with app.app_context():
    db.create_all()

    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            password='admin123',
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()

# Home
@app.route('/')
def home():
    return redirect('/login')

# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Choose another.")
            return redirect('/register')

        user = User(
            username=username,
            password=password,
            role='user'
        )
        db.session.add(user)
        db.session.commit()

        # Give standard credits to new user
        initial_leaves = [
            ("Casual Leave", 10),
            ("Maternity Leave", 0),
            ("Privilage Leave", 15),
            ("Leave Without Pay Leave", 4),
            ("CompOff Leaves", 0),
            ("Client Leave", 0)
        ]

        for l_type, l_days in initial_leaves:
            ledger_entry = LeaveLedger(
                username=username,
                leave_type=l_type,
                days=l_days,
                transaction_type="Credit"
            )
            db.session.add(ledger_entry)

        db.session.commit()
        flash("Registration Successful")
        return redirect('/login')

    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user: 
            session['username'] = user.username
            session['role'] = user.role

            if user.role == 'admin':
                return redirect('/admin_dashboard')
            else:
                return redirect('/user_dashboard')

        flash("Invalid Username or Password")

    return render_template('login.html')

# User Dashboard
@app.route('/user_dashboard')
def user_dashboard():
    if 'username' not in session:
        return redirect('/login')

    username = session['username']

    total_leaves = Leave.query.filter_by(username=username).count()
    leaves = Leave.query.filter_by(username=username).all()

    # Fetch leave ledger entries ONLY for THIS specific user
    ledger_entries = LeaveLedger.query.filter_by(username=username).all()
    
    # Calculate remaining balance for each leave type
    leave_balances = {}
    for entry in ledger_entries:
        if entry.leave_type not in leave_balances:
            leave_balances[entry.leave_type] = 0
        
        if entry.transaction_type == "Credit":
            leave_balances[entry.leave_type] += entry.days
        elif entry.transaction_type == "Debit":
            leave_balances[entry.leave_type] -= entry.days

    return render_template(
        'user_dashboard.html',
        username=username,
        leaves=leaves, 
        total_leaves=total_leaves,
        leave_balances=leave_balances
    )

# Apply Leave
@app.route('/apply_leave', methods=['GET', 'POST'])
def apply_leave():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        leave = Leave(
            username=session['username'],
            leave_type=request.form['leave_type'],
            from_date=request.form['from_date'],
            to_date=request.form['to_date'],
            reason=request.form['reason']
        )

        db.session.add(leave)
        db.session.commit()

        return redirect('/user_dashboard')

    return render_template('apply_leave.html')

# Admin Dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        return redirect('/login')

    total_leaves = Leave.query.count()
    leaves = Leave.query.all()

    return render_template(
        'admin_dashboard.html',
        leaves=leaves,
        total_leaves=total_leaves
    )

@app.route('/users')
def users():
    if session.get('role') != 'admin':
        return redirect('/login')
        
    users = User.query.all()
    return render_template(
        'users.html',
        users=users
    )

# Approve Leave
@app.route('/approve/<int:id>')
def approve(id):
    if session.get('role') != 'admin':
        return redirect('/login')

    leave = Leave.query.get(id)
    if leave and leave.status != 'Approved':
        leave.status = 'Approved'

        # Calculate number of days between from_date and to_date
        try:
            d1 = datetime.strptime(leave.from_date, '%Y-%m-%d')
            d2 = datetime.strptime(leave.to_date, '%Y-%m-%d')
            days_count = (d2 - d1).days + 1
            if days_count < 1:
                days_count = 1
        except:
            days_count = 1  # Fallback if date parsing format varies

        # Add a Debit transaction to the user's LeaveLedger
        debit_entry = LeaveLedger(
            username=leave.username,
            leave_type=leave.leave_type,
            days=days_count,
            transaction_type="Debit"
        )
        db.session.add(debit_entry)
        db.session.commit()

    return redirect('/admin_dashboard')

# Reject Leave
@app.route('/reject/<int:id>')
def reject(id):
    if session.get('role') != 'admin':
        return redirect('/login')

    leave = Leave.query.get(id)
    if leave:
        leave.status = 'Rejected'
        db.session.commit()

    return redirect('/admin_dashboard')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)