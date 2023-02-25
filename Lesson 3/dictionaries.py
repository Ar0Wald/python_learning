person = {"name": "Alice", 
          "age": 30,
          "location": "New York"
}

print(person["name"])

person["age"] = 31
print(person)

del person ["location"]
print(person)

person["gender"] = "Female"
print(person)
