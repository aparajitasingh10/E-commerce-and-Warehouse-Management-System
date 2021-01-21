import requests, names, json;
from pprint import pprint;

wms_register = "http://localhost:5000/users/register"
wms_login = "http://localhost:5000/users/login"
wms_searchproduct = "http://localhost:5000/users/searchProduct"
wms_addtocart = "http://localhost:5000/cart/addToCart"
wms_viewcart = "http://localhost:5000/cart/viewCart"
wms_placeOrder = "http://localhost:5000/order/placeOrder"

fake_name = names.get_full_name().replace(' ', '_')
fake_password = "testing123"
fake_email = fake_name + "@wms.com"
fake_phone = "1234567"
product = "5Star"

data = json.dumps(
    {
        'username': fake_name,
        'password': fake_password,
        "email": fake_email,
        "phone": fake_phone,
        "role": 0
    }
)

product_payload = json.dumps(
    {
        'username': fake_name,
        'password': fake_password,
        "name": product,
        "quantity": 5
    }
)

headers = {
    'content-type': "application/json"
}

# API test User Registration

response = requests.request("POST", wms_register, data=data, headers=headers)
print("****************  "+response.json()+"  ****************")
assert response.json() == "Successfully registered"

# Login functionality test

response = requests.request("POST", wms_login, data=data, headers=headers)
print("\n****************  "+response.json()+"  ****************\n")
assert response.json() == "Welcome User " + fake_name

# User Search Product API test

response = requests.request("POST", wms_searchproduct, data=product_payload, headers=headers)
print("\n" + response.json()['message']+"\n")
pprint(response.json()['productDetails'])
assert response.json()['productDetails']["name"] == product

# Use id from the search product api to add to cart
product_id = response.json()['productDetails']["_id"]

# Add to cart functionality API test

response = requests.request("POST", wms_addtocart, data=data, headers=headers)
print("\n"+response.json()+"\n")
assert response.json() == "Created a new cart and Successfully Added Product to the cart!!"


# Login and view Cart API
response = requests.request("POST", wms_viewcart, data=data, headers=headers)
print(response.json())
# assert response.json() == "Created a new cart and Successfully Added Product to the cart!!"



