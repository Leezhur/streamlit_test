import streamlit as st
from PIL import Image  # local에서 이미지 불러오기

#01. 사이드바 화면
st.sidebar.header("Login")
user_id = st.sidebar.text_input("ID 입력", value='', max_chars=15)
user_password = st.sidebar.text_input("P/W 입력", value='', type="password")

if user_id == "suyoung" and user_password == '1234':
    st.sidebar.header("그림 목록")

    # 선택할 데이터 목록 (여러 개의 데이터 불러올 때는 리스트나 딕셔너리로 불러오기)
    sel_options = ['', '진주 귀걸이를 한 소녀', '별이 빛나는 밤',
                '절규', '생명의 나무', '월하장인']

    # 콤보 상자 (내가 선택한 작품명)
    user_opt = st.sidebar.selectbox("▼ 좋아하는 작품 선택", sel_options, index=0)  # index : 기본 선택값

    # .write == print
    st.sidebar.write("※ Choice한 작품 : ", user_opt)

    #02. 메인 화면
    st.subheader("Main 화면")
    image_files = "Welcome.png", 'Verneer.png', 'Gogh.png', 'Munch.png', 'Klimt.jpg', 'ShinYoonbok.png'
    sel_index =  sel_options.index(user_opt)
    image_file = image_files[sel_index]
    img_local = Image.open(f'img/{image_file}')
    st.image(img_local, caption=user_opt)
    

