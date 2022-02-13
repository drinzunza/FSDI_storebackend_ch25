

from audioop import add


def print_name():
    print("your name")



def test_dict():
    print("------ Dictionary --------")

    me = {
        "first": "Sergio",
        "last": "Inzunza",
        "age": 35,
        "hobbies": [],
        "address": {
            "street": "evergreen",
            "city": "springfield"
        }
    }


    print(me["first"] + " " + me["last"])


    address = me["address"]
    print(address["street"] + " " + address["city"])



def youger_person():
    ages = [12,42,32,50,56,14,78,30,51,89,12,38,67,10]

    # print the smallest number
    pivot = ages[0]
    for age in ages:
        if age < pivot:
            pivot = age

    print(f"The result is: {pivot}")


print_name()
test_dict()

youger_person()



# function to print your name
# call the function
# run the script