from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from dotenv import load_dotenv

# Load your API keys from the .env file
load_dotenv()

# 1. Define the State Structure
class PongState(TypedDict):
    # 'add_messages' ensures every agent's chat history is appended, not overwritten
    messages: Annotated[list[BaseMessage], add_messages]
    
    # The step-by-step roadmap created by the Planner
    plan: str
    
    # The HTML/JS written by the Worker so far
    current_code: str
    
    # The current step the Worker is actively trying to code
    current_step: str
    
    # Your feedback when the system pauses for Human-in-the-Loop
    human_feedback: str

# 2. Initialize the Graph
workflow = StateGraph(PongState)

print("State defined and graph initialized successfully!")
