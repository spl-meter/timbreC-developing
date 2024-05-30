import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import glob
import seaborn as sns
pi=np.pi
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
#from streamlit_extras.add_vertical_space import add_vertical_space


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

palette = iter(sns.color_palette("Paired"))
c1=np.array(next(palette))
c2=np.array(next(palette))
c3=np.array(next(palette))
c4=np.array(next(palette))
c5=np.array(next(palette))
c6=np.array(next(palette))
c7=np.array(next(palette))
c8=np.array(next(palette))
c9=np.array(next(palette))
c10=np.array(next(palette))
c11=np.array(next(palette))
c12=np.array(next(palette))

# fig = go.Figure(data=[go.Scatter3d(x=[1, 2, 3], y=[4, 5, 6], z=[7, 8, 9], mode='markers')])

# fig.update_layout(scene=dict(xaxis_title='X-axis',
#                              yaxis_title='Y-axis',
#                              zaxis_title='Z-axis'))
# st.plotly_chart(fig)

pl_range=0.3
OP=0.7
#https://plotly.com/python/discrete-color/#color-sequences-in-plotly-express
CSH=px.colors.qualitative.Antique
CSH=px.colors.qualitative.Dark2
CSH=px.colors.qualitative.Safe
MS=3

url="https://doi.org/10.1051/aacus/2023071"
st.markdown("## Violoncellos – the pilot example")
st.markdown(' ')


" We depict three-dimensional harmonic timbre spaces of nine violoncelli's empty strings. The cellist played each note (C, G, D, A) five times in succession – shown as five points for every instrument. These proof-of-concept results demonstrate that the violoncellos form distinct and robust clusters, despite natural variations in human playing and minor differences between like instruments." 

st.markdown(' ')

" The harmonic basis vectors defining the diagrams’ axes – the principal harmonic timbres – emerge without prior assumptions from measured sound color differences within the collection of instruments of the same type. They describe sound color variations within that instrument type as efficiently as possible. They have a direct concrete auditory meaning that can be listened to and are the basis of an instrument type’s harmonic timbre coordinates." 
st.markdown(' ')
#"See the paper “Quantifying sound colour of musical instruments – precise harmonic timbre coordinates of like instruments” published (open access) in Acta Acustica for audio examples and further explanation." 

st.markdown("See the paper ['Quantifying sound colour of musical instruments – precise harmonic timbre coordinates of like instruments'](%s) published (open access) in Acta Acustica for audio examples and further explanation." % url)








struna='G'
dfG=pd.DataFrame(columns=['c1','c2','c3','violoncello','size'])
fajl = sorted(glob.glob('data/celos1/*'+struna+'.npz'))

for kk in range(len(fajl)):
    [a,b]=dfG.shape

    data=np.load(fajl[kk])
    x=data['x']
    y=data['y']
    z=data['z']
    besed=str(data['celo'])
    besed=str(kk+1)
    n=len(x)
    
    for nn in range(a,a+n):
        dfG.loc[nn,'c1']=x[nn-a]
        dfG.loc[nn,'c2']=y[nn-a]
        dfG.loc[nn,'c3']=z[nn-a]
        dfG.loc[nn,'violoncello']=besed
        dfG.loc[nn,'size']='a'


struna='D'
dfD=pd.DataFrame(columns=['c1','c2','c3','violoncello'])
fajl = sorted(glob.glob('data/celos1/*'+struna+'.npz'))

for kk in range(len(fajl)):
    [a,b]=dfD.shape

    data=np.load(fajl[kk])
    x=data['x']
    y=data['y']
    z=data['z']
    besed=str(data['celo'])
    besed=str(kk+1)
    n=len(x)
    
    for nn in range(a,a+n):
        dfD.loc[nn,'c1']=x[nn-a]
        dfD.loc[nn,'c2']=y[nn-a]
        dfD.loc[nn,'c3']=z[nn-a]
        dfD.loc[nn,'violoncello']=besed


struna='A'
dfA=pd.DataFrame(columns=['c1','c2','c3','violoncello'])
fajl = sorted(glob.glob('data/celos1/*'+struna+'.npz'))

