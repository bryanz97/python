from flask import Flask, app,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    titulo='Hola Bryan'
    return render_template('index.html',ejemplo=titulo)

if __name__ : '__main__'
app.run(port=5000,debug=True)