def userData(**user: dict) -> dict:
    print(user["id"])
    print(user["name"])
    print(user["city"])

userData(id=1, name="Yasir", city="New Delhi")
