from socket import ntohl
import streamlit as st
import os
import time
import glob
import os
import pip

from gtts import gTTS
from googletrans import Translator
from langdetect import detect

try:
    os.mkdir("temp")
except:
    pass


st.title("Speech Assistant")
translator = Translator()

text = st.text_input("Nhập chữ vào")

out_lang = st.selectbox(
    "Chọn ngôn ngữ đầu ra",
    ("Tiếng Việt", "Tiếng Anh", "Tiếng Hàn","Tiếng Trung", "Tiếng Nhật"),
)
language={'Tiếng Anh':'en', 'Tiếng Nhật':'ja','Tiếng Việt':'vi','Tiếng Hàn':'ko','Tiếng Trung':'zh-cn'}
output_language=language[out_lang];

english_accent = st.selectbox(
    "Chọn giọng cho tiếng anh",
    ("Mặc định","Anh-Ấn","Anh-Anh","Anh-Mỹ","Anh-Can","Anh-Úc"),
)
accent={'Mặc định':'com','Anh-Ấn':'co.in','Anh-Anh':'co.uk','Anh-Mỹ':'com','Anh-Can':'ca','Anh-Úc':'com.au'}
tld=accent[english_accent];


def text_to_speech(output_language, text, tld):
    translation = translator.translate(text, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text


display_output_text = st.checkbox("Hiện bản dịch")
col1, col2 = st.columns(2)
with col1:
    if st.button("Dịch"):
        result, output_text = text_to_speech(output_language, text, tld)
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Bản nghe:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)

        if display_output_text:
            st.markdown(f"## Bản dịch:")
            st.write(f" {output_text}")

with col2:
    if st.button("Reverse"):
        result, output_text= text_to_speech(detect(text),text ,tld)
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Bản nghe:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        st.write(f"Mã ngôn ngữ của văn bản này có thể là ",detect(text))
        
        if display_output_text:
            st.markdown(f"## Bản dịch:")
            st.write(f" {output_text}")

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
