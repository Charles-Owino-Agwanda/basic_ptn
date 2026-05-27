capitals = {
    "Kenya": "Nairobi",
    "Uganda": "Kampala",
    "Tanzania": "Dar es salaam",
    "South Africa": "Johannesburg",
}

plants = {"fruits": ["Mango", "Banana"], "flowers": ["Rose", "Lotus"]}
geo = {
    ("India", "USA"): "Countries",
    ("New Delhi", "New York"): "Capitals",
    ("Africa", "Asia"): "Continents",
}


student1_info = dict(name="Charles", age=32, major="Computer Science")
student2_info = dict(name="Kevin", age=33, major="Med")
student3_info = dict(name="Justin", age=30, major="EEE")

del student1_info["major"]  # del method
print(student1_info)

removed_age = student2_info.pop("age")  # pop
print(removed_age)
print(student2_info)

item = student3_info.popitem()  # popitem()
print(item)
print(student3_info)


for key in capitals:
    print(f"{key}, {capitals[key]}")

for value in capitals.values():
    print(f"{value}")

for key, value in capitals.items():
    print(f"{key}, {value}")

print(capitals.get("Kenya"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

if "Kenya" in capitals:
    print("yes")
else:
    print("false")
