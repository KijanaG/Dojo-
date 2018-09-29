class Product: 
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(tax):
        self.price = (1+tax)* self.price
        return self.price
    def return_item(reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
        elif reason_for_return == "like-new":
            self.status = "like new"
        elif reason_for_return == "opened":
            self.status = "opened"
        return self
    def display_info(self):
        print("Price: ", self.price)
        print("Item Name: ", self.item_name)
        print("Weight: ", self.weight, "lbs")
        print("Brand: ", self.brand)
        print("Status: ", self.status)
    