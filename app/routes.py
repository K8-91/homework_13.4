from app import app, db
from flask import request, redirect, url_for, render_template
from app.models import Book, Author, Rental, Shopping
from app.forms import BookForm, ShoppingForm


#@app.route("/todos/", methods=["GET", "POST"])
#def book_list():
    #if request.method == "POST":
        #form = TodoForm(data=request.form)
        #if form.validate_on_submit():
            #new_book = Book()
            #new_book.tittle = form.data.tittle
            #new_book.author_name = form.data.author
            #new_book.rental_status = form.data.status
            #db.session.add(new_book)
            #db.session.commit()
        #return True
    #return True

@app.route("/shopping/", methods=["GET", "POST"])
def shopping_list():
    if request.method == "POST":
        form = ShoppingForm(request.form)
        new_list = Shopping()
        if form.validate_on_submit():
            new_list.product = request.form("product")
            new_list.quantity = request.form("quantity")
            db.session.add(new_list)
            db.session.commit()
        return redirect((url_for("shopping_list")))
    return render_template("shopping.html", form=form)


