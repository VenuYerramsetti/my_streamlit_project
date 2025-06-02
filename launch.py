#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import webbrowser
import time

# Run Streamlit app in new CMD window (Windows)
os.system("start cmd /k streamlit run streamlit_app.py")

# Wait 3 seconds to let Streamlit start, then open browser
time.sleep(3)
webbrowser.open("http://localhost:8501")

