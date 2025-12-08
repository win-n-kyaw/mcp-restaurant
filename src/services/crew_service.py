"""Service for managing CrewAI operations."""
import warnings
from typing import List, Dict, Any
from crewai import LLM
from mcp import StdioServerParameters
from crewai_tools import MCPServerAdapter
from mcp_restaurant.quorem import RestaurantServiceFlow, RestaurantServiceState

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

class CrewService:
    """Service for managing CrewAI crew operations."""
    
    def __init__(self):
        self.llm = None
        self.tools = None
        self.mcp_adapter = None
        self.initialized = False
    
    def initialize(self, model_config: Dict[str, Any], db_path: str) -> tuple[bool, str, List[str]]:
        """
        Initialize the crew with given configuration.
        
        Returns:
            Tuple of (success, message, tool_names)
        """
        try:
            # Close existing adapter if any
            self.cleanup()
            
            # Create LLM instance
            llm_config = {
                "model": model_config["model_name"],
                "api_key": model_config["api_key"]
            }
            if model_config.get("base_url"):
                llm_config["base_url"] = model_config["base_url"]
            
            self.llm = LLM(**llm_config)
            
            # Create server parameters
            server_params = StdioServerParameters(
                command="mcp-server-sqlite",
                args=["--db-path", db_path]
            )
            
            # Initialize MCP adapter
            self.mcp_adapter = MCPServerAdapter(server_params)
            self.mcp_adapter.__enter__()
            self.tools = self.mcp_adapter.tools
            
            self.initialized = True
            tool_names = [tool.name for tool in self.tools]
            
            return True, "Crew initialized successfully!", tool_names
            
        except Exception as e:
            self.initialized = False
            return False, f"Error initializing crew: {str(e)}", []
    
    def process_message(self, message: str, customer_name: str) -> str:
        """
        Process a customer message through the crew.
        
        Args:
            message: Customer's message
            customer_name: Customer's name
            
        Returns:
            Crew's response
        """
        if not self.initialized:
            raise ValueError("Crew not initialized. Please initialize first.")
        
        inputs = {
            'enquiry': message,
            'user_id': customer_name,
            'customer_name': customer_name
        }
        
        flow = RestaurantServiceFlow()
        result = flow.kickoff(inputs=inputs)

        # Extract response
        if hasattr(result, 'raw'):
            return result.raw
        elif hasattr(result, 'output'):
            return result.output #type: ignore
        else:
            return str(result)
    
    def cleanup(self):
        """Cleanup resources."""
        if self.mcp_adapter:
            try:
                self.mcp_adapter.__exit__(None, None, None)
            except:
                pass
            self.mcp_adapter = None
        self.initialized = False