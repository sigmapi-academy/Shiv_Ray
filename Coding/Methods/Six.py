def details(name, city = 'Kolkata',pincode=700001):
    print(f'Name: {name}')
    print(f'City: {city}')
    print(f'Pincode: {pincode}')
    
    
details("Amit", "Delhi", 700011)
# Keyword arguments
details(pincode=700084, name='Shiv', city='Kolkata')
details('Sankar')
details('Yash', 'Mumbai')