import main
import time

def show(name):
    print(f"Hello {name}")

def greeting():
    print('How are you?')


main.every().hour.at(':05').do(show, name='Mahdi')

while True:
    main.run_pending()
    time.sleep(1)