import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

image = Image.open('image/dna.jpg')

st.image(image, use_column_width=True)
st.write(""" 
         # DNA Nucleotide Count Web App
         This app counts the nucleotide composition of query DNA!
         """)

st.header("Enter DNA sequence")

sequence_input  = ">DNA Query\n Enter your data"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence
sequence = ''.join(sequence)

st.write(""" 
***
""")


st.header('INPUT (DNA Query)')
sequence



st.header("OUTPUT (DNA Nucleotide Count)")

