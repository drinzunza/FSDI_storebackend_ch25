from flask import Flask, abort
from mock_data import catalog
from about_me import me, test
import json

# create the server/app
app = Flask("server")

@app.route("/", methods=["get"])
def home_page():
    return "Under construction!"


@app.route("/about")
def about_me():
    return "Sergio Inzunza"

@app.route("/myaddress")
def get_address():
    test()
    address = me["address"]
    # return address["street"] + " " + address["city"]
    return f"{address['street']} {address['city']}"


@app.route("/test")
def test():
    return "I'm a simple test"




########################################################
############# API ENDPOINT #############################
########################################################



@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)



# get /api/catalog/count
# return the num of products
@app.route("/api/catalog/count")
def get_count(): 
    count = len(catalog)
    return json.dumps(count)



# get /api/catalog/sum
# return the sum of all prices    $999.00
@app.route("/api/catalog/sum")
def get_sum():
    total = 0
    for prod in catalog:
        total += prod["price"]

    res = f"$ {total}"
    return json.dumps(res)



# get /api/product/<id>
# get a product by its id
@app.route("/api/product/<id>")
def get_product(id):
    for prod in catalog:
        if id == prod["_id"]:
            return json.dumps(prod)

    return abort(404) # 404 = not found



# get /api/product/most_expensive
@app.route("/api/product/most_expensive")
def get_most_expensive():
    pivot = catalog[0]

    for prod in catalog:
        if prod["price"] > pivot["price"]:
            pivot = prod
    
    return json.dumps(pivot)


# start the server
app.run(debug=True)