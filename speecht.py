import speech_recognition as st
r=st.Recognizer()
with st.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("say something")
    a=r.listen(source)
    text=r.recognize_google(a)
    print(text)