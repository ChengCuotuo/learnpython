import random
import easygui
secret=random.randint(1,99)
guess=0
tries=0
easygui.msgbox("I have a secret, It is a number from 1 to 99. I will give you 6 tries")
while guess!=secret and tries<6:
       guess=easygui.integerbox("what is your guess")
       if not guess:break
       if guess<secret:
              easygui.msgbox(str(guess)+" is too low, try again")
       elif guess>secret:
              easygui.msgbox(str(guess)+"too high, try again")
       tries=tries+1
       if guess == secret:
              easygui.msgbox("you got it! found your secret, good!")
       else:
              easygui.msgbox("no more guess,better luck next time")
              easygui.msgbox("the secret number was:" + str(secret))