for kk in range(len(fajl)):
    [a,b]=dfA.shape

    data=np.load(fajl[kk])
    x=data['x']
    y=data['y']
    z=data['z']
    besed=str(data['celo'])
    besed=str(kk+1)
    n=len(x)
    
    for nn in range(a,a+n):
        dfA.loc[nn,'c1']=x[nn-a]
        dfA.loc[nn,'c2']=y[nn-a]
        dfA.loc[nn,'c3']=z[nn-a]
        dfA.loc[nn,'violoncello']=besed


struna='C'
dfC=pd.DataFrame(columns=['c1','c2','c3','violoncello'])
fajl = sorted(glob.glob('data/celos1/*'+struna+'.npz'))

for kk in range(len(fajl)):
    [a,b]=dfC.shape

    data=np.load(fajl[kk])
    x=data['x']
    y=data['y']
    z=data['z']
    besed=str(data['celo'])
    besed=str(kk+1)
    n=len(x)
    
    for nn in range(a,a+n):
        dfC.loc[nn,'c1']=x[nn-a]
        dfC.loc[nn,'c2']=y[nn-a]
        dfC.loc[nn,'c3']=z[nn-a]
        dfC.loc[nn,'violoncello']=besed

    


#with st.expander("3D scatter plot representation"):
#col1, col2 = st.columns(2)
FAK=1.4

GRminor="rgba(0.2, 0.2, 0.2,0.3)"
GRmajor="rgba(0.4, 0.4, 0.4,0.3)"

figC = px.scatter_3d(dfC, x='c1', y='c2', z='c3',  color='violoncello',title='C string', opacity=OP, color_discrete_sequence=CSH,
                        range_x=[-pl_range*FAK,pl_range*FAK],range_y=[-pl_range*FAK,pl_range*FAK],range_z=[-pl_range*FAK,pl_range*FAK],height=800)
figC.update_traces(marker_size = MS)

figC.update_layout(legend= {'itemsizing': 'constant'},scene = dict(
                        xaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        yaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        zaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),),
                     )

st.plotly_chart(figC, theme="streamlit", use_container_width=False)

figG = px.scatter_3d(dfG, x='c1', y='c2', z='c3',  color='violoncello',title='G string', opacity=OP, color_discrete_sequence=CSH,
                        range_x=[-pl_range*FAK,pl_range*FAK],range_y=[-pl_range*FAK,pl_range*FAK],range_z=[-pl_range*FAK,pl_range*FAK],height=800)
figG.update_traces(marker_size = MS)
figG.update_layout(legend= {'itemsizing': 'constant'},scene = dict(
                        xaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        yaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        zaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),),
                     )
st.plotly_chart(figG, theme="streamlit", use_container_width=True)

figD = px.scatter_3d(dfD, x='c1', y='c2', z='c3',  color='violoncello',title='D string', opacity=OP, color_discrete_sequence=CSH,
                        range_x=[-pl_range*FAK,pl_range*FAK],range_y=[-pl_range*FAK,pl_range*FAK],range_z=[-pl_range*FAK,pl_range*FAK],height=800)
figD.update_traces(marker_size = MS)
figD.update_layout(legend= {'itemsizing': 'constant'},scene = dict(
                        xaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        yaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        zaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),),
                     )
st.plotly_chart(figD, theme="streamlit", use_container_width=True)

figA = px.scatter_3d(dfA, x='c1', y='c2', z='c3',  color='violoncello',title='A string', opacity=OP, color_discrete_sequence=CSH,
                        range_x=[-pl_range*FAK,pl_range*FAK],range_y=[-pl_range*FAK,pl_range*FAK],range_z=[-pl_range*FAK,pl_range*FAK],height=800)
figA.update_traces(marker_size = MS)
figA.update_layout(legend= {'itemsizing': 'constant'},scene = dict(
                        xaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        yaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),
                        zaxis = dict(backgroundcolor="rgba(0, 0, 0,0)",gridcolor=GRminor,showbackground=True,zerolinecolor=GRmajor),),
                     ) 
st.plotly_chart(figA, theme="streamlit", use_container_width=True)


