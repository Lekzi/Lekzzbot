import time as t
import os
t.sleep(3)
os.system("clear")
print("\33[1;32;40m")
e = """\033[01;91mInvalid option!
Choose a valid option!"""
print("""
            +-+-+-+-+-+-+-+-+
            |L|E|K|Z|I|B|O|T|    
            +-+-+-+-+-+-+-+-+
""")
print("""Hello dear☺,My name is  Twii l am fun to be with and chat with.I am friendly.
I also sells cardro pro,xcaret100 and their activation codes..I also sell some other stuffs""")
print("""
Rules:{1}No insultive words or u will be punished.
{2}No bad words like \"Fuck\".
{3}Don't ask silly questions""")
print("""
[A] Business Chat
[B] Friendly Chat
[C] Update me""")
c = input("What kind of chat do u prefer? ")
t.sleep(3)
os.system("clear")
if c == "A":
  print("Let's talk about business 🤑🤑 ")
  print("""
  [1] Hacking tools
  [2] Exam runs""")
  c2 = input("What type of business? ")
  t.sleep(3)
  os.system("clear") 
  if c2 == "1":
    print("Contact Lekzi for hacking tools")
  elif c2 == "2":
    print("Contact Lekzi for hacking tools")
  else:
    print(e)
    os.system("python3 Lekzi.py")
  os.system("xdg-open https://wa.me/07064822519")
elif c == "B":
  print("[A] Jokes")
  c3 = input("What type of chat? ")
  os.system("clear")
  if c3 == "A":
    print("""
    What do Alexander the Great and Winnie the Pooh have in common? Same middle name.
    I was horrified when my wife told me that my six-year-old son wasn't actually mine. Apparently I need to pay more attention during school pick-up.
    I have a joke about time travel, but I'm not gonna share it. You guys didn't like it.
    I'm thinking of a career where I estimate crowd sizes at different outdoor events. I wonder how many people are in that field.""")
elif c == "C":
  print("Updating...")
  t.sleep(6)
  os.system("""
  cd $HOME
  rm -f -r Lekzleap
  git clone https://github.com/Lekzi/Lekzleap""")
  print("""Now type
  cd
  cd Lekzleap
  python3 Lekzi.py""")
  exit()
  
else:
  print(e)
  os.system("python3 Lekzi.py")
op = input("Do you wanna continue? Y/N: ")
if op == "Y":
  os.system("python3 Lekzi.py")
elif op == "y":
  os.system("python3 Lekzi.py")
else:
  print("Goodbye 👋👋")
  exit()