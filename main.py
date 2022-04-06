from flask import Flask, render_template, request, redirect
import sqlite3
con = sqlite3.connect("hospitalmanagementsystem.db", check_same_thread= False)
listOfTables = con.execute("SELECT name from sqlite_master WHERE type='table' AND name='PATIENT' ").fetchall()
if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    con.execute(''' CREATE TABLE PATIENT(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            PATIENTNAME TEXT,
                            MOBILE INTEGER,
                            AGE INTEGER,
                            ADDRESS TEXT,
                            PLACE TEXT,
                            PINCODE INTEGER,
                            DATEOFBIRTH TEXT,
                            PASSWORD TEXT); ''')

print("Table has created")
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def welcome():
    if request.method == "POST":
        getlogUsername = request.form["logusername"]
        getlogpassword = request.form["logpassword"]
        print(getlogUsername)
        print(getlogpassword)
        if getlogUsername == "admin" and getlogpassword == "12345":
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET","POST"])
def register():
    if request.method == "POST":
        getpatientName = request.form["patname"]
        getMobile = request.form["mobile"]
        getAge = request.form["age"]
        getAddress = request.form["address"]
        getPlace = request.form["place"]
        getPincode = request.form["pincode"]
        getDob = request.form["dob"]
        getPassword = request.form["pwd"]
        getConformPassword = request.form["cfnpwd"]
        print(getpatientName)
        print(getMobile)
        print(getAge)
        print(getAddress)
        print(getPlace)
        print(getPincode)
        print(getDob)
        print(getPassword)
        print(getConformPassword)
        try:
            con.execute("INSERT INTO PATIENT(PATIENTNAME, MOBILE, AGE, ADDRESS, PLACE, PINCODE, DATEOFBIRTH, PASSWORD) VALUES('"+getpatientName+"','"+getMobile+"','"+getAge+"','"+getAddress+"','"+getPlace+"','"+getPincode+"','"+getDob+"','"+getPassword+"')")
            print("Successfully inserted.")
            con.commit()
            return redirect('/viewall')
        except Exception as e:
            print(e)

    return render_template("dashboard.html")

@app.route("/search")
def search():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM PATIENT WHERE MOBILE = 7485969685")
    q = cursor.fetchall()
    return render_template("search.html", patients=q)


@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/viewall")
def viewall():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM PATIENT")
    r = cursor.fetchmany()
    return render_template("viewall.html", patients=r)

if __name__=="__main__":
    app.run()
