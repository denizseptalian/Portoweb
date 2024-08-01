import streamlit as st
from PIL import Image

logo = Image.open("logo.png")
st.set_page_config(page_title="Kim Marcial Vallesteros", page_icon=logo, layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")


st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True
)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000000;">
        <a class="navbar-brand" href="#">Kim Marcial A. Vallesteros</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="#about">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#skills"
                    >Skills Summary</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#projects">Projects</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#contact">Contact Me</a>
                </li>
            </ul>
        </div>
    </nav>
    """,
    unsafe_allow_html=True
)


# ---- HEADER SECTION ----
profile_pic = Image.open("profile_pic2.png")
about_pic = Image.open("about_pic.png")

buttons = {
    "Resume": "http://tinyurl.com/3hz4pfym",               ### To be updated whenever I have a new version
    "LinkedIn": "https://www.linkedin.com/in/kimmarcialvallesteros/",
    "GitHub": "https://github.com/Kimchi21",
    "Gmail": "mailto:kimmarcialv@gmail.com"
}

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        col1, col2, col3 = st.columns([1.75, 6, 3])
        max_width = 520
        max_height = 480
        original_width, original_height = profile_pic.size
        aspect_ratio = original_width / original_height
        new_width = max_width
        new_height = int(new_width / aspect_ratio)

        if new_height > max_height:
            new_height = max_height
            new_width = int(new_height * aspect_ratio)

        resized_pic1 = profile_pic.resize((new_width, new_height))

        with col2:
            st.image(resized_pic1, width=475)

            st.markdown(
                f'<style>.specific-image-class {{height: 550px !important;}}</style>',
                unsafe_allow_html=True
            )

    with right_column:
        st.markdown("<h4 style='text-align: center;'>Hello, I'm</h4>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>Kim Marcial A. Vallesteros</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Data Analyst</h4>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>&quot;Asking the right questions paves the way for discovery. And asking the wrong ones? Well, it still leads to discovery, albeit on a different path.&quot;</h5>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <style>
                .download-button {{
                    background-color: #0067c3;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    align-self: center;
                }}
                .download-button:hover {{
                    background-color: #0b35b6;
                }}
            </style>
            <div id="download-container" style="display: flex; justify-content: center; margin-bottom: 20px;">
                <a href="{buttons['Resume']}" download>
                    <button class="download-button">
                        <strong>Download Resume</strong>
                    </button>
                </a>
            </div>
            <script>
                var button = document.querySelector('.download-button');
                button.addEventListener('mouseover', function() {{
                    button.style.backgroundColor = '#0b35b6';
                }});
                button.addEventListener('mouseout', function() {{
                    button.style.backgroundColor = '#0067c3';
                }});
            </script>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
        f"<div style='display: flex; justify-content: center;'>"
        f"<a href='{buttons['LinkedIn']}' target='_blank'><img src='https://cdn-icons-png.flaticon.com/128/3536/3536505.png' alt='LinkedIn' style='width: 35px; height: 35px; margin: 0 10px;'></a>"
        f"<a href='{buttons['GitHub']}' target='_blank'><img src='https://cdn-icons-png.flaticon.com/128/5968/5968866.png' alt='GitHub' style='width: 35px; height: 35px; margin: 0 10px;'></a>"
        f"<a href='{buttons['Gmail']}' target='_blank'><img src='https://cdn-icons-png.flaticon.com/128/732/732200.png' alt='Gmail' style='width: 35px; height: 35px; margin: 0 10px;'></a>"
        "</div>",
        unsafe_allow_html=True
        )

st.write("##")


# ---- ABOUT ME ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(
            """
            <div id="about">
            <h1>About Me</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"<div style='display: flex; justify-content: center;'>"
                "<div style='text-align: center; border: 1px solid #ccc; padding: 20px; border-radius: 20px; width: 225px; margin: 10px;'>"
                f"<img src='https://raw.githubusercontent.com/denizseptalian/Portoweb/blob/main/experience.png' alt='exp' style='width: 50px; height: 50px;'>"
                "<br>"
                "<p style='margin: 3px 0;'><strong>Experience</strong></p>"
                "<p style='margin: 3px 0;'>1+ years</p>"
                "<p style='margin: 3px 0;'>Data Analytics</p>"
                "</div>"
                "</div>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<div style='display: flex; justify-content: center;'>"
                "<div style='text-align: center; border: 1px solid #ccc; padding: 20px; border-radius: 20px; width: 225px; margin: 10px;'>"
                f"<img src='https://raw.githubusercontent.com/denizseptalian/Portoweb/blob/main/education.png' alt='edu' style='width: 50px; height: 50px;'>"
                "<br>"
                "<p style='margin: 3px 0;'><strong>Education</strong></p>"
                "<p style='margin: 3px 0;'>Bachelors Degree</p>"
                "<p style='margin: 3px 0;'>Computer Engineering</p>"
                "</div>"
                "</div>",
                unsafe_allow_html=True
            )

        st.write("##")
        st.write(
            """
           Driven by a passion for computer and data-related fields, I possess a solid foundational knowledge base 
           and a strong desire for performance and attention to detail. The technical tools I mainly use are Python, SQL, 
           Microsoft Excel and Power BI, I specialize in data analysis, data visualization, and 
           data manipulation, aiming to extract meaningful insights from data. I am dedicated to continuous learning 
           and innovation. My passion for learning serves as the cornerstone of my journey in data analytics.
            """
        )

    with right_column:
        col1, col2, col3 = st.columns([1, 1.6, 1])
        max_width = 600
        max_height = 900
        original_width, original_height = about_pic.size
        aspect_ratio = original_width / original_height
        new_width = max_width
        new_height = int(new_width / aspect_ratio)

        if new_height > max_height:
            new_height = max_height
            new_width = int(new_height * aspect_ratio)

        resized_pic = about_pic.resize((new_width, new_height))

        with col2:
            st.image(resized_pic, width=375)

            st.markdown(
                f'<style>.specific-image-class {{height: 550px !important;}}</style>',
                unsafe_allow_html=True
            )


