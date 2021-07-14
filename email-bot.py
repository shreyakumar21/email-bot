import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('Email', 'Email_password') #give access to google account
    email = EmailMessage()
    email['From'] = 'Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'Shreya': 'shreyakumar603@gmail.com',
    'Sneha': 'snehajed@gmail.com',
}

def get_email_info():
    speak('Who do you want to send the mail to?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    speak('Subject of your mail:')
    subject = get_info()
    speak('Content of the mail:')
    message = get_info()
    send_email(receiver, subject, message)
    speak('Your email is sent!!!')
    speak('Do you want to send another email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()