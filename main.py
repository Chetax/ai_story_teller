import streamlit as st 
from story_generator import generate_story_from_images
from PIL import Image
st.title("AI Story Generator from images")
st.markdown("Upload 1 to 10 images, choose an style and let AI write and narrate an story for you.")



# Left sidebar 
with st.sidebar:
    st.header("Controls")

    uploaded_files=st.file_uploader(
        "Upload your images....",
        type=["png","jpg","jpeg"],
        accept_multiple_files=True
    )
    #select an stroy style
    story_style=st.selectbox(
        "Choose a story style",
        ("Comedy","Thriller","Fairy Tale","Sci-FI","Mystery","Adventure","Morale")
    )
    
    generate_button=st.button("Generate Story and Narration",type="primary")


    #main Logic to put the data

if generate_button :
    if not uploaded_files:
        st.warning("Please upload atleast 1 file!")
    elif len(uploaded_files)>10:
        st.warning("Please upload an maximum of 10 images.")
    else:
        with st.spinner("The Ai is writing and narrating your storty...."):
            try:
                pil_images=[Image.open(uploaded_files) for uploaded_files in uploaded_files]
                st.subheader("Your visual inspirations:")
                image_column=st.columns(len(pil_images))

                for i,image in enumerate(pil_images):
                    with image_column[i]:
                        st.image(image,use_container_width=True)
                generate_story=generate_story_from_images(pil_images,story_style)
                if "Error" in generate_story or "failed" in generate_story or "API key" in generate_story :
                    st.error(generate_story)
                else:

                 st.subheader(f"Your {story_style} story : ")
                 st.success(generate_story)
            except Exception as e:
                st.error(f"An Application Error {e}")
    