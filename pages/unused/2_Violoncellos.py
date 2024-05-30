import streamlit as st
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit_vertical_slider as svs
import pandas as pd

st.title('Mix your own violoncello')
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

#C1=np.random.rand(20)
#C2=np.random.rand(20)
#C3=np.random.rand(20)
#np.savez('vectors.npz',C1=C1,C2=C2,C3=C3)
data=np.load('vectors.npz')
C1=(data['C1']+.1)**3
C2=data['C2']+np.linspace(0,.8,20)
C3=data['C3']**2-0.5

df = pd.DataFrame({
    'harmonic' : np.arange(0,20,1),
    'C1' : C1,
    'C2' : C2,
    'C3' : C3,
})
st.markdown('### The three fundamental harmonics of the instruments')
st.line_chart(df,x='harmonic')

Nc=3
columns = st.columns(Nc)
n=np.arange(Nc)
sliders = {}

sliders=np.zeros(Nc)

st.markdown('### Your personal mix - your violoncello.')
for idx, i in enumerate(n):
     key = f'{str(idx)}'
     with columns[idx]:
         sliders[idx] = svs.vertical_slider(key=key, default_value=0.0, step=.1, min_value=-1.0, max_value=1.0)




outp=sliders[0]*C1+sliders[1]*C2+sliders[2]*C3
df2 = pd.DataFrame({
    'harmonic' : np.arange(0,20,1),
    'your note' : outp,
})
st.line_chart(df2,x='harmonic',y='your note')
    