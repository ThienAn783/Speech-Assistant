import streamlit as st
import os
import time
import glob
import os
import pip

from gtts import gTTS
from googletrans import Translator

def install(package):
    pip.main(['install', package])

# Example
if __name__ == '__main__':
    install('gTTS')

try:
    os.mkdir("temp")
except:
    pass
st.title("Speech Assistant")
translator = Translator()

text = st.text_input("Nhập chữ vào")
in_lang = st.selectbox(
    "Chọn ngôn ngữ đầu vào",
    ("Tiếng Việt", "Tiếng Anh", "Tiếng Hàn","Tiếng Hindi", "Tiếng Nhật"),
)
if in_lang == "Tiếng Anh":
    input_language = "en"
elif in_lang == "Tiếng Hindu":
    input_language = "hi"
elif in_lang == "Tiếng Việt":
    input_language = "vi"
elif in_lang == "Tiếng Hàn":
    input_language = "ko"
elif in_lang == "Tiếng Trung":
    input_language = "zh-cn"
elif in_lang == "Tiếng Nhật":
    input_language = "ja"

out_lang = st.selectbox(
    "Chọn ngôn ngữ đầu ra",
    ("Tiếng Việt", "Tiếng Anh", "Tiếng Hàn","Tiếng Hindi", "Tiếng Nhật"),
)
if out_lang == "Tiếng Anh":
    output_language = "en"
elif out_lang == "Tiếng Hindi":
    output_language = "hi"
elif out_lang == "Tiếng Việt":
    output_language = "vi"
elif out_lang == "Tiếng Hàn":
    output_language = "ko"
elif out_lang == "Tiếng Trung":
    output_language = "zh-cn"
elif out_lang == "Tiếng Nhật":
    output_language = "ja"

english_accent = st.selectbox(
    "Chọn giọng cho tiếng anh",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
)

if english_accent == "Default":
    tld = "com"
elif english_accent == "India":
    tld = "co.in"

elif english_accent == "United Kingdom":
    tld = "co.uk"
elif english_accent == "United States":
    tld = "com"
elif english_accent == "Canada":
    tld = "ca"
elif english_accent == "Australia":
    tld = "com.au"
elif english_accent == "Ireland":
    tld = "ie"
elif english_accent == "South Africa":
    tld = "co.za"


def text_to_speech(input_language, output_language, text, tld):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text


display_output_text = st.checkbox("Hiện bản dịch")

if st.button("Dịch"):
    result, output_text = text_to_speech(input_language, output_language, text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Bản nghe:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

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
