import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyDYTuy_XvMlSFkExQ2_rnvy1Y48VoAcxQk")

st.title("Isometric Pixel Art Maker")
prompt_user = st.text_input("Mau buat apa?", "Kastil kecil di awan")

system_instructions = "Isometric 3D pixel art style, clean edges, retro game look, solid background."

if st.button("Generate"):
    with st.spinner("Sedang menggambar..."):
        # Memanggil Nano Banana/Gemini untuk buat gambar
        response = client.models.generate_content(
            model="nano-banana",
            config={'system_instruction': system_instructions},
            contents=prompt_user
        )
        # Menampilkan gambar hasil AI
        st.image(response.generated_image)
