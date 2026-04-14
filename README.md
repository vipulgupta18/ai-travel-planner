# ✈️ AI Travel Planner (Agentic Chat using AutoGen & Groq)

This project is a **multi-agent AI travel planner** built using **AutoGen**, **Groq LLM API**, and **Streamlit**.  
It simulates a collaborative team of AI travel agents (**Destination Expert**, **Itinerary Creator**, **Budget Analyst**, and **Report Writer**) to generate **personalized travel plans**.

---

## 🚀 Features

- ✅ Multi-agent conversation flow using **AutoGen GroupChat**
- ✅ Real-time AI-powered travel planning via **Streamlit**
- ✅ Budget, itinerary, and destination insights in a single output
- ✅ **Groq Llama-3-8b-8192** model integration
- ✅ Safe input handling (only travel-related queries allowed)

---

## 📂 Project Structure

📁 travel_plannr/
│
├── .env # Local environment variables (GROQ_API_KEY)
├── .gitignore
├── README.md
├── requirements.txt
└── app.py # Main Streamlit application


---

⚙️ Setup Instructions

1. Clone the Repository
git clone https://github.com/harshitg433/travel_plannr.git
cd travel_plannr

2. Create Virtual Environment (Optional but Recommended)
python3 -m venv .venv
source .venv/bin/activate

3. Install Required Packages

pip install -r requirements.txt

4. Configure API Key(Using .env)
Create a .env file in your project root:

GROQ_API_KEY=your_groq_api_key_here

▶️ Running the Application

streamlit run app.py

Then open your browser: http://localhost:8501

📝 Usage
Enter your travel preferences (destination, duration, budget, etc.).

The AI agents will discuss internally and generate:

✨ Destination highlights

📅 Itinerary breakdown

💰 Budget estimation

📝 Final compiled travel plan

Only valid travel-related requests are processed.

✅ Example Prompt
Plan a 5-day trip to Goa for a couple, focusing on beaches and relaxation, with a luxury budget.
🖥️ Tech Stack
Python 🐍

AutoGen (Multi-Agent AI Framework)

Groq API (Llama3 8B Model)

Streamlit (UI)

dotenv (Secret Management)

💡 Notes
📝 Groq Pricing Warning: This project includes "price": [0.2, 0.2] in llm_config to avoid AutoGen cost calculation warnings.

🚧 Limited to Travel Use-Case: Non-travel queries are blocked.

🏆 Future Scope Ideas
✅ Multi-city trip support

✅ Export travel plan as PDF

✅ Integration with Google Maps / Flights APIs

🤝 Contributing
Pull requests are welcome! Please open issues for bugs or feature suggestions.


🖼️ Project banner image

![Alt Text](https://github.com/harshitg433/travel_plannr/blob/master/output/Screenshot%20from%202025-07-22%2023-37-33.png)

![Alt Text](https://github.com/harshitg433/travel_plannr/blob/master/output/Screenshot%20from%202025-07-22%2023-37-51.png)

