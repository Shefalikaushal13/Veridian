import base64
import io
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
from streamlit_lottie import st_lottie  # type: ignore
import json

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_res(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [{
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()
        }]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_hr = load_lottiefile("animations/ATS_animation.json")

if "show_form" not in st.session_state:
    st.session_state.show_form = False

# Streamlit App

st.set_page_config(
    page_title="Veridian",
    page_icon="Veridian-favicon.png",
    layout="centered"
)

st.markdown(
    """
    <style>
    html,body, .main .block-container {
        max-width: 100%;
        padding: 1rem 2rem 2rem;
    }
    .hero-text h1 {
        font-size: 3rem;
        color: #08fdd8;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .hero-text h2 {
        font-size: 1.5rem;
        color: #08fdd8;
        text-align: center;
        margin-bottom: 0.2rem;
        white-space: nowrap;
    }
    .hero-text h4 {
        font-size: 1.5rem;
        color: #c0c6cc;
        text-align: center;
        margin-bottom: 1rem;
    }
    .hero-text h6 {
        font-size: 1.1rem;
        color: #9da5b4;
        text-align: center;
    }
    div.stButton button {
        font-size: 2.2rem;
        padding: 0.75rem 2rem;
        font-weight: 600;
        color: #ffffff;
        border-radius: 8px;
    }
    label {
        font-size: 2rem !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Lottie animation
st.markdown("<div style='display:flex; justify-content:center; position: relative; top: -300px;'>", unsafe_allow_html=True)
st_lottie(lottie_hr, height=280, key="ats")
st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    """
    <div class="hero-text" style='margin-bottom: 50px;'>
        <h1 style='margin-top: -30px;'>Veridian</h1>
        <h2 style='margin-top: -30px;'>Track, Improve, and Optimize Your Resume for ATS</h2>
        <h4>Stop Getting Ignored by Recruiters</h4>
        <h6>Most resumes fail before a human even sees them<br>
        Veridian helps you beat the bots and get noticed for the right reasons<br>
        No sugarcoating, just real, AI-powered feedback that actually works</h6>
    </div>
    """,
    unsafe_allow_html=True
)


col_center = st.columns(3)
with col_center[1]:
    cta_clicked = st.button("🚀 Let's Get Started", key="start_button", use_container_width=True)


st.markdown("<div style=' margin-top: 20px; margin-bottom: 50px;'></div>", unsafe_allow_html=True)

if cta_clicked:
    st.session_state.show_form = True

if st.session_state.show_form:
    st.markdown(
    "<h3 style='text-align: center; margin-bottom: 15px;'>Upload Your Resume & Paste the Job Description</h3>",
    unsafe_allow_html=True
)

    input_text = st.text_area("📄 Paste the Job Description", key="input")
    uploaded_file = st.file_uploader("📎 Upload your Resume (PDF only)", type=["pdf"])

    if uploaded_file:
        st.success("Resume uploaded successfully!")

    col1, col2, col3 = st.columns(3)
    with col1:
        submit1 = st.button("📋 Resume Overview", use_container_width=True)
    with col2:
        submit2 = st.button("🔑 Missing Keywords", use_container_width=True)
    with col3:
        submit3 = st.button("📈 Match Percentage", use_container_width=True)


input_prompt1 = """
    You are an experienced HR with tech experience in the field of any one job role out of: Data Science, Full Stack
    Developer, Frontend Developer, Backend Developer, ML engineer, Big Data engineer, Devops,
    Data Analyst, Business Analyst and UI/UX Designer. Your task is to review the provided
    resume against the given job description for these profiles. Please share your professional
    evaluation on whether the candidate's profile aligns with the role. Consider that the job market is very competitive so 
    answer with highest accuracy.
    Highlight the strengths and weaknessed of the applicant in relation to the specified job requirements.
    Don't mention what you are specialising in as an HR manager, give the response directly.
"""

input_prompt2 = """
    You are a technical Human resource Manager with expertise in the field of any one job role out of: Data Science, 
    Full Stack Developer, Frontend Developer, Backend Developer, ML engineer, Big Data engineer, Devops,
    Data Analyst, Business Analyst and UI/UX Designer. Your role is to analyze the given resume and
    the given job description. Identify keywords and skills from the job description absent in 
    the resume. Prioritize based on frequency and relevance to the job. Consider that the job market is very competitive so 
    answer with highest accuracy
    Provide suggestions for integrating these keywords into the resume, emphasizing achievements and quantifiable results.
    Don't mention what you are specialising in as an HR manager, give the response directly.
"""

input_prompt3 = """
    You are a skilled ATS (application treacking system) scanner with a deep understanding of any one job role out of: Data Science, 
    Full Stack Developer, Frontend Developer, Backend Developer, ML engineer, Big Data engineer, Devops, Data Analyst, Business Analyst
    and UI/UX Designer and deep ATS functionality.
    Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
    the job description. Consider that the job market is very competitive so answer with highest accuracy.
    First the output should come as percentage and then use cues to represent high, medium, and low match areas, 
    highlighting strengths and weaknesses and last final thoughts.
    Don't mention what you are specialising in as an HR manager, give the response directly.s
"""

if st.session_state.show_form:
    if 'submit1' in locals() and submit1:
        if uploaded_file and input_text:
            with st.spinner("Analyzing resume..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_gemini_res(input_prompt1, pdf_content, input_text)
            st.subheader("Resume Summary")
            st.write(response)
        else:
            st.warning("Please upload a valid Resume and Job Description")

    elif 'submit2' in locals() and submit2:
        if uploaded_file and input_text:
            with st.spinner("Finding missing keywords..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_gemini_res(input_prompt2, pdf_content, input_text)
            st.subheader("Missing Keywords:")
            st.write(response)
        else:
            st.warning("Please upload a valid Resume and Job Description")

    elif 'submit3' in locals() and submit3:
        if uploaded_file and input_text:
            with st.spinner("Calculating match percentage..."):
                pdf_content = input_pdf_setup(uploaded_file)
                response = get_gemini_res(input_prompt3, pdf_content, input_text)
            st.subheader("Percentage Match is:")
            st.write(response)
        else:
            st.warning("Please upload a valid Resume and Job Description")

st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
st.markdown("<hr style='margin-top: 3rem; margin-bottom: 1rem;'>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div style='text-align: center; font-size: 1.1rem; color: #9da5b4; margin-bottom: 3rem;'>
        Made with ❤️ by <b>Shefali Kaushal</b> | © 2025 <b>Veridian</b>
    </div>
    """,
    unsafe_allow_html=True
)
