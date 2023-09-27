import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Title
st.write('Name: Tanisha Dhopeshwar')
st.write('Student ID: 017411199')
# getting path of directory
path = os.path.dirname(__file__)

# dataset path
dataset_path = path + '/Fish.csv'
# reading the dataset
Fish = pd.read_csv(dataset_path)

#Weight = Fish[‘Weight’]
#Height = Fish[‘Height’]
#Width = Fish[‘Width’]
#Length1 = Fish [‘Length1’]
#Length2 = Fish[‘Length2’]
#Length3 = Fish[‘Length3’]

Species = Fish['Species']

Weight = Fish ['Weight']



# Create a bar chart
plt.bar(Species, Weight)

# Add labels and title
plt.xlabel(Species)
plt.ylabel(Avg Weight of Species)
plt.title('Bar Chart Example')

# Rotate x-axis labels if they are long
plt.xticks(rotation=45, ha='right')

st.pyplot(plt)


