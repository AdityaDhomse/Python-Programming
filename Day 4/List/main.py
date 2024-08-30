area_in_pune = ["Kothrud", "Karve Nagar", "Warje"]

# Accessing items in the list
print(area_in_pune[0])
print(area_in_pune[1])
print(area_in_pune[2])

# Modifying items
area_in_pune[2] = "Warje Malwadi"
print(area_in_pune)

# Adding items
area_in_pune.append("Bavdhan")
area_in_pune.append("Katraj")

print(area_in_pune)

# Removing items
area_in_pune.remove("Karve Nagar")

print(area_in_pune)

# Pop() --> Removes & Returns indexed item of the list
popped_item =  area_in_pune.pop(2)  
print(popped_item)

print(area_in_pune)

# Insert an item
area_in_pune.insert(1, "Sadashiv Peth")

print(area_in_pune)

 