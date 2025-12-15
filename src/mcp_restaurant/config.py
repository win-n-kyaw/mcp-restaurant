import yaml
import os

class Config:
    @staticmethod
    def load_agents():
        with open('src/mcp_restaurant/config/agents.yaml') as f:
            return yaml.safe_load(f)
    
    @staticmethod
    def load_tasks():
        with open('src/mcp_restaurant/config/tasks.yaml') as f:
            return yaml.safe_load(f)
        
    @staticmethod
    def load_skills():
        with open('src/mcp_restaurant/config/skills.yaml') as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_db_path():
        return os.getenv('DB_PATH', 'db/restaurant.db')