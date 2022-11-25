from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)  
app.secret_key= "keep it safe"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/checkout', methods=['POST'])
def check():
    total=int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    session['str']=request.form['strawberry']
    session['res']=request.form['raspberry']
    session['app']=request.form['apple']
    session['first_name']=request.form['first_name']
    session['last_name']=request.form['last_name']
    session['id']=request.form['student_id']
    session['sum']=total
    return redirect('/checkout')

@app.route('/checkout')
def show_result():
    return render_template('checkout.html',str=session['str'],res=session['res'],app=session['app'],firstname=session['first_name'],finalname=session['last_name'],id=session['id']
    )
@app.route('/fruits')
def display_fruit():
    session['fruit_picture']=['apple.png' ,'blackberry.png','raspberry.png','strawberry.png']
    return render_template('fruits.html')

if __name__=="__main__":   
    app.run(debug=True)    