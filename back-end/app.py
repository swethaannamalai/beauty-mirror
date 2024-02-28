import sqlite3
from flask import Flask ,render_template,flash,session,request,redirect

app=Flask(__name__)
app.secret_key="123"

sqlconnection =sqlite3.connect("beauty.db")
sqlconnection.execute("create table if not exists register(username text,email text,password text,confirm text)")
sqlconnection.execute("create table if not exists contact(name text, email text,message text)")
sqlconnection.execute("create table if not exists appointment(name text,services text,price number,date number,time number,phonenumber number)")
sqlconnection.close()
 
       
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/appointment',methods =["GET","POST"])
def appointment():
    if request.method =="POST":
        try:
            aname=request.form['name']
            aservices=request.form['services']
            aprice=request.form['price']
            adate=request.form['date']
            atime=request.form['time']
            aphonenumber=request.form['phonenumber']

            sqlconnection= sqlite3.connect('beauty.db')
       
            cur=sqlconnection.cursor()
            cur.execute("insert into appointment(name,services,price,date,time,phonenumber)values(?,?,?,?,?,?)",(aname,aservices,aprice,adate,atime,aphonenumber))
            sqlconnection.commit()
            flash("Message has been sent","record")
        except:
             flash("Opps! Please Try Again","oops")
             return redirect('/')

        finally:
             return redirect('/')
             sqlconnection.close()

    return render_template("appointment.html")

@app.route('/contact',methods =["GET","POST"])
def contact():
     if request.method =="POST":
        try:
            cname=request.form['name']
            cemail=request.form['email']
            cmessage=request.form['message']
            sqlconnection= sqlite3.connect('beauty.db')
       
            cur=sqlconnection.cursor()
            cur.execute("insert into contact(name,email,message)values(?,?,?)",(cname,cemail,cmessage))
            sqlconnection.commit()
            flash("Message has been sent","record")
        except:
             flash("Opps! Please Try Again","oops")
             return redirect('/')

        finally:
             return redirect('/')
             sqlconnection.close()


     return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/facial')
def facial():
    return render_template("facial.html")

@app.route('/waxing')
def waxing():
    return render_template("waxing.html")

@app.route('/hairstyle')
def hairstyle():
    return render_template("hairstyle.html")

@app.route('/nail')
def nail():
    return render_template("nail.html")

@app.route('/bridal')
def bridal():
    return render_template("bridal.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        rusername = request.form['username']
        remail = request.form['email']
        rpassword = request.form['password']
        rconfirm = request.form['confirm']
        conn =sqlite3.connect("beauty.db")
        conn.execute("INSERT INTO user (username, email, password, confirm)VALUES (?, ?, ?, ?) ", (rusername, remail, rpassword, rconfirm,))
        conn.commit()
        conn.close()

        flash('register successful!', 'success')
        return redirect('/login')
    
    return render_template('register.html')


@app.route('/log',methods=["GET","POST"])
def log():
    if request.method == 'POST':
        memail = request.form.get('email')
        mpassword = request.form.get('password')
        conn =sqlite3.connect("beauty.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE email = ? AND password = ?", (memail,mpassword))
        user = cur.fetchone()
        conn.close()

        if user:
            #session['username'] = user['fullname']
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid username or password', 'danger')
            return redirect('/login')

    return render_template('login.html')



if __name__=='__main__':
    app.run(debug=True)