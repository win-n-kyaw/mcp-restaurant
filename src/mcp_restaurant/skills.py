from mcp_restaurant.config import Config
from crewai import Task, Agent
from mcp_restaurant.tools.sqlite_tool import SQLiteTools
from mcp import StdioServerParameters
from mcp_restaurant.memory import Mem0_Service

server_params = StdioServerParameters(
    command="mcp-server-sqlite", 
    args=["--db-path", '/Users/winnaingkyaw/crew-ai/crewai-mcp/mcp_restaurant/db/restaurant.db']
)
sqlite_tool = SQLiteTools(server_params)

mem0_client = Mem0_Service()

class Skills:
    def __init__(self, agent: Agent):
        self.skills = Config.load_skills()
        self.current_skill = "intent_classifier_skill"
        self.terminate_skill = "response_skill"
        self.agent = agent
    
    def use_skill(self, user_id, **kwargs):
        memory_context = mem0_client.retrieve_memories(user_id, kwargs.get('enquiry', ''))
        description = self.skills[self.current_skill]["task"]["description"].format(**kwargs)
        if memory_context:
            description = description + memory_context
            
        return Task(
            description=description,
            expected_output=self.skills[self.current_skill]["task"]["expected_output"],
            tools=sqlite_tool.get_tools(),
            agent=self.agent
        ).execute_sync().raw
    
    def generate_response(self, **kwargs):
        response = Task(
            description=self.skills[self.terminate_skill]["task"]["description"].format(**kwargs),
            expected_output=self.skills[self.terminate_skill]["task"]["expected_output"],
            tools=sqlite_tool.get_tools(),
            agent=self.agent
        ).execute_sync().raw
        self.current_skill = "intent_classifier_skill"
        return response
    
    def update_skill(self, skill_context: str):
        self.current_skill = skill_context