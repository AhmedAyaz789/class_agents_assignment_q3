
from agents import Agent
from tools import roll_dice, generate_event

narrator_agent = Agent(
    name="NarratorAgent",
    instructions="You guide the player through the story and offer choices.",
    tools=[generate_event]
)

monster_agent = Agent(
    name="MonsterAgent",
    instructions="You simulate combat using the roll dice tool.",
    tools=[roll_dice]
)

item_agent = Agent(
    name="ItemAgent",
    instructions="You handle inventory and give rewards after successful events."
)

main_agent = Agent(
    name="GameMasterAgent",
    instructions="You are the main game master. Coordinate game flow using other agents.",
    handoffs=[narrator_agent, monster_agent, item_agent]
)
