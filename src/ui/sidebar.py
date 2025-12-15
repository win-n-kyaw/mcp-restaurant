"""Sidebar UI component."""
import streamlit as st
from typing import Dict, Any

class Sidebar:
    """Manages the sidebar UI."""
    
    @staticmethod
    def render(config_manager) -> Dict[str, Any]:
        """
        Render the sidebar and return configuration.
        
        Returns:
            Dictionary containing all configuration values
        """
        with st.sidebar:
            st.title("⚙️ Configuration")
            
            # Model Settings
            st.header("Model Settings")
            model_provider = st.selectbox(
                "Model Provider",
                ["OpenAI", "OpenRouter", "Google"],
                help="Select your LLM provider"
            )
            
            defaults = config_manager.get_default_model_config(model_provider)
            
            model_name = st.text_input(
                "Model Name",
                value=defaults["model_name"],
                help=f"{model_provider} model name"
            )
            
            api_key = st.text_input(
                "API Key",
                value=defaults["api_key"],
                type="password",
                help=f"Your {model_provider} API key"
            )
            
            base_url = None
            if model_provider == "OpenRouter":
                base_url = st.text_input(
                    "Base URL",
                    value=defaults["base_url"],
                    help="OpenRouter API base URL"
                )
            
            st.divider()
            
            # Customer Info
            st.header("Customer Info")
            customer_name = st.text_input(
                "Customer Name",
                value="Guest",
                help="Name for personalized responses"
            )
            
            st.divider()
            
            return {
                "model_provider": model_provider,
                "model_name": model_name,
                "api_key": api_key,
                "base_url": base_url,
                "customer_name": customer_name
            }
    
    @staticmethod
    def render_actions() -> Dict[str, bool]:
        """
        Render action buttons.
        
        Returns:
            Dictionary with button states
        """
        with st.sidebar:
            initialize_clicked = st.button(
                "🔄 Initialize/Reset Crew",
                use_container_width=True
            )
            
            clear_chat_clicked = st.button(
                "🗑️ Clear Chat History",
                use_container_width=True
            )
            
            return {
                "initialize": initialize_clicked,
                "clear_chat": clear_chat_clicked
            }
    
    @staticmethod
    def render_status(initialized: bool): #type: ignore
        """Render status information."""
        with st.sidebar:
            st.divider()
            if initialized:
                st.success("✅ Crew Status: Active")
            else:
                st.warning("⚠️ Crew Status: Not Initialized")
