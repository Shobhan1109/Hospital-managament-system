from flask import Flask, render_template, request, redirect
import sqlite3
con = sqlite3.connect("hospitalmanagementsystems.db", check_same_thread= False)
cursor = con.cursor()
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
        except Exception as e:
            print(e)

    return render_template("dashboard.html")

@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "POST":
        getMobile = request.form["mobile"]
        print(getMobile)
        try:
            cursor.execute("SELECT * FROM PATIENT WHERE MOBILE="+getMobile)
            print("Selected")
            q = cursor.fetchall()
            if len(q) == 0:
                print("Invalid mobile number")
            else:
                print("Search successful")
                print(len(q))
                return render_template("search.html", patient=q, status=True)
        except Exception as e:
            print(e)

    return render_template("search.html", patient=[], status=False)


@app.route("/delete", methods=["GET","POST"])
def delete():
    if request.method == "POST":
        getMobile = request.form["mobile"]
        print(getMobile)
        try:
            cursor.execute("DELETE FROM PATIENT WHERE MOBILE="+getMobile)
            q = cursor.fetchall()
            if len(q) == 0:
                print("Invalid mobile number")
            else:
                print("Successfully deleted")
                print(len(q))
                return render_template("search.html", patient=q, status=True)
        except Exception as e:
            print(e)

    return render_template("delete.html", patient=[], Status=False)

@app.route("/update",methods=["GET","POST"])
def update():
    if request.method == "POST":
        getMobile = request.form["mobile"]
        print(getMobile)
        try:
            cursor.execute("SELECT * FROM PATIENT WHERE MOBILE="+getMobile)
            print("Selected a patient")
            r = cursor.fetchall()
            if len(r)==0:
                print("Invalid mobile number")
            else:
                print(len(r))
                return render_template("viewupdate.html", patients=r)
            return redirect("/viewupdate")
        except Exception as e:
            print(e)
    return render_template("update.html")

@app.route("/viewupdate", methods = ['GET','POST'])
def viewupdate():
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
            con.execute(
                "INSERT INTO PATIENT(PATIENTNAME, MOBILE, AGE, ADDRESS, PLACE, PINCODE, DATEOFBIRTH, PASSWORD) VALUES('" + getpatientName + "','" + getMobile + "','" + getAge + "','" + getAddress + "','" + getPlace + "','" + getPincode + "','" + getDob + "','" + getPassword + "')")
            print("Successfully inserted.")
            con.commit()
            return redirect('/viewall')
        except Exception as e:
            print(e)

    return render_template("viewupdate.html")

@app.route("/viewall")
def viewall():
    cursor.execute("SELECT * FROM PATIENT")
    r = cursor.fetchall()
    return render_template("viewall.html", patients=r)

if __name__=="__main__":
    app.run(debug=True)