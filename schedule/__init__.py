import main
import time

def show(name):
    print(f"Hello {name}")

def greeting():
    print('How are you?')


main.every().second.do(show, name='amir')
main.every(4).seconds.do(greeting)

while True:
    main.run_pending()
    time.sleep(1)