import streamlit as st

st.markdown('## Potential applications')


st.markdown(' ')
"Some potential applications of TimbreC are presented as examples."
            

st.markdown(' ')
st.markdown(' ')
st.markdown('### 1) Online sell of musical instruments')
st.markdown(' ')
st.markdown("""TimbreC are labels for musical instruments that quantify their sound color. As such, they can be used as a filter for customers to select the instrument of their choice.""")

#with st.expander("Check an example"):
#st.image("https://static.streamlit.io/examples/dice.jpg")
st.image("data/webpage_coordinates.jpeg")

    
st.markdown(' ')
st.markdown(' ')
st.markdown('### 2) Record timbreC of your instrument')
st.markdown(' ')
st.markdown("""The only strict requirement for recording the coordinates of your own instruments is a sufficiently large and quiet room. In such a room, the position-specific features are averaged out by walking around while recording the sound of the playing instrument. This offers a technically simple implementation for recording coordinates - with a smartphone.""")

#with st.expander("Check an example"):
st.write('The acquisition is performed in 3 consecutive steps.')
col1, col2, col3 = st.columns(3)

col1.write('1) Record')
col1.image("data/recording2.jpeg")

col2.write('2) Process in the cloud')
col2.image("data/server.jpeg")

col3.write('3) Retrieve the coordinates')
col3.image("data/phone.jpeg")

st.write('A mobile app is required for recording and communication with the cloud-based backend. Using the cello as an example, it was tested that the mems microphones integrated into the phones provide sufficient fidelity for recording. Alternatively, any computer-based recording method can be used to create the recordings, which are then transferred to the cloud via a web-based user interface.')

st.markdown(' ')
st.markdown(' ')
st.markdown('### 3) timbreC of noise sources')
st.markdown(' ')
st.markdown("""Not yet tested, but the coordinates can be determined for any sound source with a sufficiently harmonic spectrum. A possible extension of the technology would be to apply it to machines with rotating elements that generate noise with such a characteristic. """)

#with st.expander("Check an example"):
st.write('Noise sources with dominant harmonic components include household appliances, electric motors and internal combustion engines. A few examples are washing machines, exhaust systems and HVAC systems.')
col1, col2, col3 = st.columns(3)

#col1.write('washing machines')
col1.image("data/washing.jpeg")
#col2.write('exhaust systems')
col2.image("data/ekhaust.jpeg")
#col3.write('HVAC')
col3.image("data/hvac.jpeg")

st.write('In combination with the standardized acoustic measures of noise sources (e.g. sound power level), timbreC can help you to select your preferred (or less annoying!) device. The timbreC labels can be used as labels that facilitate the online sales process.')
