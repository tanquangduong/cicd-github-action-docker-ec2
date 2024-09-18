import streamlit as st
import pandas as pd

# Define the title and logos for the chat interface
APP_TITLE = """<div style="text-align: center">
                <h1 style="font-size: 48px; color: #6366F1;">
                    CICD - GitHub Action x Docker x AWS EC2
                </h1>
                <p>
                    <b style="font-size: 24px">
                        Streamlit App
                    </b>
                </p>
            </div>
        """
LOGO_PATH = "./image/logo_ai.png"


def app():
    # Set the page configuration
    st.set_page_config(
        page_title="Time Series App",  
        page_icon=LOGO_PATH,  
        layout="wide",  
    )
    # Create three columns with specified widths
    c1, c2, c3 = st.columns([1, 5, 1], gap="small")
    with c2:
        st.markdown(APP_TITLE, unsafe_allow_html=True)
    with c3:
        st.image(LOGO_PATH, use_column_width=True)
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")     
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state["dataframe"] = df
        ###
        st.dataframe(df.head())
        st.write(" ")

# Run the app
if __name__ == "__main__":
    app()
