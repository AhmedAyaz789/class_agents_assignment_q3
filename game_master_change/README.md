# 🧙‍♀️ Game Master Agent - Fantasy Adventure AI

This project is a **text-based fantasy game** powered by AI agents. It allows users to:
- 🎲 Roll dice
- 🧌 Battle monsters
- 🎁 Win rewards
- 🗺️ And enjoy immersive storytelling

All through a fun and interactive terminal experience!  
Built with the **OpenAI Agent SDK**, using function tools and multi-agent handoff logic.

---

## 🔮 Features

- 🎲 **Roll Dice** – Simulate a dice roll with customizable sides
- 🧌 **Monster Encounter** – Fight monsters using tools and random rolls
- 🗺️ **Immersive Narration** – Experience fantasy storylines guided by a narrator agent
- 🎁 **Inventory & Rewards** – Receive magical items or victory bonuses
- 🧠 **Multi-Agent Logic** – Agents collaborate using smart handoffs
- 🛠️ **Tool Integration** – `roll_dice()`, `generate_event()`, etc.

---

## 🧪 How to Run

```bash
uv run main.py
Make sure your .env file includes:

env
Copy
Edit
GEMINI_API_KEY=your_api_key_here
🧠 Agents Involved
Agent Name	Role
GameMasterAgent	Coordinates the full game logic and agent handoffs
NarratorAgent	Tells the story and guides the player
MonsterAgent	Handles monster encounters and combat
ItemAgent	Gives rewards and manages inventory

📁 Folder Structure
bash
Copy
Edit
GameMasterAgent/
│
├── agents/
│   ├── multi_agents.py
│
├── tools/
│   ├── dice_tool.py
│   ├── event_tool.py
│
├── main.py
├── .env
└── README.md
✨ Sample Input
txt
Copy
Edit
I challenge the monster! Roll a 6-sided dice to attack.
Narrate the battle and give me a reward if I win.
✅ Output (Example)
"You rolled a 1! Your attack fails to hit the monster.
The monster retaliates, and you are defeated. Better luck next time!"

👨‍💻 Author
Created with ❤️ by Ayaz Ahmed Laghari