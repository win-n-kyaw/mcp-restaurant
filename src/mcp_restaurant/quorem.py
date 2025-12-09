from typing import Any
from crewai.flow.persistence.base import FlowPersistence
from mcp_restaurant.tools.sqlite_tool import SQLiteTools
from crewai.flow.flow import Flow, listen, start
# from crewai.utilities import RPMController
from mcp_restaurant.agent_factory import create_agent_task
from mcp_restaurant.memory import Mem0_Service
from mcp import StdioServerParameters
from pydantic import BaseModel

## Memory
mem0_client = Mem0_Service()

## MCP tools
server_params = StdioServerParameters(
    command="mcp-server-sqlite", 
    args=["--db-path", '/Users/winnaingkyaw/crew-ai/crewai-mcp/mcp_restaurant/db/restaurant.db']
)
sqlite_tool = SQLiteTools(server_params)
tools = sqlite_tool.get_tools()

def _resolve_specialist(intent: str, mapping: dict) -> str:
    for intent_key, specialist_key in mapping.items():
        if intent_key in intent:
            return specialist_key
    return 'menu_expert'

# Flow Model
class RestaurantServiceState(BaseModel):
    enquiry: str = ""
    customer_name: str = ""
    user_id: str = ""  
    intent: str = ""
    specialist_response: str = ""
    final_response: str = ""

class RestaurantServiceFlow(Flow[RestaurantServiceState]):
    def __init__(self, llm=None, persistence: FlowPersistence | None = None, tracing: bool | None = None, **kwargs: Any) -> None:
        super().__init__(persistence, tracing, **kwargs)
        self.llm = llm  # Store the LLM instance

    @start()
    def classify_intent(self):
        print("\n[Flow] Classifying intent...")
        # if self.rpm_controller.check_or_wait():
        intent = create_agent_task(
            'intent_classifier',
            llm=self.llm,
            mem0_client=mem0_client,
            tools=None,
            enquiry=self.state.enquiry,
            user_id=self.state.user_id
        )
        self.state.intent = intent
        print(f"[Flow] Detected intent: {intent}")

    @listen(classify_intent)
    def route_to_specialist(self):
        intent_mapping = {
            'MENU_INQUIRY': 'menu_expert',
            'PLACE_ORDER': 'order_manager',
            'CHECK_ORDER': 'order_tracker',
            'MAKE_RESERVATION': 'reservation_specialist',
        }

        specialist_key = _resolve_specialist(self.state.intent, intent_mapping)
        # if self.rpm_controller.check_or_wait():
        try:
            response = create_agent_task(
                specialist_key,
                llm=self.llm, 
                tools=tools,
                mem0_client=mem0_client,
                enquiry=self.state.enquiry, 
                customer_name=self.state.customer_name,
                user_id=self.state.user_id
            )
            self.state.specialist_response = response
        
        except Exception as e:
            print(f"Error with specialist '{specialist_key}': {str(e)}")
            self.state.specialist_response = (
                "I apologize, but I encountered an issue processing your request."
            )
    
    @listen(route_to_specialist)
    def coordinate_response(self):
        print("\n[Flow] Coordinating final response...")
        # if self.rpm_controller.check_or_wait():
        final_response = create_agent_task(
            'response_coordinator',
            tools=None,
            llm=self.llm,
            mem0_client=mem0_client,
            enquiry=self.state.enquiry,
            specialist_response=self.state.specialist_response,
            customer_name=self.state.customer_name,
            user_id=self.state.user_id
        )
        self.state.final_response = final_response
        
        # Store the conversation in Mem0 after generating response
        mem0_client.store_conversation(
            user_id=self.state.user_id,
            user_message=self.state.enquiry,
            assistant_message=final_response
        )
        print("[Flow] Final response ready and stored in memory")
        return final_response