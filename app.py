import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------- Config --------------------
st.set_page_config(layout="wide", page_title="Carbon Footprint Calculator")

# Emission factors (kgCO2 per unit)
EMISSION_FACTORS = {
    "India": {"Transportation": 0.14, "Electricity": 0.82, "Diet": 1.25, "Waste": 0.10},
    "United States": {"Transportation": 0.25, "Electricity": 0.45, "Diet": 2.50, "Waste": 0.20},
    "Germany": {"Transportation": 0.18, "Electricity": 0.38, "Diet": 2.00, "Waste": 0.15},
    "Brazil": {"Transportation": 0.13, "Electricity": 0.10, "Diet": 1.80, "Waste": 0.12},
    "China": {"Transportation": 0.21, "Electricity": 0.65, "Diet": 2.20, "Waste": 0.18},
    "Australia": {"Transportation": 0.24, "Electricity": 0.70, "Diet": 2.10, "Waste": 0.19},
    "Canada": {"Transportation": 0.26, "Electricity": 0.50, "Diet": 2.30, "Waste": 0.16},
    "UK": {"Transportation": 0.19, "Electricity": 0.33, "Diet": 2.00, "Waste": 0.14},
    "France": {"Transportation": 0.17, "Electricity": 0.10, "Diet": 1.90, "Waste": 0.13},
    "Japan": {"Transportation": 0.20, "Electricity": 0.45, "Diet": 2.10, "Waste": 0.15},
}

# CO2 per capita (in tonnes/year)
CO2_AVERAGES = {
    "India": 1.9,
    "United States": 15.0,
    "Germany": 8.4,
    "Brazil": 2.2,
    "China": 7.6,
    "Australia": 16.8,
    "Canada": 14.2,
    "UK": 5.2,
    "France": 4.6,
    "Japan": 8.7,
}

# -------------------- CSS --------------------
st.markdown("""
<style>
body, .main {
    background-color: #121a2a;
    color: #e0e0e0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Fixed Header */
header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
    background-color: #1f2a44;
    color: #00e676;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    font-weight: 700;
    z-index: 9999;
    box-shadow: 0 3px 8px rgba(0,0,0,0.8);
    letter-spacing: 2px;
    padding: 0 20px;
}

/* Left aligned text in header */
header .left-text {
    position: absolute;
    left: 20px;
    font-size: 1rem;
    font-weight: 600;
    color: #00e676cc;
}

/* Top and bottom padding to prevent overlap */
.main > div:first-child {
    padding-top: 80px !important;
    padding-bottom: 100px !important;
}

/* Footer */
footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 40px;
    background-color: #1f2a44;
    color: #00e676;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    font-weight: 500;
    box-shadow: 0 -3px 8px rgba(0,0,0,0.8);
    z-index: 9999;
}
</style>

<header>
  <div class="left-text">CFC by Priyam Parashar</div>
  Carbon Footprint Calculator
</header>
<footer>© Priyam Parashar | 2025</footer>
""", unsafe_allow_html=True)

# -------------------- Main UI --------------------

st.markdown("<h1 style='color:#a5d6a7; text-align:center;'>🌍 Carbon Footprint Calculator</h1>", unsafe_allow_html=True)

# User Inputs
country = st.selectbox("🌎 Select Your Country", list(EMISSION_FACTORS.keys()))

col1, col2 = st.columns(2)
with col1:
    distance = st.slider("🚗 Daily commute (km)", 0.0, 100.0)
    electricity = st.slider("💡 Monthly electricity usage (kWh)", 0.0, 1000.0)

with col2:
    waste = st.slider("🗑️ Weekly waste (kg)", 0.0, 100.0)
    meals = st.number_input("🍽️ Meals per day", 0, 10, value=3)

# Annualize values
distance *= 365
electricity *= 12
waste *= 52
meals *= 365

# Calculate Emissions
factors = EMISSION_FACTORS[country]
emissions = {
    "Transportation": factors["Transportation"] * distance,
    "Electricity": factors["Electricity"] * electricity,
    "Diet": factors["Diet"] * meals,
    "Waste": factors["Waste"] * waste,
}
emissions_tonnes = {k: round(v / 1000, 2) for k, v in emissions.items()}
total_emissions = round(sum(emissions_tonnes.values()), 2)

# Output
if st.button("🧮 Calculate CO2 Emissions"):
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("🔹 Emissions by Category (tonnes/year)")
        for k, v in emissions_tonnes.items():
            st.info(f"{k}: {v} tonnes CO2")
        st.success(f"🌍 Your Total: {total_emissions} tonnes/year")

    with col4:
        st.subheader("📈 Comparison with Country Average")
        avg = CO2_AVERAGES[country]
        if total_emissions > avg:
            st.warning(f"⚠️ You are above the average ({avg} tonnes/year for {country})")
        else:
            st.success(f"✅ You are below the average ({avg} tonnes/year for {country})")
        st.bar_chart(pd.DataFrame(emissions_tonnes.items(), columns=["Category", "Tonnes CO2"]).set_index("Category"))

    # Heatmap
    st.subheader("🌡️ Heatmap of CO2 Per Capita (All Countries)")
    heat_df = pd.DataFrame(list(CO2_AVERAGES.items()), columns=["Country", "Tonnes CO2"])
    heat_df = heat_df.pivot_table(values="Tonnes CO2", index="Country", aggfunc="sum")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(heat_df, annot=True, cmap="YlOrRd", linewidths=.5, fmt=".1f", ax=ax, cbar_kws={"shrink": 0.6})
    plt.yticks(rotation=0)
    st.pyplot(fig)

# -------------------- Chatbot Section --------------------

st.markdown("---")
st.subheader("💬 Ask the Carbon Footprint Chatbot")

qa_pairs = {
    "What is a carbon footprint?": "A carbon footprint is the total greenhouse gas emissions caused by an individual, expressed as CO2 equivalents.",
    "How can I reduce my carbon footprint?": "Use public transport, reduce meat consumption, conserve energy, recycle, and use renewable sources.",
    "Which activity contributes most to emissions?": "Usually transportation and electricity, depending on lifestyle and location.",
    "What are CO2 equivalents?": "They standardize the impact of various greenhouse gases (like methane, nitrous oxide) as equivalent CO2.",
    "Why does diet affect carbon footprint?": "Animal-based diets, especially red meat, have higher emissions than plant-based diets.",
    "What’s the global average CO2 per capita?": "Approximately 4.7 tonnes per person per year (varies by year and source).",
    "Is recycling effective for reducing emissions?": "Yes, it reduces raw material extraction and manufacturing emissions.",
}

question = st.selectbox("Choose a question or type your own:", list(qa_pairs.keys()) + ["Other (type below)"])
custom_question = ""
if question == "Other (type below)":
    custom_question = st.text_input("Type your question:")

if st.button("💬 Ask"):
    if question != "Other (type below)":
        st.info(f"**You asked:** {question}")
        st.success(qa_pairs[question])
    elif custom_question.strip():
        st.info(f"**You asked:** {custom_question}")
        st.warning("This is a basic chatbot. Please select a predefined question for a proper response.")
    else:
        st.error("Please enter a question.")
