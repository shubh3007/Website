from flask import Flask, render_template

app = Flask(__name__) #this objects calls the script
'''
case 1: Script exrcuted: __name__ = "__main__"
Case 2: Script imported by another class __name__= "Script1"
'''
@app.route('/') #localhost:5000
def homepage():
    return render_template("layout.html")

@app.route('/ashish/') #localhost:5000/ashish
def ashish():
    return render_template("ashish.html") #output

@app.route('/about/') #localhost:5000/about
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)