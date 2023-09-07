import requests
import streamlit as st

import urllib.request
from PIL import Image
  
# Retrieving the resource located at the URL
# and storing it in the file name a.png


  
# Opening the image and displaying it (to confirm its presence)


API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {'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'}"}

st.title("Image Captioning")


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
    
#Function for image upload
def upload_image():
    uploaded_file=st.sidebar.file_uploader("Upload image", accept_multiple_files=False)
    submit=st.sidebar.button("Submit")

    if uploaded_file is not None and submit:
        with open('file.jpg', 'wb') as f:
          f.write(uploaded_file.read())
          f.close()
        st.image('file.jpg')
        output=query('file.jpg')
        word=output[0]['generated_text']

        st.success("The Image Description is: {}".format(word.title()))
         



options=st.sidebar.selectbox("Select Option",('',"Upload Image","Paste Url"))

if options=="Upload Image":
    
    output = upload_image()
    

elif options=="Paste Url" :
    url = st.sidebar.text_input("Enter the URL")
    submit=st.sidebar.button("Submit")
    if submit:
        urllib.request.urlretrieve(url, "url.png")    
        st.image('url.png', width=500)
        output= query('url.png')
        word=output[0]['generated_text']

        st.success("The Image Description is: {}".format(word.title()))
    

   
    

else:
    st.warning("Please select an option")

