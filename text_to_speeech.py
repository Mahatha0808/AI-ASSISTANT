import pyttsx3


text="how are you"
engine=pyttsx3.init()
rate=engine.getProperty("rate")
engine.setProperty("rate","rate-100")
engine.say(text)
engine.runAndWait()