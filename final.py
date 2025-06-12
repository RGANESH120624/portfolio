import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(page_title="Redagani Ganesh Portfolio", page_icon="📄", layout="wide")

# --- Sidebar ---
st.sidebar.image("my-avatar.png", width=120)
st.sidebar.title("Redagani Ganesh")
st.sidebar.markdown("**Python Developer | Data Analyst**")

st.sidebar.header("📞 Contact")
st.sidebar.markdown("[📧 Email](mailto:redaganiganesh67@gmail.com)")
st.sidebar.write("+91 8341060798")
st.sidebar.write("📍 Hyderabad, India")

st.sidebar.header("🔗 Social Links")
st.sidebar.markdown("[GitHub](https://github.com/RGANESH120624)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/redagani-ganesh-b41045245/)")

# --- Navigation ---
pages = ["About", "Resume", "Contact"]
selected_page = st.radio("Navigation", pages, horizontal=True)

# --- Resume Download Button ---
def download_pdf_button(pdf_path, label="⬇️ Download Resume"):
    try:
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        href = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="Redagani_Ganesh_Resume.pdf">{label}</a>'
        st.markdown(href, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Resume PDF not found. Please upload `ganesh.pdf` in the root directory.")

# --- Resume Section Renderer ---
def show_resume_section(section):
    if section == "🎓 Education":
        st.subheader(section)
        st.markdown("- **M.Sc. Statistics**, Acharya Nagarjuna University, Guntur")

    elif section == "💼 Experience":
        st.subheader(section)
        st.markdown("""
        - **Python Developer**, Lyros Technologies – *April 2025 – Present*  
        - **Python Developer**, Accuracy Info Labs – *Nov 2020 – Dec 2020*  
        - **R Programmer**, Accuracy Info Labs – *Apr 2020 – Oct 2020*
        """)

    elif section == "🛠️ Professional Experience":
        st.subheader(section)
        points = [
            "3+ years as Python Developer",
            "2+ years in web scraping",
            "2+ years using Flask",
            "4+ months in Object Detection",
            "7+ months in R",
            "Worked with: PostgreSQL, MsSQL, MySQL",
            "Libraries: BeautifulSoup, TensorFlow, detectron2",
        ]
        for pt in points:
            st.markdown(f"- {pt}")

    elif section == "🧠 Skills & Expertise":
        st.subheader(section)
        st.markdown("""
        | Area            | Skills                                     |
        |-----------------|--------------------------------------------|
        | Developer       | Python, Flask                              |
        | Operating System| Windows                                    |
        | IDEs            | PyCharm, Jupyter, Google Colab, VS Code    |
        """)

    elif section == "📂 Projects":
        st.subheader(section)
        projects = [
            {
                "client": "Wingspan Global Solutions",
                "name": "Voice Recognition",
                "description": "Automates medical prescriptions using voice input and AI.",
                "responsibilities": [
                    "Designed RESTful API endpoints with Flask.",
                    "Integrated AssemblyAI and ChatGPT APIs.",
                    "Collaborated with cross-functional teams.",
                    "Implemented secure communication and error handling."
                ]
            },
            {
                "client": "Cyient",
                "name": "City Fiber",
                "description": "Built intelligent tools to automate fiber planning for UK cities.",
                "responsibilities": [
                    "Developed Flask backend services.",
                    "Applied ML/DL for telecom object detection.",
                    "Implemented file handling APIs."
                ]
            },
            {
                "client": "Accuracy Info Labs",
                "name": "Joblisting",
                "description": "Job portal similar to Naukri/Monster.",
                "responsibilities": [
                    "Led Python development team.",
                    "Performed data scraping and DB integration.",
                    "Used Pandas, NumPy, BeautifulSoup."
                ]
            }
        ]

        for proj in projects:
            with st.expander(f"{proj['name']} ({proj['client']})"):
                st.markdown(f"**Description:** {proj['description']}")
                st.markdown("**Responsibilities:**")
                for r in proj['responsibilities']:
                    st.markdown(f"- {r}")

# --- About Page ---
if selected_page == "About":
    st.header("🙋‍♂️ About Me")
    st.write("""
    I'm Redagani Ganesh, a Python Developer and Data Analyst with 3+ years of experience in web scraping, 
    Flask API development, OpenStack automation, and object detection using ML/DL frameworks.
    """)

    st.subheader("🔧 Key Skills")
    st.markdown("- Python, Flask, SQL, TensorFlow, detectron2")
    st.markdown("- Web scraping with BeautifulSoup and Requests")
    st.markdown("- Database: PostgreSQL, MSSQL, MySQL")
    st.markdown("- Containerization & Orchestration: Docker, Kubernetes")

# --- Resume Page ---
elif selected_page == "Resume":
    st.header("📄 My Resume")

    download_pdf_button("ganesh.pdf")

    sections = [
        "🎓 Education", "💼 Experience",
        "🛠️ Professional Experience", "🧠 Skills & Expertise", "📂 Projects"
    ]
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: btn1 = st.button(sections[0])
    with col2: btn2 = st.button(sections[1])
    with col3: btn3 = st.button(sections[2])
    with col4: btn4 = st.button(sections[3])
    with col5: btn5 = st.button(sections[4])

    if btn1:
        show_resume_section(sections[0])
    elif btn2:
        show_resume_section(sections[1])
    elif btn3:
        show_resume_section(sections[2])
    elif btn4:
        show_resume_section(sections[3])
    elif btn5:
        show_resume_section(sections[4])
    else:
        st.markdown("> Click a section above to view details.")

# --- Contact Page ---
elif selected_page == "Contact":
    st.header("📬 Contact Me")

    st.markdown("""
    <style>
    form input, form textarea {
        padding: 8px;
        border-radius: 6px;
        border: 1px solid #ccc;
        font-size: 16px;
    }
    form button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 25px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
    }
    form button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <form action="https://formsubmit.co/redaganiganesh67@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%;"><br><br>
        <input type="email" name="email" placeholder="Your email" required style="width: 100%;"><br><br>
        <textarea name="message" placeholder="Your message" style="width: 100%; height: 150px;" required></textarea><br><br>
        <button type="submit">Send</button>
    </form>
    """, unsafe_allow_html=True)
