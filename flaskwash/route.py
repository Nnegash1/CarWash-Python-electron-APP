from flask import redirect, url_for,render_template, request
from flaskwash import app, db, admin
from flask_admin.contrib.sqla import ModelView
from flaskwash.create_db import Worker, Client, Item
  
#check workers name in the dataset
@app.route("/workertable", methods=["GET", "POST"])
def index():
    workers = Worker.query.all()  
    app.logger.info("The type returned:", type(workers))
    return render_template("WorkersTable.html", workers = workers)

#check items inside the stock database
@app.route("/stock", methods=["GET", "POST"])
def stock():
    item = Item.query.all()   
    return render_template("itemTable.html", item = item)


'''
Add item to the data base; if it exists 
return without adding.
'''
@app.route("/item", methods=["GET","POST"])
def new_item():
    if request.method == "POST":
        def_val = None
        item_name = request.form.get("item_name", def_val)
        item_price = request.form.get("price", def_val)
        qty = request.form.get("qty", def_val)
        total_cost = 10
        item = Item(item_name, qty, item_price, total_cost)
        db.session.add(item)
        db.session.commit()
    return render_template("itemForm.html")

'''
Add workers to the data base
'''
@app.route("/workerform", methods=["GET", "POST"])
def worker_form_index():
    if request.method == "POST":
        default_name = "Error"
        first_name = request.form.get("first_name", default_name)
        last_name = request.form.get("last_name", default_name)
        email = request.form.get("email", default_name)
        phone_number = request.form.get("phone", default_name)
        
        worker = Worker(first_name, last_name, email, phone_number)
        db.session.add(worker)
        db.session.commit()

    return render_template("Workersform.html")

@app.route("/clientform", methods=["GET","POST"])
def client_form_index():
    
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone")
        plate_number = request.form.get("plate")
        vehicle_brand = request.form.get("brand")
        #if first_name == None or last_name == None
        client = Client(first_name, last_name, email, phone_number, plate_number, vehicle_brand)
        db.session.add(client)
        db.session.commit()

    return render_template("Clientform.html")

@app.route("/clientTable", methods=["GET", "POST"])
def client_table():
    client = Client.query.all() 
    if client == None:
        return
    return render_template("ClientTable.html", client=client)

# @app.route("/chart")
# def bar_chart():
#     incomings = [121212, 5312, 6251, 7841, 9821, 14984]
#     return render_template("chart.html")

@app.route("/dashboard")
def dashbord():
    return render_template("dashboard.html")

@app.route("/")
def home():
    return render_template("dashboard.html")

admin.add_view(ModelView(Item, db.session))
admin.add_view(ModelView(Worker, db.session))

