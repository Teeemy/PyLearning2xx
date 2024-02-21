# real example of dict which is similar to  json
api_response = {
        "first_name": "Temitope",
        "age": 32,
        "last_name": "Onibon",
        "email": "onibonoje@gmail.com",
        "password": "Oyinkansola",
        "commission": 1000
}
print(api_response)
print(type(api_response))
print(api_response.get("first_name"))
print(api_response["age"])
print(len(api_response))
api_response["password"] = "kansola" # dict is mutable i.e values can be changed
print(api_response)

for k,v in api_response.items(): # to iterates the value
        print(k,v)