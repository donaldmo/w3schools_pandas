import pandas as pd
import streamlit as st

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passing': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

# print(myvar)

st.write(myvar)