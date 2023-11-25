import streamlit as st
import utils as utl
from views import search, email, digitalhuman, mode, audio

# st.set_page_config(layout="wide", page_title='Navbar sample')
st.set_option('deprecation.showPyplotGlobalUse', False)
# utl.inject_custom_css()
# utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "search":
        search.load_view()
    elif route == "email":
        email.load_view()
    elif route == "digitalhuman":
        digitalhuman.load_view()
    elif route == "mode":
        mode.load_view()
    elif route == "audio":
        audio.load_view()
    elif route == None:
        email.load_view()
        
navigation()