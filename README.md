# 🌍 Migration Assistance Expert System

An intelligent expert system that provides personalized migration guidance for 18+ countries using rule-based reasoning powered by Experta.

## 🌟 Features

- **Multi-Country Support**: Comprehensive migration rules for 18 countries across multiple continents
- **Expert System Engine**: Built with Experta (Python expert system library)
- **Interactive UI**: User-friendly Streamlit web interface
- **Intelligent Recommendations**: Visa eligibility assessment, points calculation, and alternative suggestions
- **Extensible Architecture**: Easy to add new countries and migration rules

## 🌍 Supported Countries

- **North America**: Canada, United States
- **Europe**: United Kingdom, Germany, France, Netherlands, Italy, Norway, Finland, Sweden, Denmark, Latvia
- **Asia-Pacific**: Australia, New Zealand, Singapore, Japan
- **Middle East**: Saudi Arabia, United Arab Emirates

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/tharukaprabhashana/migration-assistance-expert-system-.git
cd migration-assistance-expert-system-
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install streamlit experta
```

## 💻 Usage

1. **Start the Streamlit application**
```bash
streamlit run ui_streamlit.py
```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Fill in your details**:
   - Personal information (age, education, occupation)
   - Work experience
   - Language proficiency (IELTS for English-speaking countries)
   - Financial details
   - Family information

4. **Click "Run Expert System"** to get:
   - Visa eligibility assessment
   - Points breakdown
   - Recommendations
   - Alternative country suggestions

## 📁 Project Structure

```
.
├── engine.py                    # Core expert system engine
├── ui_streamlit.py             # Streamlit web interface
├── ontology.json               # Knowledge base ontology
├── static_kb.json              # Static knowledge base
├── rules/                      # Country-specific migration rules
│   ├── __init__.py
│   ├── base_rules.py
│   ├── country_specs.json
│   ├── australia_rules.py
│   ├── canada_rules.py
│   ├── denmark_rules.py
│   ├── finland_rules.py
│   ├── france_rules.py
│   ├── germany_rules.py
│   ├── italy_rules.py
│   ├── japan_rules.py
│   ├── latvia_rules.py
│   ├── netherlands_rules.py
│   ├── new_zealand_rules.py
│   ├── norway_rules.py
│   ├── saudi_arabia_rules.py
│   ├── singapore_rules.py
│   ├── sweden_rules.py
│   ├── united_arab_emirates_rules.py
│   ├── united_kingdom_rules.py
│   └── united_states_rules.py
└── tools/                      # Utility scripts
    └── generate_country_rules.py
```

## 🔧 How It Works

1. **Rule-Based Reasoning**: Uses Experta to implement forward-chaining inference
2. **Fact Declaration**: User input is converted into facts
3. **Rule Matching**: Country-specific rules are matched against declared facts
4. **Inference**: System derives eligibility, calculates points, and generates recommendations
5. **Results**: Comprehensive migration guidance is presented to the user

## 🛠️ Adding New Countries

1. Create a new rule file in `rules/` directory (e.g., `spain_rules.py`)
2. Define country-specific rules extending `BaseRules`
3. Add country specifications to `rules/country_specs.json`
4. Update the country list in `ui_streamlit.py`

## 📦 Dependencies

- **streamlit**: Web application framework
- **experta**: Python expert system library (forward-chaining rule-based system)

## 🐛 Known Issues

- **Python 3.10+ compatibility**: The project includes a compatibility shim for `collections.Mapping` deprecation in `rules/__init__.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👥 Authors

- **Tharuka Prabhashana** - Initial work - [@tharukaprabhashana](https://github.com/tharukaprabhashana)

## 🙏 Acknowledgments

- Built with [Experta](https://github.com/nilp0/experta) expert system library
- UI powered by [Streamlit](https://streamlit.io/)
- Migration rules based on official immigration policies of respective countries
