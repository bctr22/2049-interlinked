import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")
    
    try:
        audio_data = r.listen(source, timeout=5)
        text = r.recognize_google(audio_data)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
