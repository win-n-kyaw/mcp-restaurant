"""Configuration management for the application."""
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class ModelConfig:
    """Model configuration settings."""
    provider: str
    model_name: str
    api_key: str
    base_url: Optional[str] = None

@dataclass
class AppConfig:
    """Application configuration."""
    customer_name: str = "Guest"

class ConfigManager:
    """Manages application configuration."""
    
    @staticmethod
    def get_default_model_config(provider: str) -> dict:
        """Get default configuration for a provider."""
        defaults = {
            "OpenAI": {
                "model_name": os.getenv('OPENAI_MODEL', 'gpt-4'),
                "api_key": os.getenv('OPENAI_API_KEY', ''),
                "base_url": None
            },
            "OpenRouter": {
                "model_name": os.getenv('OPENROUTER_MODEL', 'openrouter/deepseek/deepseek-r1'),
                "api_key": os.getenv('OPENROUTER_API_KEY', ''),
                "base_url": os.getenv('OPENROUTER_API_BASE', 'https://openrouter.ai/api/v1')
            },
            "Google": {
                "model_name": os.getenv('MODEL', 'gemini-2.5-flash'),
                "api_key": os.getenv('GOOGLE_API_KEY', ''),
                "base_url": None
            }
        }
        return defaults.get(provider, defaults["OpenAI"])