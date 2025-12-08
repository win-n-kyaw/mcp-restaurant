"""Chat UI component."""
import streamlit as st
from typing import List, Dict

class ChatUI:
    """Manages the chat interface."""
    
    @staticmethod
    def initialize_session_state():
        """Initialize session state variables."""
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        if 'crew_initialized' not in st.session_state:
            st.session_state.crew_initialized = False
        if 'tool_names' not in st.session_state:
            st.session_state.tool_names = []
    
    @staticmethod
    def render_header():
        """Render chat header."""
        st.title("🍽️ Restaurant AI Assistant")
        st.markdown(
            "Chat with our AI-powered restaurant assistant for menu inquiries, "
            "orders, reservations, and more!"
        )
    
    @staticmethod
    def render_initialization_message():
        """Render message when crew is not initialized."""
        st.info(
            "👈 Please configure and initialize the crew in the sidebar "
            "to start chatting."
        )
    
    @staticmethod
    def render_messages(messages: List[Dict[str, str]]):
        """Render chat messages."""
        for message in messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    @staticmethod
    def get_user_input(disabled: bool = False) -> str:
        """Get user input from chat."""
        return st.chat_input(
            "Ask about our menu, place an order, make a reservation...",
            disabled=disabled
        ) #type: ignore
    
    @staticmethod
    def add_message(role: str, content: str):
        """Add a message to chat history."""
        st.session_state.messages.append({
            "role": role,
            "content": content
        })
    
    @staticmethod
    def clear_messages():
        """Clear all messages."""
        st.session_state.messages = []
    
    @staticmethod
    def render_footer():
        """Render footer."""
        st.divider()
        st.markdown(
            """
            <div style='text-align: center; color: gray; font-size: 0.8em;'>
            Powered by CrewAI with MCP Tools | Built with Streamlit
            </div>
            """,
            unsafe_allow_html=True
        )