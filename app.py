from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session


from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def home():
	return render_template("home.html")

@app.route('/store')
def store():
	products=query_all()
	return render_template("store.html",products=products)
@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/cart')
def cart():
	products=[]
	cart_products=session.query(Cart).all()
	for id1 in cart_products:
		products.append(query_by_id(id1.productID))
	return render_template('cart.html',products=products)

@app.route('/add_to_cart/<int:p_id>')
def add_to_cart(p_id):
	add_To_Cart(p_id)

	return redirect(url_for("cart"))
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
	 	return render_template("login.html")
	else:
		username=request.form['uname']
		password=request.form['psw']

		if username=="noy" and password==1234:
			return render_template("portal.html")
		return render_template("login.html")


@app.route('/portal')
def portal():
	return render_template("portal.html")







if __name__ == '__main__':
    app.run(debug=True)