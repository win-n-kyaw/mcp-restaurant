"""Service for managing CrewAI operations."""
import warnings, re, time
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
        self.max_retries = 3
    
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
            print(llm_config.values())
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
        """
        if not self.initialized:
            raise ValueError("Crew not initialized. Please initialize first.")
        
        inputs = {
            'enquiry': message,
            'user_id': customer_name,
            'customer_name': customer_name
        }
        attempt = 0 
        flow = RestaurantServiceFlow(llm=self.llm)

        while attempt < self.max_retries:
            try:
                result = flow.kickoff(inputs=inputs)

                if hasattr(result, 'raw'):
                    return result.raw
                elif hasattr(result, 'output'):
                    return result.output
                return str(result)

            except Exception as e:
                msg = str(e)

                # Detect 429 RESOURCE_EXHAUSTED
                if "RESOURCE_EXHAUSTED" in msg or "429" in msg:
                    print("❗ Rate limit hit: 429 RESOURCE_EXHAUSTED")

                    match = re.search(r"'retryDelay':\s*'(\d+\.?\d*)s'", msg)
                    if match:
                        delay = float(match.group(1))
                    else:
                        delay = 30  # fallback

                    print(f"⏳ Waiting {delay} seconds before retrying...")
                    time.sleep(delay)

                    attempt += 1
                    continue
                raise e
        raise RuntimeError("Exceeded max retries due to repeated rate limits")
    
    def cleanup(self):
        """Cleanup resources."""
        if self.mcp_adapter:
            try:
                self.mcp_adapter.__exit__(None, None, None)
            except:
                pass
            self.mcp_adapter = None
        self.initialized = False