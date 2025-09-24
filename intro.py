import streamlit as st 
import os
import pandas as pd
st.write("Hello world 123456")


print("run")
presses= st.button("Press me")
print(presses)


st.title("Super simple Title")
st.header("This is a header")

st.markdown("This is _Markdown_")

st.caption("smalll text")

code_example="""
 def greet(name):
 print('hello',name)
"""

st.code(code_example,language='python')

st.divider()

st.image(os.path.join(os.getcwd(),"static","BG.png"))
# To  put image we ned to have folder name static 

df=pd.DataFrame({
    "Name":['alice','bob','charlie','david'],
    'Age':[25,34,21,34],
    'Occupations':['Engineer','Doctor','Artist','Chef'] 
})
st.dataframe(df)