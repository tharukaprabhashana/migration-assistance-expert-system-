# ui_streamlit.py
import streamlit as st
from engine import MigrationEngine

st.set_page_config(page_title="Migration Expert System", layout="wide")

# -----------------------------
# Country → Currency mapping
# -----------------------------
COUNTRY_TO_CURRENCY = {
    "Canada": "CAD",
    "Australia": "AUD",
    "New Zealand": "NZD",
    "Singapore": "SGD",
    "Japan": "JPY",
    "United Kingdom": "GBP",
    "United States": "USD",
    "Germany": "EUR",
    "Netherlands": "EUR",
    "France": "EUR",
    "Italy": "EUR",
    "Norway": "NOK",
    "Finland": "EUR",
    "Sweden": "SEK",
    "Denmark": "DKK",
    "Latvia": "EUR",
    "Saudi Arabia": "SAR",
    "United Arab Emirates": "AED"
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🌍 Migration Assistance Expert System")
st.write("This tool uses expert system rules (Experta) to provide migration guidance for 18 countries.")

st.header("👤 Applicant Information")

col1, col2 = st.columns(2)
with col1:
    role = st.selectbox("Role", ["professional", "student", "unemployed"])
    age = st.number_input("Age", min_value=18, max_value=70, value=30)
    education = st.selectbox("Education Level", ["Diploma", "Bachelors", "Masters", "PhD"])
    degree_field = st.text_input("Field of Study", "Computer Science")
    occupation = st.text_input("Occupation", "Software Developer")
    experience_years = st.number_input("Years of Experience", min_value=0, max_value=50, value=3)

with col2:
    preferred_country = st.selectbox("Preferred Country", list(COUNTRY_TO_CURRENCY.keys()))
    current_country = st.text_input("Current Country", "Sri Lanka")
    marital_status = st.selectbox("Marital Status", ["single", "married", "divorced"])
    has_spouse = marital_status == "married"
    spouse_education = st.selectbox(
        "Spouse Education",
        ["None", "Diploma", "Bachelors", "Masters", "PhD"],
        disabled=not has_spouse
    )
    spouse_is_working = st.checkbox("Spouse is employed", disabled=not has_spouse)
    num_children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

# IELTS input (only for English-speaking countries)
ielts = None
if preferred_country in ["Canada", "Australia", "New Zealand", "United Kingdom"]:
    st.markdown("### 🗣️ English Proficiency (IELTS)")
    ielts = st.number_input("IELTS Overall Band Score", min_value=0.0, max_value=9.0, step=0.5, value=7.0)
else:
    st.markdown("### 🗣️ English Proficiency not required for this country")
    ielts = None

# Salary input
st.markdown("### 💰 Financial Details")
salary_currency = COUNTRY_TO_CURRENCY[preferred_country]
salary_local = st.number_input(f"Annual Salary ({salary_currency})", min_value=0, value=30000)

# -----------------------------
# Run the Engine
# -----------------------------
st.divider()
if st.button("🚀 Run Expert System"):
    st.info("Running rules... please wait.")
    engine = MigrationEngine()
    person_data = {
        "role": role,
        "age": age,
        "education": education,
        "degree_field": degree_field,
        "occupation": occupation,
        "experience_years": experience_years,
        "ielts": ielts,
        "salary_local": salary_local,
        "salary_currency": salary_currency,
        "current_country": current_country,
        "preferred_country": preferred_country,
        "marital_status": marital_status,
        "has_spouse": has_spouse,
        "spouse_education": spouse_education if has_spouse else None,
        "spouse_is_working": spouse_is_working if has_spouse else False,
        "num_children": num_children
    }

    results = engine.run_for_person(person_data)

    st.success("✅ Expert System Run Complete!")

    # -----------------------------
    # Results Display
    # -----------------------------
    st.subheader("🎯 Eligibility & Points Summary")
    if results["eligibility"]:
        for e in results["eligibility"]:
            country, visa_type, confidence = e
            st.write(f"- **{country} → {visa_type}** (confidence: {confidence*100:.0f}%)")
    else:
        st.warning("No eligibility facts detected.")

    if results["points"]:
        st.subheader("📊 Points Earned")
        total = sum([p[1] for p in results["points"]])
        st.write(f"**Total Base Points:** {total}")
        for p in results["points"]:
            st.write(f"- {p[0]}: {p[1]} points")

    if results["add_points"]:
        st.subheader("➕ Bonus Points")
        for p in results["add_points"]:
            st.write(f"- {p}")

    st.subheader("📋 Explanations")
    for exp in results["explanations"]:
        st.write(f"- {exp}")

    if results["alternative_suggestions"]:
        st.subheader("🌎 Alternative Country Suggestions")
        st.write(", ".join(results["alternative_suggestions"]))

    if results["recommendations"]:
        st.subheader("💡 Recommendations")
        for r in results["recommendations"]:
            st.write(f"- {r}")
