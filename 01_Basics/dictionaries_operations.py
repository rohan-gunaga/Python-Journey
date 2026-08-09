# dictionaries

birthday = {
    "Rohan": "26/04/2006",
    "Ravi": "4/04/1978",
    "Bhavana": "27/11/2003",
    "Ujwala": "7/01/1979"
    }

print(type(birthday))
print(birthday["Rohan"])
print(birthday["Bhavana"])

print(birthday.get("sudeep","Not Found"))

# adding new values

print("Adding sudeep to the list")
birthday["sudeep"] = "2/09/1973"
print(birthday)

# updating...
print(birthday)
birthday["Rohan"] = "26/04/2007"

print(birthday)

# deleting

print(birthday)
birthday.pop("Rohan")
print(birthday)

# extract keys

print(birthday.keys())
print(birthday.values())