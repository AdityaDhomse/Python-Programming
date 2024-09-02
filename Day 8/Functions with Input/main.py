def greet():
    print("How are you?")
    print("How you doin'")
    
def greet_with_name(name):
    print(f"How are you {name}?")
    print(f"How you doing, {name}?")

greet()
greet_with_name("Aditya")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")
    
greet_with("Aditya", "London")

greet_with(location="Pune", name="Rahul")