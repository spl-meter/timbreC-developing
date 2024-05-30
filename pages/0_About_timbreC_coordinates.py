import streamlit as st
import plotly.graph_objects as go
import numpy as np


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




st.markdown('## About timbreC coordinates')
st.markdown(' ')
" timbreC – harmonic timbre coordinates are simple numbers that quantify harmonic timbre of a musical instrument and place it in a multidimensional harmonic timbre space tailored to that instrument type. For instance, within such a space for violins, the sound of certain regions might be identified as bright, dark, warm, nasal, mellow, wide, focused ... While such qualitative and intuitive descriptors may run out or lack consensus, timbre coordinates offer an objective quantification of sound color for specific instrument type, independent of subjective impressions. Moreover, regardless of potential psychoacoustic interpretations of harmonic space regions, they quantify harmonic similarity and dissimilarity between instruments: instruments with coordinates close together sound similar, while those with coordinates further apart sound notably different."
st.markdown(' ')
'##### Examples of application include:'
st.markdown('- primary timbre quantification in production and marketing of instruments (instrument’s timbre label),')
st.markdown('- tracking changes of timbre, e.g. due to ageing, environment, conditioning, repairs ...,')
st.markdown('- detecting instrument damage or counterfeiting,')
st.markdown('- providing quantitative sound color basis for design and optimization of an instrument’s sound,')
st.markdown("""- extension to other areas, such as home appliances: serving as the basis for psychoacoustic noise annoyance tests to shape 'pleasant' machine noise guidlines.""")
st.markdown(' ')
'##### Key development principles, crucial for relevance and feasibility of timbreC:'
st.markdown('- The coordinates must refer to the circumstances under which the instrument is normally used – they should be measured while the instrument is excited by a musician in usual playing.')
st.markdown('- Measurements should take place in a suitable live concert hall and should not require specialized environments like anechoic or reverberation chambers, which are not musically realistic and usually not available in artistic venues.') 
st.markdown('- Notwithstanding natural variations due to the involvement of the musician, as well as differences between acoustic environments, the coordinates must be robust, reproducible, and independent of the concert hall used for recording.')

# st.title('Staro besedilo - spodaj')
# data=np.load('data/waveform.npz')

# t=data['t']
# s1=data['s1']
# s1B=data['s1B']


# figSIG = go.Figure()
# figSIG.add_trace(go.Scatter(x=t, y=s1, name="Recorded signal", mode="lines"))
# figSIG.add_trace(go.Scatter(x=t, y=s1B, name="Stationary sections", mode="lines"))
# figSIG.update_layout(
#     #title="A typical recording of an instrument from a single microphone", 
#     xaxis_title="time [s]", yaxis_title="Sound pressure [a.u.]",height=320
# )


# data=np.load('data/vektorcki.npz')
# XT=data['XT']
# vek_1=data['vek_1']
# vek_2=data['vek_2']
# vek_3=data['vek_3']

# figVEK = go.Figure()
# figVEK.add_trace(go.Scatter(x=XT, y=vek_1, name="instrument 1", mode="lines+markers"))
# figVEK.add_trace(go.Scatter(x=XT, y=vek_2, name="instrument 2", mode="lines+markers"))
# figVEK.add_trace(go.Scatter(x=XT, y=vek_3, name="instrument 3", mode="lines+markers"))

# figVEK.update_layout(
#     #title="A typical recording of an instrument from a single microphone", 
#     xaxis_title="harmonic [/]", yaxis_title="integrated power level [a.u.]",height=400
# )



# st.title('About timbre coordinates')

# st.markdown('### The challenge')


# st.markdown("""The differences between the sounds of musical instruments of the same type, although clearly audible to experts, are extremely small. 
# Small compared to the sensitivity of recording an instrument. Surprisingly, the sound varies much more if we change the position of the microphone, the room and/or its acoustics, the way the musician handles the instruments!""")
# st.markdown('*<div style="text-align: right;">Timbre is intangible. Almost intangible. It was intangible!</div>*', unsafe_allow_html=True)


# st.markdown("""The challenge in this regars is to obtain a universal and robust recording of a musical instrument that is stable enough to analyze even the smallest differences between instruments – in order to extract TimbREC. """)
# with st.expander("How to record musical instrument?"):
#     st.write(' A more detailed decription with photos about recording the instruments.')

# st.markdown('### What is TimbREC')


# st.markdown("""A skilled musician plays the same note on a large number of musical instruments. Each instrument is recorded and from the recording of 
# each microphone the stationary sound is extracted. This is how a recorded soundpressure level typically looks!""")
            
# st.plotly_chart(figSIG, theme="streamlit", use_container_width=True)
# st.markdown("""Out of the stationary sections, the frequency spectrum is calculated and from there the power sd distributed between harmonic components. 
# This distribution varies between musical instruments as shown here:""") 

# st.plotly_chart(figVEK, theme="streamlit", use_container_width=True)
# st.markdown("""The values graphically shown above, can be represented as a sequence of numbers - a vector:""")
# st.latex(r'''\mathbf{h}=\left[h_0, h_1, h_2...\right]''') 
# st.markdown("""Typically, 20 lowest components are sufficient to represent an instrument.""")

# st.markdown('#### Applying PCA')

# st.markdown("""Harmonic vectors, **h** corresponding to the different instruments, are then analyzed with PCA. This is a well established method about which, 
# you can read more on [Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis).
            
# PCA constructs the timber space by providing orthonormal basis vectors. They are as many as harmonics were analysed but ordered by importance. It turnes out that
# using the first 3 almost offer a almost complete description. We named them timbre$_1$, timbre$_2$ and timbre$_3$ and have the same length as the harmonic vectors.

# The timbre components are important because they are orthogonal to each other. This means that every vector (and every instrument!) can be represented by a linear combination of different timbre components.""")
# st.latex(r'''\mathbf{h}=c_1\cdot timbre_1 + c_2 \cdot  timbre_2 + c_3 \cdot timbre_3.''') 
# st.markdown("""c$_1$, c$_2$ and c$_3$ are numbers - timbre coodrinates coordinates of the timbrem that represent the position of a musical instrument in timbre space. 
# They are analogous x, y, z - the spatial coordinates of a point in space! """)


# st.markdown('### The power of TimbREC')

# st.markdown("""Let us mention some of the several features of timbre that are significant. 

# The distance between two points in the timbre space corresponds to the difference in the sound of two instruments. By analyzing instruments in this way, we can determine which instruments sound different and which sound the same. This has the potential applications of labeling instruments, for example for online sales, grouping instruments based on their particular timbre, e.g., from the same manufacturer, from the same region, etc.
# Check how this looks for violoncellos!
            
# We can listen to the timbre components and even mix them to create the sound of a musical instrument – existing and non-existing! This allows us to investigate timbre space, explore personal preferences for instruments, and much more!
# Listen to violoncellos this way!""")


# st.markdown('### The limitations of the approach')

# st.markdown("""TimREC is based on the analysis of the stationary sound of musical instruments, i.e., the distribution of harmonic components in the sound. However, this is not a complete description of a musical instrument; in particular, it does not take into account the time-varying properties of musical instruments, such as attack and sustain. One must also be aware that the value of a musical instrument is also determined by other factors, such as its playability and historical significance""")


# st.markdown('### Future challenges')

# st.markdown("""The concept of timbre was developed on the working example of violoncellos. We are currently testing it on violins and plan to extend it to other instruments.
# Next, we are investigating how the concept can be applied to non-musical sound sources. Machines, household appliances, engines… all of these can be analyzed with this innovative tool.""")