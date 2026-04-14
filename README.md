# AI Travel Planner

AI Travel Planner is a Streamlit application that uses a multi-agent workflow to generate personalized trip plans from a simple natural-language prompt. The app asks for your destination preferences, validates that the request is actually travel-related, then coordinates a small team of agents to produce a destination summary, day-by-day itinerary, budget estimate, and a final polished travel plan.

## Links

- [Clone the Repository](https://github.com/vipulgupta18/ai-travel-planner.git)
- [Running the Application](https://ai-travel-planner-vipul.streamlit.app/)

## Project Overview

The app is built around a focused group-chat architecture powered by AutoGen:

- `User_Proxy_Agent` receives the user request and hands it into the workflow.
- `Destination_Expert_Agent` creates a destination snapshot based on the trip goals.
- `Itinerary_Creator_Agent` turns that snapshot into a day-by-day plan.
- `Budget_Analyst_Agent` estimates likely costs and suggests savings ideas.
- `Report_Writer_Agent` combines everything into a final user-friendly result.

The interface is intentionally simple: users type a travel prompt, submit it, and the app returns a structured plan. If the request is not travel-related, the app blocks it and asks for a valid travel prompt instead.

## Features

- Personalized travel planning from a single prompt.
- Multi-agent orchestration for destination research, itinerary design, and budgeting.
- Travel-only input validation to reduce irrelevant requests.
- Final plan display plus expandable conversation history.
- Supports local development with `.env` or deployment with Streamlit secrets.
- Hosted Streamlit deployment available through the browser link above.

## How It Works

1. The user enters a travel request such as destination, duration, budget, and interests.
2. The app checks whether the text contains travel-related keywords.
3. If the prompt is valid, the user proxy agent starts a controlled AutoGen group chat.
4. Each agent contributes one stage of the trip-planning pipeline.
5. The final response is shown in the Streamlit UI along with the message history.

## Tech Stack

- Python
- Streamlit
- AutoGen
- Groq API
- OpenAI-compatible client configuration through AutoGen
- python-dotenv

## Prerequisites

- Python 3.10 or newer
- A Groq API key
- `pip` for dependency installation

## Installation

### Clone the Repository

```bash
git clone https://github.com/vipulgupta18/ai-travel-planner.git
cd ai-travel-planner
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Set your Groq API key in one of the following ways:

### Option 1: Local `.env` file

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Option 2: Streamlit Secrets

For deployment, add the key to Streamlit secrets:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

## Running the Application

### Local Development

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

### Browser Demo

You can also run the deployed version here:

https://ai-travel-planner-vipul.streamlit.app/

## Example Usage

Try a prompt like this:

> Plan a 5-day trip to Goa with a low budget and focus on beaches. Keep it short.

The app will generate a destination snapshot, a sample itinerary, budget guidance, and a summarized travel plan.

## Screenshots

### Main input screen

![AI Travel Planner input screen](output/Screenshot%202026-04-14%20014432.png)

### Generated travel plan

![AI Travel Planner generated itinerary](output/Screenshot%202026-04-14%20014455.png)

### Travel-only validation example

![AI Travel Planner validation message](output/Screenshot%202026-04-14%20014634.png)

## Repository Structure

```text
app.py        # Streamlit application and agent workflow
requirements.txt
README.md
output/       # Screenshots used in the documentation
```

## Notes

- The app expects `GROQ_API_KEY` to be available before it can generate plans.
- The final answer is produced by the last agent in the group chat, and the UI stores the full chat history in session state.
- The travel keyword filter is a simple guardrail, so travel prompts should be clear and specific for best results.

## License

No license file is currently included in the repository.
