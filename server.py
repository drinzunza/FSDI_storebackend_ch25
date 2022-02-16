from flask import Flask, abort, request
from mock_data import catalog
from about_me import me, test
import json
import random

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


@app.route("/api/catalog", methods=["POST"])
def save_product():
    product = request.get_json()  # read the payload as a dictionary from json string

    # validate
    # title and longer than 5 chars
    if not "title" in product or len(product["title"]) < 5:
        return abort(400, "There should be a title. Title should be at least 5 chars long.")

    # there should be a price
    if not "price" in product:
        return abort(400, "Price is required.")

    # if the price is not and int AND not a float, error
    if not isinstance(product["price"], int) and not isinstance(product["price"], float):
        return abort(400, "Price is invalid.")

    # the price should be greater than zero
    if product["price"] <= 0:
        return abort(400, "Price should be greater than zero.")

    product["_id"] = random.randint(10000, 50000)
    catalog.append(product)  # save it
    return json.dumps(product)


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


# get /api/categories
# return a list of strings, representing the UNIQUE categories

@app.route("/api/categories")
def get_categories():

    res = []
    for prod in catalog:
        category = prod["category"]

        # if category not exist inside res
        # push category into res
        if not category in res:
            res.append(category)

    return json.dumps(res)


# create an endpoint that allow the client (react) to retrieve
# all the products that belongs to and specified category
# the client will the send the category and expect a list of products in return


# ? what's the ULR ????    /api/catalog/<category>
@app.route("/api/catalog/<category>")
def products_by_category(category):
    res = []
    for prod in catalog:
        if prod["category"] == category:
            res.append(prod)

    return json.dumps(res)


#############################################################
########### API Methods for Coupon codes ####################
#############################################################
coupons = []

# {
#  code: "qwerty"
#  discount: 10
# }

# get all       get /api/coupons
# save new      post  /api/coupons
# get by code   get  /api/coupons/<code>


@app.route("/api/coupons")
def get_coupons():
    return json.dumps(coupons)


@app.route("/api/coupons", methods=["POST"])
def save_coupon():
    coupon = request.get_json()

    # validation

    coupon["_id"] = random.randint(500, 900)
    coupons.append(coupon)

    return json.dumps(coupon)


@app.route("/api/coupons/<code>")
def get_coupon_by_code(code):
    for coupon in coupons:
        if coupon["code"] == code:
            return json.dumps(coupon)

    return abort(404)



# start the server
app.run(debug=True)