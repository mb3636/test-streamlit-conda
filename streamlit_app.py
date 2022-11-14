import streamlit as st

def main():
    # set page layout
    st.set_page_config(layout='wide')
    # info
    st.markdown(readme())

@st.cache()
def readme():
    with open('README.md', 'r') as f:
        return f.read()


if __name__ == "__main__":
    main()