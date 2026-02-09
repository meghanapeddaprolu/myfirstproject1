Application_name="MakeUP_App"
Min_stock=5
Reordering_limit=20
Inventory_history=[20,10,5,8]
store_locations={"store1","store2"}
product1={      "name":"LIP GLOSS",
                 "Category":"Makeup",
                 "product_id":"1",
                 "location":"store1",
                 "stock":13 }

##Display Inventory History##
def display_inventory_history():
    print(Inventory_history)
def update_inventory_history():
    value = int(input("enter what to add:"))
    Inventory_history.append(value)
    print(Inventory_history)
    
def display_store_locations():
    print(product1["location"]) 
    
def check_stock_levels():
    if product1["stock"] <= Min_stock:
        print(f"{product1['name']} stock levels are low there are {product1['stock']} left ")
    else:
        print(f"{product1['name']} stock levels are sufficient")   
        
def Calculate_Reorder_Levels():
    if product1["stock"]<=Min_stock:
        print(f"we have to order more {Reordering_limit-product1['stock']} of {product1['name']}")
        

def Update_Product_Details():
    print("\nWhat do you want to update?")
    print("1 - Stock")
    print("2 - Location")
    print("3 - Name")

    choice = int(input("Enter choice: "))

    if choice == 1:
        new = int(input("Enter new stock value: "))
        product1["stock"] = new

    elif choice == 2:
        new = input("Enter new location: ")
        product1["location"] = new
        store_locations.add(new)      # also add to set

    elif choice == 3:
        new = input("Enter new product name: ")
        product1["name"] = new

    else:
        print("Invalid choice")

    print("Updated Successfully!")

    
    
        
Update_Product_Details()
display_inventory_history()
update_inventory_history()
display_store_locations()
check_stock_levels()
Calculate_Reorder_Levels()
