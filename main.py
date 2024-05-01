from flask import Flask, render_template, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
password, user = '1234', 'beni'


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db.init_app(app)
app.secret_key = b'_5#y2L"F4hi=g]/'
buy_enable = False


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/buy', methods=['GET', 'POST'])
def user_data():
    global buy_enable
    if request.method == 'POST':
        buy_enable = True
        name = str(request.form['first']) + ' ' + str(request.form['last'])
        address = str(request.form['address'])
        email = str(request.form['email'])
        datas = UserData(name=name, address=address, email=email)
        db.session.add(datas)
        db.session.commit()
        return redirect(url_for('card'))
    return render_template('user_data.html')


@app.route('/buy/card', methods=['GET', 'POST'])
def card():
    global buy_enable
    if buy_enable:
        buy_enable = False
        return redirect('https://buy.stripe.com/00gbJ3coneQF10c3cc')
    return redirect(url_for('user_data'))


@app.route('/a', methods=['GET', 'POST'])
def admin():
    admin_enabled = False
    if request.method == 'POST':
        if request.form['user'] == user and request.form['password'] == password:
            admin_enabled = True

        if admin_enabled:
            session['logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin.html')
    return render_template('admin.html')


@app.route('/admin')
def admin_dashboard():
    megrendeles = db.session.execute(db.select(UserData)).scalars()
    if 'logged_in' in session:
        return render_template('admin_dash.html', megrendeles=megrendeles)
    else:
        return redirect(url_for('admin'))


@app.route('/delete/<int:order_id>', methods=['POST'])
def delete(order_id):
    datas = UserData.query.get_or_404(order_id)
    db.session.delete(datas)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('admin'))


app.run(debug=True)
