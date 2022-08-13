from tkinter import W
from typing import Text
import streamlit as st
import os
import time
import glob
from mtranslete import translate
import pandas as pd
from gtts import gTTS
import base64
from googletrans import Translator
try:
    oss.mkdir("temp")
except:
    pass

st.title("Speech Assistant")

col1 , col2, col3 = st.column(3)
with col1:
inputtext = st.text_area("Nhập vào")
with col2:
in_lang = st.selectbox(
    "Chọn ngôn ngữ của bạn",
    ("Tiếng Việt", "Tiếng Đức" ,  "Tiếng Anh" , "Tiếng Hindi" , "Tiếng Nhật" ,"Tiếng Trung"),
)
if in_lang == "Tiếng Anh":
    input_language = "en"
elif in_lang == "Tiếng Hindi":
    input_language = "hi"
elif in_lang == "Tiếng Nhật":
    input_language = "ja"
elif in_lang == "Tiếng Trung":
    input_language = "zh-CN"
elif in_lang == "Tiếng Đức":
    input_language = "de"
elif in_lang == "Tiếng Việt":
    input_language = "vi"

out_lang = st.selectbox(
    "Chọn ngôn ngữ đầu ra",
    (("Tiếng Việt", "Tiếng Đức" ,  "Tiếng Anh" , "Tiếng Hindi" , "Tiếng Nhật" ,"Tiếng Trung"),
)
if out_lang == "Tiếng Anh":
    output_language = "en"
elif out_lang == "Tiếng Hindi":
    output_language = "hi"
elif out_lang == "Tiếng Nhật":
    output_language = "ja"
elif out_lang == "Tiếng Trung":
    output_language = "zh-CN"
elif out_lang == "Tiếng Đức":
    output_language = "de"
elif out_lang == "Tiếng Việt":
    output_language = "vi"
with col3:
def text_to_speech(input_language, output_language,)
    translation = translator.translate(text, src=input_language , dest=output_language)
    trans_text = translation.text 
    tts = gTTS(trans_text, lang= output_language,slow=False)
    try:
        my_file_name = text[0:20]
        except:
            my_file_name = "audio"
        tts.save(f"temp/{my_file_name}.mp3")
        return my_file_name, trans_text
if st.button("convert")
        result, output_text = text_to_speech(input_language,out_language,text)
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Audio")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)

        if display_output_text:
            st.markdown(f"## Bản dịch:")
            st.write(f" {output_text}")

def remove_files(n):
        mp3_files = glob.glob("temp/*mp3")
        if len(mp3_files) !=0:
            now = time.time()
            n_days = n* 86400
            for f in mp3_files:
                if os.stat(f).st_mtime < now - n_days:
                    os.remove(f)
                    print("Deleted",f)
remove_files(7)