command = ''
car_started = False
while True:
    command = input().lower()
    if command == 'start':
        if car_started == True:
            print('Car is already started.')
        else:
            car_started = True
            print('Car Started... Ready to go!')
    elif command == 'stop':
        if car_started == False:
            print('Car is already stopped.')
        else:
            car_started = False
            print('Car stopped.')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit game
        ''')
    elif command == 'quit':
        break
    else:
        print("I don't understand that....")
