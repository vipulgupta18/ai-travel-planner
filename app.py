import os
import streamlit as st
from dotenv import load_dotenv
from autogen import ConversableAgent, GroupChat, GroupChatManager

# Load environment variables for local development
load_dotenv()

# --- Configuration ---
# Access GROQ_API_KEY from Streamlit secrets or .env
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except (st.errors.StreamlitSecretNotFoundError, KeyError):
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("GROQ_API_KEY not found. Please set it in Streamlit secrets for deployment or in your .env file for local development.")
        st.stop()

llm_config = {
    "config_list": [
        {
            "model": "openai/gpt-oss-20b",
            "api_key": groq_api_key,
            "base_url": "https://api.groq.com/openai/v1",
            "price": [0.2, 0.2],
        }
    ]
}

# --- Agent Definitions ---
user_proxy = ConversableAgent(
    name="User_Proxy_Agent",
    system_message="You are a user proxy agent. Relay the user's travel request to the Destination Expert and present the final plan from the Report Writer.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

destination_expert = ConversableAgent(
    name="Destination_Expert_Agent",
    system_message="You are the Destination Expert. Provide detailed travel destination info based on user preferences (climate, attractions, culture). Pass to Itinerary Creator.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

itinerary_creator = ConversableAgent(
    name="Itinerary_Creator_Agent",
    system_message="You are the Itinerary Creator. Design a day-by-day travel plan with activities, accommodations, and transportation based on the destination and preferences. Pass to Budget Analyst.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

budget_analyst = ConversableAgent(
    name="Budget_Analyst_Agent",
    system_message="You are the Budget Analyst. Estimate costs for the itinerary (flights, accommodations, activities, food) and suggest savings tips. Pass to Report Writer.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

report_writer = ConversableAgent(
    name="Report_Writer_Agent",
    system_message="You are the Report Writer. Compile a comprehensive, user-friendly travel plan from the Destination Expert, Itinerary Creator, and Budget Analyst. Deliver the final plan and terminate the conversation.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# --- Define Allowed Transitions Between Agents ---
allowed_transitions = {
    user_proxy: [destination_expert],
    destination_expert: [itinerary_creator],
    itinerary_creator: [budget_analyst],
    budget_analyst: [report_writer],
    report_writer: [],  # Terminate after report
}

# --- Set up the GroupChat ---
group_chat = GroupChat(
    agents=[user_proxy, destination_expert, itinerary_creator, budget_analyst, report_writer],
    allowed_or_disallowed_speaker_transitions=allowed_transitions,
    speaker_transitions_type="allowed",
    messages=[],
    max_round=5,  # One pass: user_proxy → destination → itinerary → budget → report
)

# --- Create the GroupChatManager ---
travel_planner_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

# --- Function to Check if Query is Travel-Related ---
def is_travel_related(query):
    travel_keywords = [
        "trip", "travel", "destination", "itinerary", "vacation", "holiday", "tour",
        "beach", "culture", "adventure", "city", "country", "flight", "hotel",
        "accommodation", "budget", "plan", "visit", "explore", "sightseeing"
    ]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in travel_keywords)

# --- Streamlit App ---
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

def main():
    st.title("✈️ AI Travel Planner")
    st.markdown("Plan your dream trip! Enter your travel preferences, and we'll create a personalized travel plan.")

    # Initialize session state
    if "chat_result" not in st.session_state:
        st.session_state.chat_result = None
        st.session_state.history = []

    # Input form
    with st.form(key="travel_form"):
        user_request = st.text_area(
            "Your travel preferences (e.g., 'Plan a 7-day trip to Kyoto for two, focusing on culture and food, with a moderate budget.')",
            height=150
        )
        submit_button = st.form_submit_button(label="Generate Travel Plan")

    if submit_button and user_request:
        # Validate if the query is travel-related
        if not is_travel_related(user_request):
            st.error("This is a traveling agent, sorry for your inconvenience. Please provide a travel-related request.")
            return

        with st.spinner("Generating your travel plan..."):
            try:
                # Clear previous result
                st.session_state.chat_result = None
                st.session_state.history = []

                # Initiate chat
                chat_result = user_proxy.initiate_chat(
                    travel_planner_manager,
                    message=user_request,
                    clear_history=True,
                )

                # Store result and history
                st.session_state.chat_result = chat_result
                st.session_state.history = chat_result.chat_history

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.markdown("Please ensure your `GROQ_API_KEY` is correctly set in Streamlit secrets or .env file and try again.")

    # Display results if available
    if st.session_state.chat_result and st.session_state.history:
        st.subheader("Your Personalized Travel Plan")
        if st.session_state.history:
            st.markdown(st.session_state.history[-1]["content"])
        else:
            st.warning("No final travel plan content available.")

        with st.expander("View Conversation History"):
            if st.session_state.history:
                for message in st.session_state.history:
                    st.markdown(f"**{message.get('name', 'Unknown Agent')}**: {message.get('content', '(No content)')}")
            else:
                st.info("No conversation history to display.")

if __name__ == "__main__":
    main()
