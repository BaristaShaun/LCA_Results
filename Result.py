import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from PIL import Image

# Title
st.title("LCA Report: Bio-SAC Production")

# Tabs for Navigation
tab1, tab2, tab3, tab4 = st.tabs(["Project Overview", "Raw Data", "Visualizations", "Insights"])

# Tab 1: Project Overview
with tab1:
    st.header("Project Overview")
    with st.expander("ISO Standards"):
        st.write("ISO 14044: The system boundary follows ISO 14044 standards for conducting an LCA.")

    with st.expander("System Boundary"):
        st.write("Cradle-to-Gate: From raw material extraction to drying and storage, excluding downstream processes.")
        st.subheader("System Boundary")
        try:
            image = Image.open("picture1.png")  # Ensure this image exists in the directory
            st.image(image, caption="System Boundary for Bio-SAC Production", use_column_width=True)
        except FileNotFoundError:
            st.error("Error: 'picture1.png' not found in the directory.")

    with st.expander("Functional Unit"):
        st.write("1 kg of Bio-SAC produced. The functional unit ensures consistent comparisons.")

    with st.expander("Allocation Method"):
        st.write("Co-product Allocation: Environmental burden is allocated proportionally based on economic value.")

    with st.expander("Impact Categories"):
        st.write("""
        EF3.1 impact categories were used.
        - Global Warming Potential (GWP) (kg CO₂-eq)
        - Cumulative Energy Demand (CED) (MJ)
        - Water Use (L)
        """)

# Tab 2: Raw Data Table
with tab2:
    st.header("Raw Data: LCA Results")
    raw_data = {
        "Process": ["Feedstock Preparation", "Fermentation", "Purification", "Drying & Storage"],
        "GWP Contribution (kg CO₂-eq/kg)": [0.24, 0.48, 0.30, 0.18],
        "Energy Demand (MJ/kg)": [1.6, 3.2, 2.0, 1.2],
        "Water Usage (L/kg)": [10, 25, 10, 5],
    }
    df = pd.DataFrame(raw_data)
    st.dataframe(df)

# Tab 3: Visualizations
with tab3:
    st.header("LCA results")
    # Contribution Analysis with ECharts
    st.subheader("Global Warming Potential (GWP) Contribution")
    option_pie = {
        "tooltip": {"trigger": "item", "formatter": "{b}: {c} kg CO₂-eq/kg ({d}%)"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "GWP Contribution",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {"borderRadius": 10, "borderColor": "#fff", "borderWidth": 2},
                "label": {"show": False, "position": "center"},
                "emphasis": {"label": {"show": True, "fontSize": "16", "fontWeight": "bold"}},
                "labelLine": {"show": False},
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

    # Bar Chart: Comparison of Bio-SAC vs Petroleum-SAC
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
            {
                "name": "Bio-SAC",
                "type": "bar",
                "data": comparison_data["Bio-SAC"],
                "itemStyle": {"color": "#1995AD"},
            },
            {
                "name": "Petroleum-SAC",
                "type": "bar",
                "data": comparison_data["Petroleum-SAC"],
                "itemStyle": {"color": "#C4DFE6"},
            },
        ],
    }
    st_echarts(options=option_bar, height="400px")
with tab4:
    st.header("Key Insights")
    st.markdown("""
    - **GWP Reduction**: Using Bio-SAC instead of petroleum-based SAC can cut CO₂ emissions by over 50%.
    - **Energy Source Optimization**: A higher reliance on renewable energy for heat and electricity could reduce GWP further.
    - **Water Use**: Water use is higher for Bio-SAC due to the fermentation process.
    - **Process Contribution**: Fermentation is the largest contributor to GWP, highlighting the need for more energy-efficient microbial processes.
    """)

# Footer
st.markdown("This report was written following the guidelines of ISO 14044 ")
