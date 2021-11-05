favcar = {
    'JJ' : ['Golf', 'Camry', 'LFA'],
    'Nicklas' : ['Innova', 'Panther', 'Fortuner'],
    'James': ['Avanza', 'Lamborghini', 'Bugatti'],
    'Tate' : ['Livina', 'HRV', 'Rocky'],
    'Man' : ['Mazda','Harrier', 'Mini Cooper']
}
for name in favcar : #applies to the keys in the dictionary only, without the lists inside each key
    print(f"{name} likes these cars :")
    for car in (favcar[name]) : #applies to the lists inside each keys in the dictionary favcar
        print("-", car)
    print() #adds an extra space after the previous name's last favourite car being declared