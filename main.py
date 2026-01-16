from datetime import date

def log_water():
    water_drank = input('How many ounces of water have you drank today? ')

    try:
        number = int(water_drank)
    except ValueError:
        print('Please enter a valid number.')
        log_water()

    with open('water_log.txt', 'a') as file:
        file.write(f'{date.today()}: {number} ounces\n')

def daily_total():
    todays_total = 0

    with open('water_log.txt', 'r') as file:
        for each_line in file:
            if each_line.startswith(str(date.today())):
                todays_total = todays_total + int(each_line.split(None)[1].strip())

    print(f'You have drank {todays_total} ounces of water today.\n')

def main():
    print('Water Goal Tracker\n------------------\n1. Log Water Drank\n2. View Daily Total\n3. Quit')
    choice = input('Choose an option (1-3):')

    if choice == '1':
        log_water()
        main()
    elif choice == '2':
        daily_total()
        main()
    elif choice == '3':
        print('\nGoodbye! Stay hydrated!')
        quit()
    else:
        print('\nInvalid option, please choose again.\n')
        main()

if __name__ == '__main__':
    main()