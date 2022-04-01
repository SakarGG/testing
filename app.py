from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from flask_selfdoc import Autodoc
import os


import qrcode
import secrets

app = Flask(__name__)
auto = Autodoc(app)

# secrete key for sessions in flask
app.config['SECRET_KEY'] = os.urandom(64).hex()


# setting path for qr codes
location = os.path.dirname(os.path.realpath(__file__))
app.config.update(
    UPLOAD_PATH=os.path.join(location, "static")

)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("db.sqlite")
    except sqlite3.error as e:
        # catch error if can't connect to database
        print(e)
    return conn


def get_users():
    # connect to database and execute select statement
    conn = db_connection()
    cursor = conn.cursor()
    visitors = cursor.execute("SELECT * FROM Visitor").fetchall()

    # create list and for each row create a dictionary to be sent
    returnVisitors = []
    for row in visitors:
        completeRow = dict(id=row[0], name=row[1], address=row[2], city=row[3], phoneNumber=row[4], email=row[5],
                           device_ID=row[6], infected=row[7])
        returnVisitors.append(completeRow)

    return returnVisitors


# ======================================================================
# Gerneral pages and logged in


@app.route("/", methods=['GET', 'POST'])
@auto.doc()
def index():
    return render_template("index.html", value={""})


@app.route("/agent", methods=['GET', 'POST'])
def agent_login():

    if request.method == 'POST':
        session.pop("username", None)
        session.pop("user", None)

        username = request.form["username"]
        password = request.form["password"]
        conn = db_connection()

        print("Logging in as Agent:\nUsername: {}\nPassword: {}".format(
            password, username))

        sql_agent = "SELECT username,password from Agent"
        agents = conn.execute(sql_agent).fetchall()

        # Format:
        # [('Agent_username', 'agent_password'), ('Agent_username2', 'agent_password2')]

        # go through all agents and check credentials
        for agent in agents:
            if(username == agent[0] and password == agent[1]):

                session['username'] = username
                session['user'] = 'Agent'

                print("Logged in as agent")
                return redirect(url_for('dashboard_agent'))

    else:
        return render_template("agent_login.html")


@app.route("/hospital", methods=["GET", "POST"])
def hospital_login():
    if request.method == 'POST':
        session.pop("username", None)
        session.pop("user", None)

        username = request.form["username"]
        password = request.form["password"]
        conn = db_connection()

        print("Logging in as Hospital with:\nUsername: {}\nPassword: {}".format(
            password, username))

        sql_hospital = "SELECT username,password from Hospital"
        hospitals = conn.execute(sql_hospital).fetchall()

        # Format
        # [('Agent_username', 'agent_password'), ('Agent_username2', 'agent_password2')]

        # go through all hospitals and check credentials
        for hopsital in hospitals:
            if(username == hopsital[0] and password == hopsital[1]):

                session['username'] = username
                session['user'] = 'Hopsital'

                print("Logged in as hopsital")
                return redirect(url_for('dashboard_hospital'))

    return render_template("hospital_login.html")


# =====================================================================================
# register users

@app.route("/reg_visitor", methods=["GET", "POST"])
@auto.doc()
def visitor_registration():

    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        city = request.form["city"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]

        device_ID = os.urandom(32).hex()
        infected = 0
        sql = """INSERT INTO Visitor (name,address, city, phoneNumber, email, device_ID,infected)
                 VALUES (?,?, ?, ?, ?, ?,?)"""
        cursor = cursor.execute(
            sql, (name, address, city, phoneNumber, email, device_ID, infected))
        conn.commit()

        return render_template("scan_qrcode.html")

    else:
        return render_template("visitor_registration.html")


@app.route("/reg_hospital", methods=["GET", "POST"])
@auto.doc()
def hospital_registration():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["pass"]
        sql = """INSERT INTO Hospital (name,username, password)
                 VALUES (?,?, ?)"""
        cursor = cursor.execute(
            sql, (name, username, password))
        conn.commit()
        return redirect(url_for('dashboard_agent'))
    else:
        return render_template("hospital_registration.html") 





@app.route("/reg_place", methods=["GET", "POST"])
# nopep8
@auto.doc()
def locale_registration():
    # if method post is used we input data into database
    if(request.method == "POST"):
        # grab data from html
        name = request.form["name"]
        address = request.form["address"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]

        qrcode_image_name = f"{secrets.token_hex(10)}.png"
        image_path = f"{app.config['UPLOAD_PATH']}/{qrcode_image_name}"
        try:
            place_qrcode = qrcode.make(str(name))
            place_qrcode.save(image_path)
        except Exception as excep:
            print(excep)

        # connect to database, create cursor, execute sql, and return message
        conn = db_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO Place (name,address,phoneNumber,email)
                 VALUES (?,?,?,?)"""
        cursor = cursor.execute(sql, (name, address, phoneNumber, email))
        conn.commit()

        return render_template("place_dashboard.html", image=qrcode_image_name)

    else:
        return render_template("place_registration.html")

# =====================================================================================
# log user our by popping their sessions


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user', None)
    return redirect(url_for('index'))


# ======================================================================================================
# dashboards

@app.route("/dashboard_agent")
def dashboard_agent():

    # if user logged in then ONLY as Agent allow to dashboard
    if('username' in session and str(session['user']) == "Agent"):
        # return agent data on users

        return render_template("dashboard_agent.html", value={"visitors": get_users()})
    else:
        # if user not logged in return to index page
        return redirect(url_for('index'))


@app.route("/dashboard_hospital")
def dashboard_hospital():
    # if user logged in then ONLY as hospital allow to dashboard
    if('username' in session and str(session['user']) == "Hopsital"):
        return render_template("dashboard_hospital.html")
    else:
        # if user not logged successfully in return to index page
        return redirect(url_for('index'))

# route to redirect user to scan a qr code


@app.route("/scan_qrcode")
def scan_qrcode():
    return render_template("scan_qrcode.html")


# route to redirect user to timer
@app.route("/timer")
def timer():
    return render_template("visitor_timer.html")


@app.route("/place_dashboard")
def place_dashboard():
    return render_template("place_dashboard.html")


@app.route("/searchvisitor", methods=['GET', 'POST'])
def searchvisitor():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        cursor.execute("SELECT * from Visitor WHERE name=?", (book,))

        data = cursor.fetchall()

        return render_template('search_visitor.html', data=data)
    return render_template("search_visitor.html")


@app.route("/searchplace", methods=['GET', 'POST'])
def searchplace():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        cursor.execute("SELECT * from Place WHERE name=?", (book,))

        data = cursor.fetchall()

        return render_template('search_place.html', data=data)
    return render_template("search_place.html")

@app.route("/searchpatient", methods=['GET', 'POST'])
def searchpatient():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        cursor.execute("SELECT * from Visitor WHERE name=?", (book,))

        data = cursor.fetchall()

        return render_template('search_patient.html', data=data)
    return render_template("search_patient.html")



@app.route('/docs')
def documentation():
    return auto.html(title='Corona Archive API Documentation')


def search():
    conn = db_connection()
    cursor = conn.cursor()
    name = request.form['name']
    # search by name
    cursor.execute("SELECT * from Visitor WHERE name=?", (name,))
    data = cursor.fetchall()
    return data

# if __name__ == "__main__":


if __name__ == "__main__":
    app.run(debug=True, port=3000)
