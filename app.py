# -*- coding:utf-8 -*-
import streamlit as st
from eda_app import run_eda_app

def main():
    st.markdown("Hello World")
    menu = ["Home", "탐색적 자료 분석", "머신러닝", "About"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Home":
        st.subheader("Home")
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNQ_JVKy0LoTnxcyPLjr_S47o7in3NZbYraemru8wA7A&s', use_column_width=True)
        st.video('https://www.youtube.com/watch?v=HNFPE1fvJno')
    elif choice == "탐색적 자료 분석":
        run_eda_app()
    elif choice == "머신러닝":
        pass
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
