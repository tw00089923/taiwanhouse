from app import app

from flask import redirect, render_template, url_for, request, jsonify, flash, make_response, session, Response, stream_with_context

from app import api, login_manager

from flask_login import UserMixin, login_required, login_user, logout_user

from flask_jwt import  current_identity, jwt_required

from datetime import datetime, timedelta


# https://apscheduler.readthedocs.io/en/latest/ # 定時執行

"""
@app.before_request
def user_login():
"""
'''
只做資料庫引出與傳送

'''

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/",methods=["POST","GET"])
def login():
    error = {}
    username = ""
    if hasattr(session,"username")  :
        username = session["username"]
    if request.method == "POST":
        form = request.form
        #password = request.form["password"]
        user = User.query.filter_by(username=form["username"]).first()
        if not user :
            error = {'error':"使用者不存在"}
            return render_template("auth/login.html",error=error,username=username)
        else :
            if not user.check_password(form["password"]):
                error= {'error':"密碼錯誤"}
                print(message)
            else:
                login_user(user, remember=True)
                return redirect("/dashboard")
        return render_template("auth/login.html",username=username)
        print(user)
    return render_template("auth/login.html",error=error,username=username)

@app.route("/api")
def api():    
    #print(os.path.exists(os.path.dirname(app.root_path+"/README.md")))
    with open(app.root_path + '/README.md','r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


@app.route('/protected',methods=["POST","GET"])
@jwt_required()
def protected():
    print("this protected is successed!!!")
    return '%s' % current_identity


