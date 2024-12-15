from flask import Flask, render_template, request, redirect, url_for, jsonify

#initialise the flask application
app = Flask(__name__)

#routing endpoints for the flask application
@app.route('/') #home page route
def homepage():
    return render_template('index.html')

@app.route('/about') #about page route
def about():
    return render_template('about.html')


#run the flask application
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)