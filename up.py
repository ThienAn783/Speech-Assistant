import speech_recognition as spr
import pyaudio
t = spr.Recognizer()
with spr.Recognizer() as source:
  print("Xin mời nói:")
  audio = t.listen(source)
  try:
    text = t.recognize_google(audio,language="vi-VI")
    print("Bạn đã nói: {}".format(text))
  except:
    print("Không nhận được voice")
