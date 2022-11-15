import streamlit as st
import qrcode
from datetime import datetime
from PIL import Image

st.title('QR-Code Streamlit App')

s = st.text_input('Type in the box below')

img = qrcode.make(s)

def get_filename():
    # Getting the current date and time
    dt = datetime.now()
    # getting the timestamp
    ts = datetime.timestamp(dt)
    ts_0 = str(ts).split(".")[0]
    return ts_0

fn = get_filename()

img.save("Img{}.jpg".format(fn))

img_0 = Image.open("Img{}.jpg".format(fn))

st.image(img_0, caption=s.split(" "))

st.write(f'{s}')

