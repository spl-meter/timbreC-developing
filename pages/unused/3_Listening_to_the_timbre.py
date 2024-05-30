import streamlit as st
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit_vertical_slider as svs
import pandas as pd
st.title('Listening')

col1, col2=st.columns(2)

x=np.array([1,2,1.45,4,3])
y=np.arange(1,6,1)
xerr=np.random.rand(5)



x[4]=col2.slider('', min_value=-2.0, max_value=2.0, value=0.0, step=0.1, format='%f', key='C5')#, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
x[3]=col2.slider('', min_value=-2.0, max_value=2.0, value=0.0, step=0.1, format='%f', key='C4')#, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
x[2]=col2.slider('', min_value=-2.0, max_value=2.0, value=0.0, step=0.1, format='%f', key='C3')#, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
x[1]=col2.slider('', min_value=-2.0, max_value=2.0, value=0.0, step=0.1, format='%f', key='C2')#, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
x[0]=col2.slider('', min_value=-2.0, max_value=2.0, value=0.0, step=0.1, format='%f', key='C1')#, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.write(x)
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=xerr,marker='s',ls='')
ax.plot(x, y,ls='-')
ax.set_yticks(y)
ax.set_xlim(-3,3)
col1.pyplot(fig)

svs.vertical_slider(key='p', 
                    default_value=4, 
                    step=1, 
                    min_value=0, 
                    max_value=100,
                    slider_color= 'green', #optional
                    track_color='lightgray', #optional
                    thumb_color = 'red' #optional
                    )