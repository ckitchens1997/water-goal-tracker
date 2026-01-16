import os

"""
Simple Water Intake Tracker
Tracks daily water intake and logs it to a file.
"""

from datetime import date, timedelta

DAILY_GOAL_OZ = 64 # Daily water intake goal in ounces

# Clear the console screen
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(title):
    width = 30
    print()
    print('=' * width)
    print(title.center(width))
    print('=' * width)
    print()

# Log the amount of water drank today
def log_water(): 
    print()
    header('Log Water Intake')
    water_drank = input('How many ounces of water have you drank today? ')

    try:
        number = int(water_drank)
    except ValueError:
        print('Please enter a valid number.')
        log_water()

    confirm = input(f'\nYou are about to log {number} ounces of water today. Confirm? (y/n) ').strip().lower()
    if confirm == 'y':
        with open('water_log.txt', 'a') as file:
            file.write(f'{date.today()}: {number} ounces\n')
            print()
    elif confirm == 'n':
        print('Log cancelled.\n')
    else: 
        print('\nInvalid input, please try again.\n')
        log_water()


# Calculate and display today's total water intake
def daily_total(): 
    header('Daily Total')
    todays_total = 0

    with open('water_log.txt', 'r') as file:
        for each_line in file:
            if each_line.startswith(str(date.today())):
                todays_total = todays_total + int(each_line.split(None)[1].strip())

    print(f'\nYou have drank {todays_total} ounces of water today.')

    if todays_total < DAILY_GOAL_OZ:
        print(f'You need to drink {DAILY_GOAL_OZ - todays_total} more ounces to reach your daily goal of {DAILY_GOAL_OZ} ounces.\n')
    else:
        print('Congratulations! You have reached your daily water intake goal!\n')

def weekly_totals():
    header('Weekly Totals')
    today = date.today()
    weekly_total = 0
  
    last_7_days = []
    for i in range(7):
        day = today - timedelta(days = i)
        last_7_days.append(day.isoformat())
        for each_line in open('water_log.txt', 'r'):
            if each_line.startswith(day.isoformat()):
                ounces = int(each_line.split(None)[1].strip())
                weekly_total += ounces

    print(f'\nWeekly Total: {weekly_total}')
    print(f'Weekly Average: {weekly_total / 7:.2f} ounces\n')


# Main menu for user interaction
def main():
    clearscreen()
    print()
    while True:
        header('Water Goal Tracker')
        print('1. Log Water Intake')
        print('2. View Daily Total')
        print('3. View Weekly Totals')
        print('4. Exit\n')

        choice = input('Choose an option (1-4): ').strip()
        if choice == '1':
            log_water()
        elif choice == '2':
            daily_total()
        elif choice == '3':
            weekly_totals()
        elif choice == '4':
            print('\nGoodbye! Stay hydrated!\n')
            break
        else:
            print('Invalid choice. Please select 1, 2, 3, or 4.')


if __name__ == '__main__':
    main()