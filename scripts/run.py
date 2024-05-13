# store this as run-streamlit.py
from streamlit.web import cli
import os

def interface():
    pa = os.path.dirname(__file__)
    print(pa)
    cli.main_run([pa + "/Interface/Home_Page.py"])

if __name__ == "__main__":
    interface()