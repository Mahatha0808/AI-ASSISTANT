import text_to_speeech
import speech_to_text
import datetime 
import webbrowser
import weather

def Action(data):
    user_data=data.lower()
    

    if "what is your name" in user_data:
        text_to_speeech.text_to_speech("My name is vox Assist and i am your virtual assistant")
        return "My name is vox Assist and i am your virtual assistant"
    elif "hello" in user_data or "hey" in user_data:
        text_to_speeech.text_to_speech("Hello sir !,how may i assist you today")
        return "Hello sir !,how may i assist you today"
    elif "shutdown" in user_data:
        text_to_speeech.text_to_speech("ok sir")
        return "ok sir"

    elif "good morning" in user_data:
        text_to_speeech.text_to_speech("good morning sir")
        return "good morning sir"

    elif "what's the time" in user_data:
        current_time=datetime.datetime.now()
        Time=(str)(current_time)+"Hour :",(str)(current_time.minute)+"minute"
        text_to_speeech.text_to_speech(Time)
        return Time

    elif "playmusic" in user_data:
        webbrowser.open("https://music.youtube.com/")
        text_to_speeech.text_to_speech("enjoy your song sir")
        return "enjoy your song sir"
    elif "weather" in user_data:
        result=weather.weather()
        text_to_speeech.text_to_speech(result)
        return result
    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speeech.text_to_speech("enjoy surfing sir")
        return "enjoy surfing sir"

    else:
        text_to_speeech.text_to_speech("not able to understand")
        return "not able to understand"


