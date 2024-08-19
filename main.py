import speech_recognition
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import font


root = Tk()
# "500 * 300"
root.geometry("")
root.title("Voice to text")

def voiceReco():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio,language='ar-AR')
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        print(bidi_text)
        textF.delete("1.0","end")
        textF.insert(END,bidi_text)
        textF.tag_add("center",1.0,"end")

BttonFont = font.Font(size=20)
LabelFont = font.Font(size=15)

Label(root,text="voice is here",font=LabelFont).pack()

textF = Text(root,height=5, width=52,font=LabelFont,)
textF.tag_configure("center", justify='center')
textF.pack()

Button(root,text='listen',font=BttonFont, command=voiceReco).place(x=220,y=200)

root.mainloop()