# st.title('Staro besedilo spodaj')
# st.markdown(""" The position of musical insuturments in the timbre space can be represented in diffrent ways. If only the first three basis vectors are needed, a 3D 
# scatter plot is convinient, showing how instruments differ in any of the dimensions. 
# On the other hand, such representation is not possible anymore if more basis vectors are required. In such case, we can use simple line plots.""")



# fig2DG= go.Figure()
# fig2DD= go.Figure()
# fig2DA= go.Figure()
# fig2DC= go.Figure()

# fig2DG.update_layout(
#         title="G string", 
#         xaxis_title="c [/]", yaxis_title="component",height=400
#         )
# fig2DD.update_layout(
#         title="D string", 
#         xaxis_title="c [/]", yaxis_title="component",height=400
#         )
# fig2DA.update_layout(
#         title="A string", 
#         xaxis_title="c [/]", yaxis_title="component",height=400
#         )
# fig2DC.update_layout(
#         title="C string", 
#         xaxis_title="c [/]", yaxis_title="component",height=400
#         )


# def colrgb(kk):
#     kk=int(kk)

#     if kk==1: cc=1*c1
#     if kk==2: cc=1*c2
#     if kk==3: cc=1*c3
#     if kk==4: cc=1*c4
#     if kk==5: cc=1*c5
#     if kk==6: cc=1*c6
#     if kk==7: cc=1*c7
#     if kk==8: cc=1*c8
#     if kk==9: cc=1*c9
#     if kk==10: cc=1*c10
#     if kk==11: cc=1*c11
#     if kk==12: cc=1*c12
#     tek='rgb('+str(int(cc[0]*255))+','+str(int(cc[1]*255))+','+str(int(cc[2]*255))+')'
#     return tek

# for kk in range(1,10):
    
#     xx=dfG.c1[dfG['violoncello']==str(kk)].values
#     yy=dfG.c2[dfG['violoncello']==str(kk)].values
#     zz=dfG.c3[dfG['violoncello']==str(kk)].values

#     fig2DG.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[0],yy[0],zz[0]], name="instrument "+str(kk),opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
#     for pp in range(1,len(xx)):
#         fig2DG.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[pp],yy[pp],zz[pp]], showlegend=False, opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
    
#     xx=dfD.c1[dfD['violoncello']==str(kk)].values
#     yy=dfD.c2[dfD['violoncello']==str(kk)].values
#     zz=dfD.c3[dfD['violoncello']==str(kk)].values

#     fig2DD.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[0],yy[0],zz[0]], name="instrument "+str(kk),opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
#     for pp in range(1,len(xx)):
#         fig2DD.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[pp],yy[pp],zz[pp]], showlegend=False, opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
    
    
#     xx=dfA.c1[dfA['violoncello']==str(kk)].values
#     yy=dfA.c2[dfA['violoncello']==str(kk)].values
#     zz=dfA.c3[dfA['violoncello']==str(kk)].values

#     fig2DA.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[0],yy[0],zz[0]], name="instrument "+str(kk),opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
#     for pp in range(1,len(xx)):
#         fig2DA.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[pp],yy[pp],zz[pp]], showlegend=False, opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
    
#     xx=dfC.c1[dfC['violoncello']==str(kk)].values
#     yy=dfC.c2[dfC['violoncello']==str(kk)].values
#     zz=dfC.c3[dfC['violoncello']==str(kk)].values

#     fig2DC.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[0],yy[0],zz[0]], name="instrument "+str(kk),opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
#     for pp in range(1,len(xx)):
#         fig2DC.add_trace(go.Scatter(y=['c1','c2','c3'], x=[xx[pp],yy[pp],zz[pp]], showlegend=False, opacity=OP, mode="lines+markers",line_color=colrgb(str(kk))))#,line_color='rgb('+str(int(kk/9.0*255))+',0,0)'))
    
    



# #with st.expander("Label representation"):

# col1, col2 = st.columns(2)    
# col1.plotly_chart(fig2DG, theme="streamlit", use_container_width=True)
# col2.plotly_chart(fig2DD, theme="streamlit", use_container_width=True)
# col1.plotly_chart(fig2DA, theme="streamlit", use_container_width=True)
# col2.plotly_chart(fig2DC, theme="streamlit", use_container_width=True)



