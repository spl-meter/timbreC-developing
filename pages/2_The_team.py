import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown('## People behind the project')
st.markdown(' ')
st.markdown("""In 2019, two scientists and a cello professor united our expertise when faced with the task of selecting better instruments for performers in the cello class. Amidst numerous listening tests, a simple yet pragmatic question arose: Could the sound color of an instrument played by a human musician be accurately and robustly measured? That is, to the extent that minute differences between like instruments – something we can hear but not quantify – can be reproducibly determined.

 

The question evolved into years of research focused on this precise goal: systematic measuring, testing, analyzing, and constant optimizing to turn the ideas confronted with hard physical reality into a tangible solution. Now, we have the privilege of advancing this evolving technology to enhance the world of musical instruments and transcend our understanding of sound.""")

# st.markdown('---')

# st.markdown('##### *This is not just a project, it is an odyssey of acoustic innovation.*', unsafe_allow_html=True)

# st.markdown('---')

st.markdown(' ')
st.markdown(' ')
st.latex('\\textit{---}\\textsf{~~~This is not just a project, it is an odyssey of acoustic innovation~~~}\\textit{---}')

st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

st.markdown("""*The development of timbreC was carried out as part of the research activities of the InnoRenew CoE acoustics laboratory.*""")

[c1, c2, c3]=st.columns(3)

# c1.image("data/DS.jpg",caption='Daniel Svenšek \n daniel.svensek@gmail.com')
# c2.image("data/RP.jpeg",caption='Rok Prislan \n rok.prislan@innorenew.eu')
# c3.image("data/UP2.jpg",caption='Urša Kržič \n ursa.pavlovcic@gmail.com')




c1.write('Daniel Svenšek \n daniel.svensek@gmail.com')
c2.write('Rok Prislan \n rok.prislan@innorenew.eu')
c3.write('Urša Kržič \n ursa.pavlovcic@gmail.com')
#st.image("data/team.jpeg")
st.image("data/team.jpeg",caption='A moment from recording sessions')

# st.title('Staro besedilo - spodaj')
# st.image("data/team.jpeg",caption='A moment from recording sessions.')
            
# st.markdown("### The infrastructure and support")

