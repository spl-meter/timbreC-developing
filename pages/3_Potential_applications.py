import streamlit as st

st.markdown('## Potential applications')


st.markdown(' ')
"Some potential applications of TimbreC are presented as examples."
            

st.markdown(' ')
st.markdown(' ')
st.markdown('### Online musical instrument store')
st.markdown(' ')
"TimbreC are labels for musical instruments that quantify their sound color. They can be used as a filter for customers to select the instrument of their choice."

#with st.expander("Check an example"):
#st.image("https://static.streamlit.io/examples/dice.jpg")
st.image("data/webpage_coordinates2.jpeg")

    
st.markdown(' ')
st.markdown(' ')
st.markdown('### Determine timbreC of your instrument')
st.markdown(' ')
"The only strict requirement for recording the coordinates of your own instruments is a sufficiently large and quiet room. "
#with st.expander("Check an example"):
st.write('The acquisition is performed in 3 consecutive steps.')
col1, col2, col3 = st.columns(3)

col1.write('1) Record')
col1.image("data/recording2.jpeg")

col2.write('2) Process in the cloud')
col2.image("data/server.jpeg")

col3.write('3) Retrieve the coordinates')
col3.image("data/phone.jpeg")




st.write('timbreC can be used to assess the value of musical instruments, track changes over time, detect damage, confirm authenticity and improve the design and production process.')
col1, col2, col3,col4,col5 = st.columns([1, 1,1,1,1])

col1.image("data/integrity.jpeg")
col2.image("data/price.jpeg")
col3.image("data/break.jpeg")
col4.image("data/optimize.jpeg")
col5.image("data/work.jpeg")


#st.write('A mobile app is required for recording and communication with the cloud-based backend. Using the cello as an example, it was tested that the mems microphones integrated into the phones provide sufficient fidelity for recording. Alternatively, any computer-based recording method can be used to create the recordings, which are then transferred to the cloud via a web-based user interface.')

st.markdown(' ')
st.markdown(' ')
st.markdown('### timbreC of noise sources')
st.markdown(' ')

"The coordinates can be determined for any sound source with a sufficiently harmonic spectrum. A possible extension of the technology would be to apply it to machines with rotating elements that generate noise with such characteristics, including washing machines, HVAC systems, internal combustion engines and electric motors."
col1, col2, col3 = st.columns(3)

#col1.write('washing machines')
col1.image("data/washing.jpeg")
#col2.write('exhaust systems')
col3.image("data/ekhaust.jpeg")
#col3.write('HVAC')
col2.image("data/hvac.jpeg")

st.write('In combination with the standardized acoustic measures of noise sources (e.g. sound power level), timbreC can help you to select your preferred (or less annoying!) device. The timbreC labels can be used as labels that facilitate the online sales process.')
