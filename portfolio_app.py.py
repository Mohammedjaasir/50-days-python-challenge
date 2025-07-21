import streamlit as st
from PIL import Image  # Pillow library for image handling

def main():
    st.set_page_config(
        page_title="Jaax Portfolio - About Me",
        page_icon="✨",
        layout="centered"
    )

    # --- HEADER SECTION ---
    st.title("✨ About Me")
    st.write("---")

    # --- PROFILE IMAGE ---
    try:
        profile_image = Image.open("profile_pic.png")  # Make sure this file is available
        st.image(profile_image, width=250)
    except FileNotFoundError:
        st.warning("Profile image not found! Please place 'profile_pic.png' in the same directory.")
        st.info("Or use a placeholder image: `st.image('https://via.placeholder.com/250')`")

    st.header("Hello, I'm Jaax!")
    st.write("### Engineering Student | AI Explorer | Project Builder")

    st.write("---")

    # --- ABOUT ME SECTION ---
    st.header("My Story & What I Do")
    st.write("""
    Hey there! I'm Jaax, an engineering student from SNS College of Engineering with a deep interest in Artificial Intelligence and Machine Learning.
    I love building smart, real-world projects—whether it's a Student Speaking Analyzer, a Collision Alert System, or even a Silent Meeting Assistant.

    I'm currently completing an AI & ML internship where I work on tasks like Exploratory Data Analysis, Regression, and Classification models.
    Hackathons have been a big part of my journey too. I was recently selected as both a team leader and developer for the **Data Sprint 2.0 Hackathon** held in Chennai.

    Outside the tech world, I enjoy writing short plays, participating in mime shows, and exploring how literature and tech intersect.
    I'm always learning and pushing myself to go further—be it through DSA practice, deep learning, or starting a startup in the automobile AI space.

    My goal? Build tech that actually helps people—and have fun doing it.
    """)

    st.write("---")

    # --- SKILLS/EXPERIENCE SECTION ---
    st.header("Key Skills")
    st.markdown("""
    * **Programming Languages:** Python, C, JavaScript
    * **Frameworks/Libraries:** Streamlit, Scikit-learn, OpenCV, Flask
    * **AI/ML:** Linear & Logistic Regression, Decision Trees, KNN, Deep Learning (Beginner)
    * **Tools:** Git, Docker, VS Code, Jupyter Notebook
    * **Others:** HTML, CSS, Arduino, V2V Communication, ADAS, Project Documentation
    """)

    st.write("---")

    # --- LINKS SECTION ---
    st.header("Connect With Me!")
    st.write("Feel free to reach out or explore my work:")

    st.markdown("""
    * **[LinkedIn](https://www.linkedin.com/in/your-linkedin-profile/)** (Update with your actual profile)
    * **[GitHub](https://github.com/your-github-profile/)** (Update with your GitHub)
    * **[Personal Blog]()** (Optional)
    * **[Email Me](mailto:jaasirjaasir76@gmail.com)** (Update with your email)
    """)

    st.write("---")
    st.markdown("Made with ❤️ using Streamlit")


if __name__ == "__main__":
    main()
