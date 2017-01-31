#!/usr/bin/env python
# password_locker.py - An insecure password locker program

# Takes in a command line argument that is the account's name ( email || blog)
# emails pass will be copied to the clipboard - so that the user can paste it into the pass field

# solution: users can have long passes without havng to memorize them

# Step 1.
# Our model
PASSWORDS = {"gmail": "keyboard_abc123",
             "youtube": "abra_cadabra_inDaHouse",
             "luggage": "12345"}

# step 3. - copy the right password
# import sys ( to access command line args ) & pyperclip( to access the clipboard)
import sys, pyperclip
if len(sys.argv) < 2:
    print("Usage: python password_locker.py [account/email] - copy account password")
    sys.exit()

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
