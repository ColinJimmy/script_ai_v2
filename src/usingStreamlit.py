import streamlit as st
from PIL import Image
import os
import subprocess

def save_image(image, save_path):
    image.save(save_path)
    st.success(f"Image saved successfully at {save_path}")
    return save_path

def run_command(image_path):
    command = f"python main.py --img_file {image_path} --decoder wordbeamsearch"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    st.text_area("Command Output:", result.stdout)
    # if result.stderr:
    #     st.error(f"Error: {result.stderr}")

def main():
    st.title("Script AI")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        save_directory = "data"
        os.makedirs(save_directory, exist_ok=True)
        save_path = os.path.join(save_directory, "img_0.png")
        
        if st.button("Save & Process Image"):
            image_path = save_image(image, save_path)
            run_command(image_path)

if __name__ == "__main__":
    main()
