import streamlit as st

text = "eror: \n"\
       "1. Scraping twitter -> solusi: scraperAPI, namun punya limit -> download data dan gunakan -> can't input request topic :( \n"\
       "2. Cleaning text -> menyambungkan tiap pekerjaan pembersihan -> memperbaiki fungsi cleaning service, banyak sekali trial and error \n"\
       "3. Membuat class fungsi u plotting -> gagal total \n"\
       "4. Membuat class fungsi u predict sentiment -> berhasil \n"\
       "5. Calling fungsi dan class fungsi dari file lain -> banyak error karena ketidakpahaman  \n"\
       "6. Make ML model dan training data Tweet lain(1600 baris)  -> Random Forest dgn berbagai parameter\n"\
       "7. Using plotly -> perbaiki update_layout -> banyak trial and rror \n"\
       "8. Make a git -> masalah karena file besar -> using Git LFS \n"\
       "9. Update requirements.txt \n"\
       "10. Can't show csv file after tracked by LFS -> remove and reupload file without Git LFS \n"\
       "11. Memperbaiki container dan columns \n"\
       "12. Fix pages 2 Biodata \n"\

st.write(text)