# ---- Skills Summary ----
with st.container():
    st.write("---")
    st.markdown(
        """
        <div id="skills">
        <h1>Skills Summary</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
            "<p style='margin: 10px 0; font-size: 20px;'><strong>Languages</strong></p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg' alt='python' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>Python</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn-icons-png.flaticon.com/128/4248/4248443.png' alt='sql' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>SQL</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg' alt='c' style='width: 50px; height: 50px;'>"
            "</div>"            
            "<p style='margin: 10px 0;'>C</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg' alt='html' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>HTML</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg' alt='css' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>CSS</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg' alt='js' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>JavaScript</p>"
            "</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
            "<p style='margin: 10px 0; font-size: 20px;'><strong>Libraries & Frameworks</strong></p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg' alt='pandas' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>Pandas</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg' alt='numpy' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>NumPy</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://icon.icepanel.io/Technology/svg/Matplotlib.svg' alt='matplot' style='width: 50px; height: 50px;'>"
            "</div>"            
            "<p style='margin: 10px 0;'>matplotlib</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://user-images.githubusercontent.com/315810/92161415-9e357100-edfe-11ea-917d-f9e33fd60741.png' alt='seaborn' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>seaborn</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://icon.icepanel.io/Technology/svg/scikit-learn.svg' alt='skl' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>scikit-learn</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://www.statsmodels.org/stable/_images/statsmodels-logo-v2-no-text.svg' alt='stats' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>statsmodels</p>"
            "</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
            "<p style='margin: 10px 0; font-size: 20px;'><strong>Development Tools & Applications</strong></p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg' alt='mysql' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>MySQL</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg' alt='postgresql' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>PostgreSQL</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg/1101px-Microsoft_Office_Excel_%282019%E2%80%93present%29.svg.png' alt='excel' style='width: 50px; height: 50px;'>"
            "</div>"            
            "<p style='margin: 10px 0;'>Microsoft Excel</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://static-00.iconduck.com/assets.00/power-bi-icon-1536x2048-0xah5g2o.png' alt='powerbi' style='width: 40px; height: 45px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>Microsoft Power BI</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg' alt='vscode' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>Visual Studio Code</p>"
            "<br>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg' alt='git' style='width: 50px; height: 50px;'>"
            "</div>"             
            "<p style='margin: 10px 0;'>Git</p>"
            "</div>",
            unsafe_allow_html=True
        )


# ---- PROJECTS ----
repo = {
    "RAWG": "https://github.com/Kimchi21/RAWG.io_Game-Data-Analysis",
    "AutoSales": "https://github.com/Kimchi21/Data-Analysis_Portfolio/tree/main/Automobile%20Sales",
    "SSD": "https://github.com/Kimchi21/Solid-State-Drives_Analysis",
    "Laz_Shopee": "https://github.com/Kimchi21/Lazada-vs.-Shopee_Sentiment-Analysis",
    "Sperm": "https://github.com/Kimchi21/Sperm-Morphological-Quality-ImageSegmentation",
    "Raisin": "https://github.com/Kimchi21/Raisin-Grain-Prediction-Using-a-StackedEnsembleModel"
}

with st.container():
    st.write("---")
    st.markdown(
        """
        <div id="projects">
        <h1>My Projects</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    right, left = st.columns(2)
    with right:
        st.markdown(
            f"""
            <style>
                .repo-button {{
                    background-color: #0067c3;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                .repo-button:hover {{
                    background-color: #0b35b6;
                }}
                .project-container {{
                    display: flex;
                    justify-content: center;
                }}
                .project-box {{
                    text-align: center;
                    border: 1px solid #ccc;
                    padding: 40px;
                    border-radius: 20px;
                    width: 550px;
                    margin: 10px;
                }}
                .project-img {{
                    width: 475px;
                    height: 275px;
                }}
            </style>
            <div class="project-container">
            <div class="project-box">
                <img src="RAWG.png" alt="RAWG" class="project-img">
                <p style='margin: 15px 0 0 0;'>This analysis delves into the vast realm of gaming data, specifically focusing on insights derived from RAWG.io, a comprehensive video game database.</p>
                <br>
                <a href="{repo['RAWG']}" project>
                    <button class="repo-button">
                        <strong>Link to Repository</strong>
                    </button>
                </a>
            </div>
            <!-- Add similar structure for other projects -->
            </div>
            <script>
                var buttons = document.querySelectorAll('.repo-button');
                buttons.forEach(function(button) {{
                    button.addEventListener('mouseover', function() {{
                        button.style.backgroundColor = '#0b35b6';
                    }});
                    button.addEventListener('mouseout', function() {{
                        button.style.backgroundColor = '#0067c3';
                    }});
                }});
            </script>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <style>
                .repo-button {{
                    background-color: #0067c3;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                .repo-button:hover {{
                    background-color: #0b35b6;
                }}
                .project-container {{
                    display: flex;
                    justify-content: center;
                }}
                .project-box {{
                    text-align: center;
                    border: 1px solid #ccc;
                    padding: 40px;
                    border-radius: 20px;
                    width: 550px;
                    margin: 10px;
                }}
                .project-img {{
                    width: 475px;
                    height: 275px;
                }}
            </style>
            <div class="project-container">
            <div class="project-box">
                <img src="ssd.png" alt="SSD" class="project-img">
                <p style='margin: 15px 0 0 0;'>This analysis dives into Amazon's diverse array of Solid State Drives (SSDs), aiming to offer insights that benefit prospective buyers in their decision-making process.</p>
                <br>
                <a href="{repo['SSD']}" project>
                    <button class="repo-button">
                        <strong>Link to Repository</strong>
                    </button>
                </a>
            </div>
            <!-- Add similar structure for other projects -->
            </div>
            <script>
                var buttons = document.querySelectorAll('.repo-button');
                buttons.forEach(function(button) {{
                    button.addEventListener('mouseover', function() {{
                        button.style.backgroundColor = '#0b35b6';
                    }});
                    button.addEventListener('mouseout', function() {{
                        button.style.backgroundColor = '#0067c3';
                    }});
                }});
            </script>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <style>
                .repo-button {{
                    background-color: #0067c3;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                .repo-button:hover {{
                    background-color: #0b35b6;
                }}
                .project-container {{
                    display: flex;
                    justify-content: center;
                }}
                .project-box {{
                    text-align: center;
                    border: 1px solid #ccc;
                    padding: 40px;
                    border-radius: 20px;
                    width: 550px;
                    margin: 10px;
                }}
                .project-img {{
                    width: 475px;
                    height: 275px;
                }}
            </style>
            <div class="project-container">
            <div class="project-box">
                <img src="sperm.png" alt="Sperm" class="project-img">
                <p style='margin: 15px 0 0 0;'>To address male infertility, a model is trained to classify and detect sperm head morphological quality, potentially streamlining and standardizing the assessment process.</p>
                <br>
                <a href="{repo['Sperm']}" project>
                    <button class="repo-button">
                        <strong>Link to Repository</strong>
                    </button>
                </a>
            </div>
            <!-- Add similar structure for other projects -->
            </div>
            <script>
                var buttons = document.querySelectorAll('.repo-button');
                buttons.forEach(function(button) {{
                    button.addEventListener('mouseover', function() {{
                        button.style.backgroundColor = '#0b35b6';
                    }});
                    button.addEventListener('mouseout', function() {{
                        button.style.backgroundColor = '#0067c3';
                    }});
                }});
            </script>
            """,
            unsafe_allow_html=True
        )

    with left:
        st.markdown(
            f"""
            <style>
                .repo-button {{
                    background-color: #0067c3;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                .repo-button:hover {{
                    background-color: #0b35b6;
                }}
                .project-container {{
                    display: flex;
                    justify-content: center;
                }}
                .project-box {{
                    text-align: center;
                    border: 1px solid #ccc;
                    padding: 40px;
                    border-radius: 20px;
                    width: 550px;
                    margin: 10px;
                }}
                .project-img {{
                    width: 475px;
                    height: 275px;
                }}
            </style>
            <div class="project-container">
            <div class="project-box">
                <img src="LS.png" alt="Lazada vs. Shopee" class="project-img">
                <p style='margin: 15px 0 0 0;'>A sentiment analysis approach for analyzing two of the most popular e-commerce platforms in the Philippines by how how users perceive, experience and engage with these platforms.</p>
                <br>
                <a href="{repo['Laz_Shopee']}" project>
                    <button class="repo-button">
                        <strong>Link to Repository</strong>
                    </button>
                </a>
            </div>
            <!-- Add similar structure for other projects -->
            </div>
            <script>
                var buttons = document.querySelectorAll('.repo-button');
                buttons.forEach(function(button) {{
                    button.addEventListener('mouseover', function() {{
                        button.style.backgroundColor = '#0b35b6';
                    }});
                    button.addEventListener('mouseout', function() {{
                        button.style.backgroundColor = '#0067c3';
                    }});
                }});
            </script>
            """,
            unsafe_allow_html=True
        )

    with left:
        st.markdown(
            f"""
            <style>
                .repo-button {{
                    background-color: #0067c3;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                .repo-button:hover {{
                    background-color: #0b35b6;
                }}
                .project-container {{
                    display: flex;
                    justify-content: center;
                }}
                .project-box {{
                    text-align: center;
                    border: 1px solid #ccc;
                    padding: 40px;
                    border-radius: 20px;
                    width: 550px;
                    margin: 10px;
                }}
                .project-img {{
                    width: 475px;
                    height: 275px;
                }}
            </style>
            <div class="project-container">
            <div class="project-box">
                <img src="AS.png" alt="Automobile Sales" class="project-img">
                <p style='margin: 15px 0 0 0;'>This analysis delves into a range of automobile sales transactions and forecasting of automobile sales for the rest of the year based on data available from Kaggle.</p>
                <br>
                <a href="{repo['AutoSales']}" project>
                    <button class="repo-button">
                        <strong>Link to Repository</strong>
                    </button>
                </a>
            </div>
            <!-- Add similar structure for other projects -->
            </div>
            <script>
                var buttons = document.querySelectorAll('.repo-button');
                buttons.forEach(function(button) {{
                    button.addEventListener('mouseover', function() {{
                        button.style.backgroundColor = '#0b35b6';
                    }});
                    button.addEventListener('mouseout', function() {{
                        button.style.backgroundColor = '#0067c3';
                    }});
                }});
            </script>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <style>
                .repo-button {{
                    background-color: #0067c3;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }}
                .repo-button:hover {{
                    background-color: #0b35b6;
                }}
                .project-container {{
                    display: flex;
                    justify-content: center;
                }}
                .project-box {{
                    text-align: center;
                    border: 1px solid #ccc;
                    padding: 40px;
                    border-radius: 20px;
                    width: 550px;
                    margin: 10px;
                }}
                .project-img {{
                    width: 475px;
                    height: 275px;
                }}
            </style>
            <div class="project-container">
            <div class="project-box">
                <img src="raisin.png" alt="Raisin" class="project-img">
                <p style='margin: 15px 0 0 0;'>A stacked ensemble model for classifying and predicting raisin grains based on physical characteristics that could potentially aid the traditional sorting of raisins by hand.</p>
                <br>
                <a href="{repo['Raisin']}" project>
                    <button class="repo-button">
                        <strong>Link to Repository</strong>
                    </button>
                </a>
            </div>
            <!-- Add similar structure for other projects -->
            </div>
            <script>
                var buttons = document.querySelectorAll('.repo-button');
                buttons.forEach(function(button) {{
                    button.addEventListener('mouseover', function() {{
                        button.style.backgroundColor = '#0b35b6';
                    }});
                    button.addEventListener('mouseout', function() {{
                        button.style.backgroundColor = '#0067c3';
                    }});
                }});
            </script>
            """,
            unsafe_allow_html=True
        )


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.markdown(
        """
        <div id="contact">
        <h1>Contact Me</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='display: flex; justify-content: center;'>"
        "<div style='text-align: center; border: 1px solid #ccc; border-radius: 20px; width: 615px; margin: 5px; padding: 20px;'>"
        f"<div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; align-items: center; justify-items: center; text-align: center;'>"
        f"<div>"
        f"<a href='{buttons['Gmail']}' target='_blank'><img src='https://cdn-icons-png.flaticon.com/128/732/732200.png' alt='gmail' style='width: 35px; height: 35px;'></a>"
        f"<p style='margin: 5px 0;'><strong>kimmarcialv@gmail.com</strong></p>"
        "</div>"
        "<div>"
        f"<img src='https://cdn-icons-png.flaticon.com/128/8103/8103544.png' alt='Phone' style='width: 35px; height: 35px;'>"
        f"<p style='margin: 5px 0;'><strong>+63 927 602 1289</strong></p>"
        "</div>"
        "<div>"
        f"<a href='{buttons['LinkedIn']}' target='_blank'><img src='https://cdn-icons-png.flaticon.com/128/3536/3536505.png' alt='LinkedIn' style='width: 35px; height: 35px;'></a>"
        f"<p style='margin: 5px 0;'><strong>Kim Marcial Vallesteros</strong></p>"
        "</div>"
        "</div>"
        "</div>"
        "</div>",
        unsafe_allow_html=True
    )

    contact_form = """
    <style>
    /* CSS styles for the form */
    form.contact-form {
        max-width: 750px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
    }

    button[type=submit] {
        margin-top: 10px;
    }
    </style>

    <div>
        <form action="https://formsubmit.co/kimmarcialv@gmail.com" method="POST" class="contact-form">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <div style="margin: 0 auto;"> <!-- Use a div with margin to center the button -->
                <button type="submit">Send</button>
            </div>
        </form>
    </div>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

st.write("##")
st.write("##")
st.write("##")
st.markdown(
    "<div>"
    "<div style='display: flex; flex-direction: column; align-items: center;'>"
    "<img src='logo.png' alt='Phone' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>© 2024 Kim Marcial A. Vallesteros</p>"
    "</div>"
    "</div>",
    unsafe_allow_html=True
)
