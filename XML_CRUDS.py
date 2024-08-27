import xml.etree.ElementTree as ET
import os

# Function to load existing data from the XML file
def load_data(filename):
    # Check if file exists and is not empty
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        # Return empty list if the file doesn't exist or is empty
        return []

    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        items = []

        for item_element in root.findall('item'):
            item_id = item_element.get('id')
            description = item_element.find('description').text
            price = float(item_element.find('price').text)
            items.append({
                "item_id": item_id,
                "description": description,
                "price": price
            })

        return items
    except ET.ParseError:
        print("Error: The XML file is malformed.")
        return []

# Function to save data into the XML file
def save_data(items, filename):
    root = ET.Element("items")

    for item in items:
        item_element = ET.SubElement(root, "item")
        item_element.set("id", item["item_id"])

        description = ET.SubElement(item_element, "description")
        description.text = item["description"]

        price = ET.SubElement(item_element, "price")
        price.text = str(item["price"])

    tree = ET.ElementTree(root)
    tree.write(filename)
    print("Data saved to file!")

# Create Operation
def create_item(items):
    item_id = input("Enter New ItemID: ")
    item_description = input("Enter Description of the Item: ")
    item_price = input("Enter Price of the Item: ")

    try:
        price = float(item_price)
        item = {
            "item_id": item_id,
            "description": item_description,
            "price": price
        }
        items.append(item)
        print("Item created successfully!")
    except ValueError:
        print("Invalid price entered. Please enter a valid number for the price.")

# Read Operation
def read_items(items):
    if items:
        print("\nCurrent Items in the XML:")
        for item in items:
            print(f"ID: {item['item_id']}, Description: {item['description']}, Price: {item['price']}")
    else:
        print("No items found.")

# Update Operation
def update_item(items):
    item_id = input("Enter ItemID to Update: ")
    for item in items:
        if item['item_id'] == item_id:
            item['description'] = input("Enter New Description: ")
            item['price'] = float(input("Enter New Price: "))
            print("Item updated successfully!")
            return
    print("Item not found!")

# Delete Operation
def delete_item(items):
    item_id = input("Enter ItemID to Delete: ")
    for item in items:
        if item['item_id'] == item_id:
            items.remove(item)
            print("Item deleted successfully!")
            return
    print("Item not found!")

# Search Operation
def search_item(items):
    item_id = input("Enter ItemID to Search: ")
    for item in items:
        if item['item_id'] == item_id:
            print(f"ID: {item['item_id']}, Description: {item['description']}, Price: {item['price']}")
            return
    print("Item not found!")

if __name__ == "__main__":
    filename = "item_data.xml"
    items = load_data(filename)

    while True:
        print("\nChoose an operation:")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            create_item(items)
            save_data(items, filename)
        elif choice == "2":
            read_items(items)
        elif choice == "3":
            update_item(items)
            save_data(items, filename)
        elif choice == "4":
            delete_item(items)
            save_data(items, filename)
        elif choice == "5":
            search_item(items)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")
