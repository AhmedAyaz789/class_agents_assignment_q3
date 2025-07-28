
import random
from agents import function_tool

@function_tool
def roll_dice(sides: int = 6) -> str:
    result = random.randint(1, sides)
    return f"You rolled a {result} on a {sides}-sided dice!"

@function_tool
def generate_event(choice: str) -> str:
    events = {
        "forest": "🌲 You encounter a wild beast in the forest!",
        "cave": "🪙 You discover a hidden treasure chest in the cave!",
        "village": "👴 A mysterious old man shares a secret with you.",
    }
    return events.get(choice.lower(), "🤷 Nothing happens...")
