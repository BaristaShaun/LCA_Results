import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from PIL import Image

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Jump to Section:", ["Project Overview", "LCI - System Boundary", "LCA Results", "Insights"])

# Title
st.title("LCA Report: Bio-SAC Production")

# Section: Project Overview
if section == "Project Overview":
    st.header("Project Overview")
    st.write("This Life Cycle Assessment (LCA) follows ISO 14044 standards to evaluate the environmental impact of Bio-SAC production.")

    with st.expander("ISO Standards"):
        st.write("This study is conducted based on ISO 14044 guidelines.")

    with st.expander("Functional Unit"):
        st.write("The functional unit is **1 kg of Bio-SAC** produced. This ensures consistency when comparing environmental impacts.")

    with st.expander("Allocation Method"):
        st.write("Co-product allocation: The environmental burden is divided based on the economic value of the co-products.")

    with st.expander("Impact Categories Assessed"):
        st.write("""
        The following EF3.1 impact categories are considered:
        - **Global Warming Potential (GWP)** (kg CO₂-eq)
        - **Cumulative Energy Demand (CED)** (MJ)
        - **Water Use** (L)
        """)

# Section: LCI - System Boundary & Inputs
elif section == "LCI - System Boundary":
    st.header("Life Cycle Inventory (LCI) - System Boundary")

    # System Boundary Image
    st.subheader("System Boundary Diagram")
    try:
        image = Image.open("picture1.png")  # Ensure this image exists in the directory
        st.image(image, caption="System Boundary for Bio-SAC Production", use_column_width=True)
    except FileNotFoundError:
        st.error("Error: 'picture1.png' not found in the directory.")

    # Table: Energy & Material Inputs
    st.subheader("Energy & Material Inputs")
    lci_data = {
        "Input Category": ["Raw Material", "Raw Material", "Energy", "Energy", "Water"],
        "Item": ["Biomass", "Chemical Catalysts", "Electricity", "Process Heat", "Water Usage"],
        "Quantity per kg Bio-SAC": ["2.5 kg", "0.3 kg", "3.5 MJ", "2.0 MJ", "50 L"],
    }
    df_lci = pd.DataFrame(lci_data)
    st.table(df_lci)

# Section: LCA Results (Merged Raw Data & Visualization)
elif section == "LCA Results":
    st.header("LCA Results")

    # Data Table
    st.subheader("Process-Level LCA Data")
    raw_data = {
        "Process": ["Feedstock Preparation", "Fermentation", "Purification", "Drying & Storage"],
        "GWP (kg CO₂-eq/kg)": [0.24, 0.48, 0.30, 0.18],
        "Energy Demand (MJ/kg)": [1.6, 3.2, 2.0, 1.2],
        "Water Usage (L/kg)": [10, 25, 10, 5],
    }
    df = pd.DataFrame(raw_data)
    st.dataframe(df)

    # GWP Contribution Pie Chart
    st.subheader("Global Warming Potential (GWP) Contribution")
    option_pie = {
        "tooltip": {"trigger": "item", "formatter": "{b}: {c} kg CO₂-eq/kg ({d}%)"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "type": "pie",
                "radius": ["40%", "70%"],
                "data": [
                    {"value": 0.24, "name": "Feedstock Preparation"},
                    {"value": 0.48, "name": "Fermentation"},
                    {"value": 0.30, "name": "Purification"},
                    {"value": 0.18, "name": "Drying & Storage"},
                ],
            }
        ],
    }
    st_echarts(options=option_pie, height="400px")

    # Comparison: Bio-SAC vs Petroleum-SAC
    st.subheader("Comparison: Bio-SAC vs Petroleum-Based SAC")
    comparison_data = {
        "categories": ["GWP (kg CO₂-eq/kg)", "Energy Demand (MJ/kg)", "Water Use (L/kg)"],
        "Bio-SAC": [1.2, 8.0, 50],
        "Petroleum-SAC": [2.5, 12.0, 20],
    }
    option_bar = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {"data": ["Bio-SAC", "Petroleum-SAC"]},
        "xAxis": {"type": "category", "data": comparison_data["categories"]},
        "yAxis": {"type": "value"},
        "series": [
            {"name": "Bio-SAC", "type": "bar", "data": comparison_data["Bio-SAC"], "itemStyle": {"color": "#1995AD"}},
            {"name": "Petroleum-SAC", "type": "bar", "data": comparison_data["Petroleum-SAC"], "itemStyle": {"color": "#C4DFE6"}},
        ],
    }
    st_echarts(options=option_bar, height="400px")

# Section: Key Insights
elif section == "Insights":
    st.header("Key Insights")
    st.markdown("""
    - **GWP Reduction**: The use of Bio-SAC instead of petroleum-based SAC results in more than a **50% reduction** in CO₂ emissions.
    - **Energy Source Optimization**: Increasing the share of renewable energy in fermentation could further reduce the environmental footprint.
    - **Water Consumption**: Bio-SAC production requires **significantly more water**, primarily due to the fermentation process.
    - **Process Efficiency**: The fermentation stage is the **largest contributor** to GWP, highlighting the need for efficiency improvements.
    """)

# Footer
st.markdown("This report follows ISO 14044 guidelines for Life Cycle Assessment (LCA).")
