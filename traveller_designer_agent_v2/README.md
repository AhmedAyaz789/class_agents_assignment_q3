🧭 AI Travel Designer Agent
This project is a smart, AI-powered travel planning system built using the OpenAI Agent SDK.
It coordinates multiple specialized agents to create a complete, personalized travel experience for users — based on their mood, interests, and preferences.

✨ What It Does
The system runs in the command-line and simulates a full trip plan. It can:

🌍 Recommend travel destinations based on mood or interests
🛫 Suggest flights and 🏨 hotels using mock data tools
📍 Recommend places to visit, 🎭 activities, and 🍽️ local food options
🧠 Use intelligent multi-agent handoff to coordinate the travel journey

🛠️ Technologies Used
🧠 OpenAI Agent SDK (via openai-agents)
⚙️ Python (async logic for multi-agent control)
🗂️ .env file to securely manage API keys (like Gemini or OpenAI)
🧪 Custom Tools: find_flight(), find_hotel(), suggest_activity(), etc.

uv run main.py

Agent Name	Responsibility
DestinationAgent	Finds suitable travel destinations
BookingAgent	Simulates flight/hotel booking
ExploreAgent	Suggests attractions and local food
All agents are coordinated using handoffs.

#run this with command uv run main.py