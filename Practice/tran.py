def TravelCost(days, vehicle):
    if vehicle == "POV":
        transportation = 50
    else:
        transportation = 0
    return (days * (60 + 95)) + transportation


def PurchaseCost(amount):
    if amount < 100:
        return amount
    else:
        return 100.00


def ParkingCost(lot):
    if lot == "A":
        return 125
    elif lot == "B":
        return 95
    else:
        return 70


def PrintHeader():
    print("{}".format("Employee"), end="")
    print("\t{}".format("Transaction"), end="")
    print("\t{}".format("+/-"), end="")
    print("\t{}".format("Amount"))
    print("-"*46)


def PrintRecord(name, transType, amount):
    print("{:<8}".format(name), end="")
    print("\t{:>10}".format(transType), end="")
    print("\t{:^4}".format("+" if transType == "Parking" else "-"), end="")
    print("\t{:>6.2f}".format(amount))


def main():
    file = open("transactions.py")
    employee = file.readline().strip()
    PrintHeader()
    travel_count = 0
    purchase_count = 0
    parking_count = 0
    max_amt = 0
    max_emp = ""

    while(employee != "X"):
        transaction = file.readline().strip()
        if transaction == "Travel":
            days = int(file.readline().strip())
            vehicle_type = file.readline().strip()
            expense = TravelCost(days, vehicle_type)
            travel_count += 1

        if transaction == "Purchase":
            amount = float(file.readline().strip())
            expense = PurchaseCost(amount)
            purchase_count += 1

        if transaction == "Parking":
            lot = file.readline().strip()
            expense = ParkingCost(lot)
            parking_count += 1

        if expense > max_amt:
            max_amt = expense
            max_emp = employee
        PrintRecord(employee, transaction, expense)
        employee = file.readline().strip()
    print("-"*46)
    print("{:<25}" .format("Total Travel Receipts:"), end=" ")
    print(f"{travel_count:>4}")
    print("{:<25}" .format("Total Purchase Receipts:"), end=" ")
    print(f"{purchase_count:>4}")
    print("{:<25}" .format("Total Parking Receipts:"), end=" ")
    print(f"{parking_count:>4}")
    print(f"Max receipt amount:  $ {max_amt} from {max_emp}")


if __name__ == "__main__":
    main()
