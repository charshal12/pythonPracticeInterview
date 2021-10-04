import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening ......')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

'''def send_email_hard_coded():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('fresh.testautopy@gmail.com', 'test@123!')
    server.sendmail('fresh.testautopy@gmail.com',
                    'charshal0100@gmail.com',
                    'Hi dude make sure you join the party tonight!!!!')'''

#Send dynamic emails
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('fresh.testautopy@gmail.com', 'test@123!')
    email = EmailMessage()
    email["From"] = 'fresh.testautopy@gmail.com'
    email['To']= receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

#We will be converting message from text to speech


email_list = {"li":"charshal000@gmail.com",
                       "mark":"mark@gmail.com" }

def get_email_info():
        talk("To whom you want to send email: ")
        name = get_info()
        receiver = email_list[name]
        print(receiver)

        talk("What is the Subject of the Email")
        subject = get_info()

        talk("Tell me the  content of the Email")
        message = get_info()
        send_email(receiver,subject,message)

        talk("Hey lazy ass. Your email is sent")
        talk("Do you want to send more email?")
        send_more = get_info()
        if "yes" in send_more:
            get_email_info()


get_email_info()
