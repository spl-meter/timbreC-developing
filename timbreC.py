import streamlit as st
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
#import streamlit_vertical_slider as svs
import pandas as pd
#from streamlit_extras.add_vertical_space import add_vertical_space



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


#st.title('timbreC')
st.markdown('## **timbreC** - The harmonic timbre coordinates')

st.image('data/vilolins.jpeg',caption='A pioneering path from instrument’s sound to numeric specification of its color')

#st.markdown('---')

#st.page_link("timbreC.py", label="Home", icon="🏠")
#st.sidebar.page_link("pages/2_The_team.py", label='k')#"Towards worldwide timbre spaces of sustaining musical instruments")

#st.divider()
#st.caption('Towards worldwide timbre spaces of sustaining musical instruments')
#st.code('Towards worldwide timbre spaces of sustaining musical instruments')

st.markdown(' ')
st.markdown(' ')
st.latex('\\textit{---}\\textsf{~~~Towards worldwide timbre spaces of sustaining musical instruments~~~}\\textit{---}')
st.markdown(' ')
st.markdown(' ')
# st.markdown('---')
# st.markdown(' ')
# st.markdown(' ')
# st.latex('\\textit{Towards worldwide timbre spaces of sustaining musical instruments}')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown('---')
# st.markdown(' ')
# st.markdown(' ')
# st.latex('\\textrm{Towards worldwide timbre spaces of sustaining musical instruments}')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown('---')
# st.markdown(' ')
# st.markdown(' ')
# st.latex('\\textsc{Towards worldwide timbre spaces of sustaining musical instruments}')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown('---')
# st.markdown(' ')
# st.markdown(' ')
# st.latex('\\textsl{Towards worldwide timbre spaces of sustaining musical instruments}')
# st.markdown(' ')
# st.markdown(' ')
# st.markdown('---')


'timbreC (patent pending) is a proprietary know-how for translation from physical sound color to abstract multidimensional timbre spaces. A quantification of sound color.'

url="https://doi.org/10.1051/aacus/2023071"

#st.markdown("The open access article about timbreC has been published in [Acta Acustica](%s)." % url)

st.markdown("Published in Acta Acustica: [doi.org/10.1051/aacus/2023071](%s) (open access)." % url)

st.markdown("""Prospective investors and collaborators are invited to contact us at rok.prislan@innorenew.eu or daniel.svensek@gmail.com.""")          

# st.title('Staro besedilo - spodaj')
# st.markdown('*TimbREC is a technology, an approach, the knowledge behind quantifying timbre - also known as the color of sound.*')
           

# st.markdown("""This is the website of the TimbREC project, where you can learn more about the approach developed. The theoretical background is explained, the results are presented, and best of all, you can listen to musical instruments in the Timbre space.
 
# If you are further interested in the project, if you know of innovative ways to implement the technology, if you would like to collaborate - please contact the authors by email at rok.prislan@innorenew.eu.""")
















#st.image("pages/data/team.jpeg",caption='A moment from recording sessions.')



# st.markdown("""
# <style>
# .css-6q9sum.ef3psqc3
# {
#     visibility: hidden;
# }
# .css-z3au9t.ea3mdgi2
# {
#     visibility: hidden;
# }
# .css-cio0dv.ea3mdgi1
# {
#     visibility: hidden;
# }
# </style>
# """,unsafe_allow_html=True)


# st.title('The TibREC project') 
# st.subheader('Introduction')
# st.header('The authors')
#st.text("The project was born as a pure intrest in the understaning of the sound quality of musical instruments.")
# st.markdown("**No sound** is *alone*")  
# st.markdown('---')
# a = """[josko](https://www.google.com)"""
# st.markdown(a)
# st.latex('X_i=\int_0^\infty={q \cdot 4f \over x\ \cdot y} dX')
# j={"a":"1,2,3","B":"4,5,6"}
# st.json(j)

# b="""
# def code():
#     print(kk)
# """
# st.code(b,language="python")

# st.write("## H2 ")
# st.metric(label="speed", value=" 120 ms⁻¹ ",delta="4 ms⁻¹ ")

# d=pd.DataFrame({"volum 1":[1,2,3,4],"volum 2":[4,2,3,4]})
# st.table(d)
# st.dataframe(d)

# st.image("data/uho.png",caption='Cool image',width=190)

# st.audio("data/Afrika.mp3",start_time=30)

# def onchange():
#     r=np.random.rand()
#     st.write(r)
#     st.write(st.session_state.CKBKEY)

# state=st.checkbox('CKB',value=True,on_change=onchange,key='CKBKEY')

# if state:
#     st.write('Hi')
# else:
#     pass

#rb1=st.radio("Od kod si?",options=("US","UK","Canada"),on_change=onchange,key='CKBKEY')

#bo=st.button('Helowing',on_click=onchange,key='CKBKEY')
# sele=st.selectbox("what is your car",options=("BMW","citroen",'TAM'))
# st.write(sele)
# sele=st.multiselect("what is your car",options=("BMW","citroen",'TAM'))
# st.write(sele)

#col1, col2=st.columns(2)

# cc1='green'
# cc2='lightgray'
# cc3='red'

# svs.vertical_slider(key='vs1', default_value=0, step=0.1,min_value=-1.0, max_value=1.0,slider_color= cc1,track_color=cc2,thumb_color = cc3)
# svs.vertical_slider(key='vs2', default_value=0, step=0.1,min_value=-1.0, max_value=1.0,slider_color= cc1,track_color=cc2,thumb_color = cc3)

# svs.vertical_slider()
# st.markdown("---")
#image=st.file_uploader("upload and image",type=['png','jpg'])
#if image is not None:
#    st.image(image)