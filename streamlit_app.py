# Add recipe title and image (create helper function for that in recipes module)
import streamlit as st

from recipes import *

# st.sidebar.selectbox("Pick Property", PROPERTY_IDS)

RECIPE_URL = SAMPLE_RECIPE_URL

RECIPE_DETAILS = get_recipe_details(RECIPE_URL)

STEPS = RECIPE_DETAILS['steps']

# Draw a title and some text to the app:
'''
# :pizza: Pizza Recipe

'''


recipe_step_col1, recipe_step_col2 = st.columns(2)

# Ingredients
with recipe_step_col1:
    st.markdown(f'### Ingredients for the Base')
    for ingredient in RECIPE_DETAILS['ingredients1']:
        st.markdown(f'{ingredient}')

    st.markdown(f'### Ingredients for the Topping')
    for ingredient in RECIPE_DETAILS['ingredients2']:
        st.markdown(f'{ingredient}')



# # Steps 
with recipe_step_col2:
    st.markdown(f'### Steps')
    for i, step in enumerate(STEPS):
        with st.expander("Step" + str(i + 1), expanded=True, icon='🧂'):
            step
            
        
