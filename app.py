from flask import Flask,render_template
app=Flask(__name__,static_folder="static",template_folder="templates")
@app.route('/api')
def func():
    return "<h1>Hello World This is a Flask backend app </h1>"
@app.route('/')
def mfunc():
    return render_template('index.html')
if __name__=="__main__":
    app.run()