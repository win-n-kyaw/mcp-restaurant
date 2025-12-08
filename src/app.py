"""Main application entry point."""
import streamlit as st
import atexit
from config.settings import ConfigManager
from services.crew_service import CrewService
from ui.sidebar import Sidebar
from ui.chat import ChatUI

# Page configuration
st.set_page_config(
    page_title="Restaurant AI Assistant",
    page_icon="🍽️",
    layout="wide"
)

# Initialize components
config_manager = ConfigManager()
chat_ui = ChatUI()
sidebar = Sidebar()

# Initialize session state
chat_ui.initialize_session_state()

if 'crew_service' not in st.session_state:
    st.session_state.crew_service = CrewService()

# Render sidebar
config = sidebar.render(config_manager)
actions = sidebar.render_actions()
sidebar.render_status(
    st.session_state.crew_initialized,
    st.session_state.tool_names
)

# Handle actions
if actions["initialize"]:
    model_config = {
        "model_name": config["model_name"],
        "api_key": config["api_key"],
        "base_url": config["base_url"]
    }
    
    with st.spinner("Initializing crew..."):
        success, message, tool_names = st.session_state.crew_service.initialize(
            model_config,
            config["db_path"]
        )
        
        st.session_state.crew_initialized = success
        st.session_state.tool_names = tool_names
        st.session_state.customer_name = config["customer_name"]
        
        if success:
            st.success(f"✅ {message}")
        else:
            st.error(f"❌ {message}")

if actions["clear_chat"]:
    chat_ui.clear_messages()
    st.rerun()

# Render main chat interface
chat_ui.render_header()

if not st.session_state.crew_initialized:
    chat_ui.render_initialization_message()

# Display chat messages
chat_ui.render_messages(st.session_state.messages)

# Handle user input
if prompt := chat_ui.get_user_input(
    disabled=not st.session_state.crew_initialized
):
    # Add user message
    chat_ui.add_message("user", prompt)
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.crew_service.process_message(
                    prompt,
                    st.session_state.customer_name
                )
                
                st.markdown(response)
                chat_ui.add_message("assistant", response)
                
            except Exception as e:
                error_msg = f"❌ Error processing request: {str(e)}"
                st.error(error_msg)
                chat_ui.add_message("assistant", error_msg)

# Render footer
chat_ui.render_footer()

# Cleanup on app termination
def cleanup():
    if 'crew_service' in st.session_state:
        st.session_state.crew_service.cleanup()

atexit.register(cleanup)