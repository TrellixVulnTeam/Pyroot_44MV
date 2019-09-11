from flask import Flask, redirect, url_for, request , render_template , make_response


app = Flask(__name__)

@app.route('/hello/')  # specified the url 
def hello():
    return 'Hello Flask world'

# @app.route('/new')
# def new():
#     return 'The new me '

# @app.route('/old/')
# def old():
#     return 'The old me'

# profile url binding with string 

# @app.route('/profile/<name>')
# def profile_name(name):
#     return 'This is the profile of %s' % name

#profile url binding with int 

# @app.route('/profile/<int:id>')
# def profile_id(id):
#     return 'This is the profile of %d' % id

# for admin and guest 

# url  for admin 

# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'

# url binding for guest 

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'Hello Guest %s' % guest

# url user check admin / guest 

# @app.route('/user/<type>')
# def hello_user(type):
#     if type == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=type))

# ----------------------


# home page 

@app.route('/')
def index():
    return 'Welcome to Flask'

# Welcome page with an user 

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('hellotemplate.html', name= username)   # renders the template 

# Use of the login html created 

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name

# use the GET and POST methods 
# Open this login html separately 

@app.route ('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        username = request.form['nm']      # to get the field from form 
        return redirect(url_for('success',name=username))
    else:
        username = request.args.get('nm')  # to get the field from form using get 
        return redirect(url_for('success', name=username))


# accessing the js file 
@app.route('/accessjs')
def js():
    return render_template('js.html')


# accessing the student html 
@app.route('/student')
def student():
    return render_template('student.html')  # with the subject details form

# accessing the result html 
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)



# cookies 
# for the cookie form 
@app.route('/cookies')
def cookies():
    return render_template('cookiesform.html')   # has the url to set cookies 

# set cookie 
@app.route('/setcookies', methods=['POST','GET'])  # route to set cookies 
def setcookies():
    if request.method == 'POST':
        username = request.form['nm']
        resp = make_response(render_template('readcookies.html'))   # to read the cookies - make_response - url for getcookies
        resp.set_cookie('userId', username)                         # setting the cookie for the specific user 
    return resp
    
# get cookies route 
@app.route('/getcookies')   # route for the getcookies 
def getcookies():
    name = request.cookies.get('userId')     # gets the userid from the set cookie thingy 
    return '<h1>Hello'+ name +'</h1>'




# to run the server 
if __name__ == '__main__':
    app.run()
