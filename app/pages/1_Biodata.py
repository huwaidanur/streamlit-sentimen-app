import os
import toml
import streamlit as st


# st.set_page_config adalah sebuah metode yang digunakan u mengubah oarameter dari page kita
st.set_page_config(
    page_title = "Portofolio Web App ",
    layout = "wide"
    )

# buat halaman cv dengan 2 kolom 

st.markdown(
    '''
    <style>
    div[data-testid="stHorizontalBlock"] > div:first-of-type {
        background-color: #c49f0c;
        padding: 10px;
        font_size: 6px;
    }
    </style>
    ''',
    unsafe_allow_html=True
)


col_1, col_2 = st.columns([1, 3])


with col_1 :
    # foto
    with st.container():
        secrets_path = os.path.abspath(os.path.join("..", ".streamlit", "secrets.toml"))

        # Membaca konfigurasi dari file secrets.toml
        with open(secrets_path, "r") as f:
            config = toml.load(f)

        # Menentukan path image dari konfigurasi
        path_configuration = config.get("path_configuration", {})
        path_image = path_configuration.get("path_image", "")

        # Mendapatkan path lengkap ke file gambar
        img_path = os.path.abspath(os.path.join("..", "file", "img", "foto_formal.png"))

        # Memeriksa apakah file gambar ada
        if os.path.exists(img_path):
            # Menampilkan gambar jika file ada
            st.image(img_path)
        else:
            st.error(f"File gambar '{img_path}' tidak ditemukan.")
                      
    with st.container(height=20, border=False):
        pass

    # biodata
    with st.container():
        original_title = '<p style="font-family:Courier; color:White; font-size: 20px; font-weight:bold">Biodata</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 16px;">Tanggal Lahir : 6 Frbruari 2002 </p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 16px;">Kota Asal: Bekasi </p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 16px;">Alamat: Teluk Pucung </p>', unsafe_allow_html=True)

    with st.container(height=30, border=False):
        pass

    # kemampuan bahasa
    with st.container():
        original_title = '<p style="font-family:Courier; color:White; font-size: 20px; font-weight:bold">Kemampuan Bahasa</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 16px;">Indonesia : Ahli </p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Courier; color:White; font-size: 16px;">Inggris: Ahli </p>', unsafe_allow_html=True)

    with st.container(height=30, border=False):
        pass

    # teknologi yang dikuasai
    with st.container():
        original_title = '<p style="font-family:Courier; color:White; font-size: 20px; font-weight:bold">Skill</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        teks='''
        public speaking, analytical thinking, communication, 
        '''
        st.markdown(f'<p style="font-family:Courier; color:White; font-size: 14px;">{teks}</p>', unsafe_allow_html=True)

    with st.container(height=50, border=False):
        pass

with col_2:
    # perkenalan

    with st.container():
        st.header("Huwaida Nur Asysyifa Mufarrida")
        teks='''
        Seorang lulusan fisika yang antusias dan bersemangat untuk menerapkan keterampilan analitis dan pemecahan masalah dalam lingkungan bisnis. 
        Dengan latar belakang pendidikan yang kuat dalam fisika, saya memiliki pemahaman mendalam tentang analisis data dan statistik. 
        Selain itu, penguasaan saya dalam pemrograman khususnya python dan keahlian dalam menggunakan berbagai alat analisis data membuat saya siap 
        untuk menjadi seorang data scientist ataupun data analyst yang produktif.
        '''
        st.write(teks)
    
    with st.container(height=30, border=False):
        pass
    
    st.divider()

    # pendidikan
    with st.container():
        st.header('Pendidikan')
        with st.container():
            col_0, col_1, col_2 = st.columns([1,10,40])
            col_1.text('2019-2023')
            col_2.text(
                    ''' 
                    INSTITUT TEKNOLOGI BANDUNG
                    FAKULTAS MATEMATIKA DAN PENGETAHUAN ALAM
                    S1 FISIKA
                    '''
                        )
    with st.container(height=30, border=False):
        pass        
    st.divider()


    # pendidikan tambahan
    with st.container():
        st.header('Pendidikan Kursus Tambahan /Sertifikat')
        with st.container():
            col_0, col_1, col_2 = st.columns([2,10,40])
            col_1.text('2023-sekarang')
            col_2.text(
                    ''' 
                    Full Stack Data Science SanberCampus x ITB
                    '''
                        )
            col_1.text('sekarang-')
            col_2.text(
                    ''' 
                    IBM Data Analyst
                    '''
                        )
    with st.container(height=30, border=False):
        pass       
    st.divider()


    # pengalaman Akademis
    with st.container():
        st.header('Pengalaman Akademis')
        with st.container():
            col_0, col_1, col_2 = st.columns([3,10,40])
            col_1.text('2021')
            col_2.text(
                    ''' 
                    Asisten Laboratorium Fisika Dasar
                    '''
                        )
            col_1.text('2022')
            col_2.text(
                    ''' 
                    Asisten Grader Fisika Dasar
                    '''
                        )
            col_1.text('2022')
            col_2.text(
                    ''' 
                    Student Exchange (Internship Program) ke Korean Advanced of Science and Technology (KAIST)
                    '''
                        )
        
    with st.container(height=30, border=False):
        pass       
    st.divider()


    # pengalaman organisasi
    with st.container():
        st.header('Pengalaman Organisasi')
        with st.container():
            col_0, col_1, col_2 = st.columns([3, 10, 40])

            # Memberikan teks pada kolom-kolom tersebut
            col_1.text('2020')
            col_2.text('''
                        Wakil Ketua Pelaksana Penerimaan Mahasiswa Baru (PMB) GAMAIS ITB (online)
                        ''')

            col_1.text('2020')
            col_2.text('''
                        Wakil Ketua Divisi Event Organizer P3RI 1442H
                        ''')

            col_1.text('2020-2021')
            col_2.text('''
                        Sekretaris KAMIKU
                        ''')

''' 
st.secrets.load_config("D:\Data Science - Sanbercode\belajar\Twitter_Sentimen_\app\pages.streamlit\secrets.toml")
img_path = st.secrets.path_configuration['path_image']
berkas_foto = 'foto_formal.png'
st.image(image=f'{img_path}{berkas_foto}') 

current_directory = os.getcwd()
secrets_path = os.path.join(current_directory, "app", "pages.streamlit", "secrets.toml")
#st.secrets["path_configuration"] = st.secrets(secrets_path)
st.secrets.load_config_file(secrets_path)
path_configuration = st.secrets["path_configuration"]
path_image = path_configuration["path_image"]
#img_path = st.secrets.path_configuration['path_image']
#berkas_foto = 'foto_formal.png'
berkas_foto = 'foto_formal.png'
st.image(image=f'{path_image}{berkas_foto}') 
'''