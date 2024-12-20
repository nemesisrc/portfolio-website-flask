from flask import Flask, render_template, request, redirect, url_for, jsonify

#initialise the flask application
app = Flask(__name__)

#routing endpoints for the flask application
#routing the home page
@app.route('/') 
def homepage():
    return render_template('index.html')

#routing the about page
@app.route('/landing') 
def landing():
    return render_template('landing.html')

#routing the blog page
@app.route('/generic') 
def generic():
    return render_template('generic.html')

#routing the blog page
@app.route('/elements') 
def elements():
    return render_template('elements.html')

#routing the blog page
@app.route('/home') 
def home():
    return redirect('/')

#run the flask application
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)