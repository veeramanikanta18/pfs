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

sequence_input  = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

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

st.subheader('1.Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])

    return d

X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())
X

## display dataframe

st.subheader('Display dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

### display Bar chart using altair

st.subheader("Display Bar chart")

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width = alt.Step(80) # controls width of bar
)

st.write(p)