c = int(input('1. Bike\n2. Auto\n3. Car\n\nEnter your choice: '))

bikefare = 5
autofare = 10
carfare = 15

km = int(input('Enter the distance travelled in km: '))

fare = 0

if c == 1:
    fare = km * bikefare
elif c == 2:
    fare = km * autofare
elif c == 3:
    fare = km * carfare
else:
    print('Invalid option')
    
print('Your fare is ', fare)
