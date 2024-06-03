import os
#import toml
import streamlit as st


# st.set_page_config adalah sebuah metode yang digunakan u mengubah oarameter dari page kita
st.set_page_config(
    page_title = "Portofolio Web App ",
    layout = "wide"
    )

# buat halaman cv dengan 2 kolom 
col_1, col_2 = st.columns([1, 3])


with col_1 :
    st.markdown(
        '''
        <style>
        div[data-testid="stHorizontalBlock"] > div:first-of-type {
            background-color: #555EB8;
            padding: 10px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
    # foto
    st.markdown(
        '''
        <style>
        .white-border {
            border: 7px solid white;
            border-radius: 5px;
            padding: 0px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )

    with st.container() as col:
 
        image_path = 'https://github.com/huwaidanur/streamlit-sentimen-app/raw/master/app/file/img/foto_formal.png'
        #st.image(image_path)
        st.markdown(f'<img src="{image_path}" width="300" class="white-border">', unsafe_allow_html=True)

    with st.container(height=50, border=False):
        pass                   


    # biodata
    with st.container():
        original_title = '<p style="font-family:Courier; color:White; font-size: 20px; font-weight:bold">Personal Information</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 15px;">Address : Bekasi, Indonesia </p>', unsafe_allow_html=True)

    with st.container(height=30, border=False):
        pass

    # kemampuan bahasa
    with st.container():
        original_title = '<p style="font-family:Courier; color:White; font-size: 20px; font-weight:bold">Language Proficiency</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 15px;">Indonesia : Native </p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 15px;">Inggris: Intermediate </p>', unsafe_allow_html=True)

    with st.container(height=30, border=False):
        pass

    # teknologi yang dikuasai
    with st.container():
        original_title = '<p style="font-family:Courier; color:White; font-size: 20px; font-weight:bold">Soft Skills</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        teks='''
        Effective Communication, 
        Problem-Solving, 
        Critical Thinking, 
        Collaboration, Teamwork
        '''
        st.markdown(f'<p style="font-family:Courier; color:White; font-size: 15px;">{teks}</p>', unsafe_allow_html=True)

    with st.container(height=50, border=False):
        pass

with col_2:
    # perkenalan

    with st.container():
        st.header("Huwaida Nur Asysyifa Mufarrida")
        teks='''
        A fresh graduate with a Bachelor of Science degree in Physics from Bandung Institute of Technology (ITB), 
        demonstrating a strong passion and dedication. Proficient in data analysis, statistical modeling, and computational physics. 
        Capable in Python programming, Data Wrangling, Machine Learning, and Natural Language Processing. 
        Aspiring to utilize analytical prowess and academic foundation as a data scientist or data analyst, adding value to data-driven decision-making in a dynamic setting.
        '''
        st.write(teks)
    
    with st.container(height=10, border=False):
        pass
    
    st.divider()

    # pendidikan
    with st.container():
        st.header('Pendidikan')
        with st.container():
            col_0,col_1, col_2 = st.columns([1,10,40])
            col_1.markdown('2019-2023')
            col_2.text(
                    ''' 
                    BANDUNG INSTITUTE OF TECHNOLOGY (ITB)
                    FACULTY OF MATHEMATICS AND NATURAL SCIENCES
                    Bachelor's Degree in Physics
                    '''
                        )
    with st.container(height=10, border=False):
        pass        
    st.divider()


    # pendidikan tambahan
    with st.container():
        st.header('Certifications and Training')
        with st.container():
            col_0, col_1, col_2 = st.columns([1,10,40])
            col_1.markdown('Oct 2023 - Feb 2024')
            col_2.markdown(
                    ''' 
                    Full Stack Data Science SanberCampus x ITB
                    '''
                        )    
            col_1.markdown('May 2024')
            col_2.markdown(
                    ''' 
                    IBM Exploratory Data Analysis for Machine Learning
                    '''
                        )
            col_1.markdown('May 2024')
            col_2.markdown(
                    ''' 
                    IBM Supervised Machine Learning : Regression 
                    '''
                        )
            col_1.markdown('May 2024')
            col_2.markdown(
                    ''' 
                    IBM Supervised Machine Learning : Classification 
                    '''
                        )
    with st.container(height=10, border=False):
        pass       
    st.divider()


    # pengalaman Akademis
    with st.container():
        st.header('Work Experience')
        with st.container():
            col_0, col_1, col_2 = st.columns([1,10,40])
            col_1.markdown('Aug 2022 - Dec 2022')
            col_2.markdown(
                    ''' 
                    Elementary Physics Grader Assistant | Bandung Institute of Technology (ITB)
                    '''
                        )
            col_1.markdown('Nov 2022')
            col_2.markdown(
                    ''' 
                    Research Intern | Korea Advanced Institute of Science and Technology (KAIST)
                    '''
                        )
            col_1.markdown('Aug 2022 - Dec 2021')
            col_2.markdown(
                    ''' 
                    Physics Laboratory Assistant | Bandung Institute of Technology (ITB)
                    '''
                        )
        
    with st.container(height=10, border=False):
        pass       
    st.divider()


    # pengalaman organisasi
    with st.container():
        st.header('Activities')
        with st.container():
            col_0, col_1, col_2 = st.columns([1, 10, 40])

            # Memberikan teks pada kolom-kolom tersebut
            col_1.markdown('Nov 2020 - Nov 2021')
            col_2.markdown('''
                        Secretary | Kuningan Student Community (KAMIKU ITB)

                        ''')

            col_1.markdown('Apr 2020 - Jul 2021')
            col_2.markdown('''
                        Head of Event Organizer Division | Festival Adha P3RI 1442H (Salman ITB)
                        ''')



