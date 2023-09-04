from flask import Flask ,render_template , redirect ,request, session # added session!
app = Flask(__name__)    
app.secret_key = '' # python -c 'import secrets; print(secrets.token_hex())'

@app.route('/')
def home_form():
    if "user_infos" not in session:    
        session["user_infos"] = '' 
        
    return render_template("index.html")


@app.route('/users_form', methods=["POST"])
def users_Form():
    print(request.form)
    session["user_infos"] = request.form
    return render_template("show.html")



@app.route("/destroy_session", methods=["POST"])
def destroy_sess():
    session.clear()
    return redirect("/")



@app.errorhandler(404) # we specify in parameter here the type of error, here it is 404
def page_not_found(error): # (error) is important because it recovers the instance of the error that was thrown
    return f"<h2 style='text-align:center;padding-top:40px'>Sorry! No response. Try again</h2>"


if __name__=="__main__":   
    app.run(debug=True)    