secNumber = int(input('Enter number of second:\n'))
secDay = 24 * 60 * 60
choice = input('Enter, what do you want to count to midnight: sec, min or hours:\n')
hours = (secDay - secNumber) // 60 // 60
minutes = (secDay - secNumber) // 60
seconds = (secDay - secNumber)
if choice == 'sec':
    print(seconds)
elif choice == 'min':
        print(minutes)
else:
    print(hours)

