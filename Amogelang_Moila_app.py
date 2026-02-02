# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 22:04:47 2026

@author: NWUUSER
"""
import streamlit as st
import pandas as pd

# ----------------------------
# Page configuration
# ----------------------------
st.set_page_config(
    page_title="Metamorphic Petrology",
    layout="wide"
)

# ----------------------------
# Lecturer & module data
# ----------------------------
name = "Ms. Amogelang Moila"
position = "Lecturer at the NWU and PhD Candidate at University of Witwatersrand"
field = "Geometallurgy and Machine learning"


module_name = "Metamorphic Petrology"
module_code = "GLGN311"
level_of_study = "Year 3"
institution = "North-West University"
textbook = "Prescribed textbook: Winter, J.D. (2014). Principles of igneous and metamorphic petrology, 2nd ed. Pearson"
credits = 16

Study_Unit_1 = "Introduction to Metamorphic Petrology"
Study_Unit_2 = "Classification and Textures of Metamorphic rocks"
Study_Unit_3 = "Textures and structures of Metamorphic terrains"
Study_Unit_4 = "Metamophic Reactions"


# ----------------------------
# Title section
# ----------------------------
st.title("Metamorphic Petrology")
st.subheader(f"{module_code} — {institution}")

# ----------------------------
# Tabs
# ----------------------------
tab1, tab2, tab3 = st.tabs(["Profile", "Module Overview", "Module Content"])

# ============================
# TAB 1: PROFILE
# ============================
with tab1:
    st.header("Lecturer Profile")
    
    st.image(
        "Amogelang Award recipient.jpg",
        caption="Amogelang recieving a Novice Teacher Award"
)
    st.markdown(
        """
        **Name:** Amogelang Moila
        
        **Position:** Lecturer at NWU & PhD Candidate at University of Witwatersrand
        
        **Field:** Geology
        
        **Specialisation:** Geometallurgy and Machine learning  
        """
    )

    with st.expander("Short Bio"):
        st.write(
            """
            I am a geology lecturer at North-West University. In 2025 I received a Novice Teacher Award from the North-West University. I teach the following modules Igneous and Metamorphic petrology and structural geology. I hold an MSc degree in Geology from the University of Joahnnesburg. 
             
            """
        )

# ============================
# TAB 2: MODULE OVERVIEW
# ============================
with tab2:
    st.header("Module Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Module Name:** {module_name}")
        st.write(f"**Module Code:** {module_code}")
        st.write(f"**Level of Study:** {level_of_study}")
        st.write(f"**Credits:** {credits}")
        st.write(f"**Textbook:** {textbook}")


    st.subheader("Module Description")
    st.write(
        """
        This module introduces the principles of metamorphism, metamorphic
        mineral assemblages, textures, and facies. Students develop skills
        in thin section analysis and interpretation of pressure–temperature
        histories of metamorphic rocks.
        """
    )
    
 # ============================
 # TAB 3: MODULE CONTENT
 # ============================
with tab3:
     st.header("Module Content")

     col1, col2 = st.columns(2)

     with col1:
         st.write(f"**Study_Unit_1:** **{Study_Unit_1}**")
         with st.expander("**Introductory Remarks**"):
             st.write(
                 """
**Study time**:
    
Recommended time to master this study unit outcome: 15 hours

**Learning Outcomes**:
    
After engaging with the materials and activities in this study unit you should be able to:
Understand the variation of pressure and temperature in the Earth’s crust.
Understand the role of metamorphic petrology in the reconstruction of pressure and temperature evolution of a specified geological terrain.
 
                  
                 """
             )
         st.write(f"**Study_Unit_2:** **{Study_Unit_2}**")
         with st.expander("**Introductory Remarks**"):
             st.write(
                 """
**Study time**:
    
Recommended time to master this study unit outcome: 25 hours

**Learning Outcomes**:
    
Understand the different schemes for classifying metamorphic rocks.
Be able to use the correct terminology to describe metamorphic rocks.
Understand the metamorphic facies principle
 
                  
                 """
                 )
         st.write(f"**Study_Unit_3:** **{Study_Unit_3}**")
         with st.expander("**Introductory Remarks**"):
             st.write(
                 """
**Study time**:
    
Recommended time to master this study unit outcome: 15 hours

**Learning Outcomes**:
    
Understand that regional metamorphism and deformation go together.
Know the difference between brittle and ductile deformation and their controlling parameters.

Understand the different processes giving rise to the characteristic textures and structures of contact, and to regional metamorphism.
 
                  
                 """
                 )
         st.write(f"**Study_Unit_4:** **{Study_Unit_4}**")
         with st.expander("**Introductory Remarks**"):
             st.write(
                 """
**Study time**:
    
Recommended time to master this study unit outcome: 30 hours

**Learning Outcomes**:
    
Use the petrographic microscope to identify metamorphic minerals.
Use the correct terminology for describing metamorphic mineral textures.
Understand the role of whole-rock chemistry in the formation of new mineral phases.
Understand the difference between net transfer and cationic exchange reactions.
 
                  
                 """
                 )
         st.write(f"**Textbook:** {textbook}")   
         with st.expander("**Introductory Remarks**"):
             st.write(
                 """
**Study time**:
    
Recommended time to master this study unit outcome: 15 hours

**Learning Outcomes**:
    
After engaging with the materials and activities in this study unit you should be able to:
Understand the variation of pressure and temperature in the Earth’s crust.
Understand the role of metamorphic petrology in the reconstruction of pressure and temperature evolution of a specified geological terrain.
 
                  
                 """
                 )



# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("North-West University | School of Geo- and Spatial Sciences")

