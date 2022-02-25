import main
import time

def show(name):
    print(f"Hello {name}")

def greeting():
    print('How are you?')


main.every(6).seconds.do(show, name='amir')
main.every(4).seconds.do(greeting)

while True:
    main.run_pending()
    print(main.idle_seconds())
    time.sleep(1)