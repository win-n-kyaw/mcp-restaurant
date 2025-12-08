from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

class SQLiteTools:
    def __init__(self, server_params: StdioServerParameters):
        self.mcp_server_adapter = MCPServerAdapter(serverparams=server_params)

    def get_tools(self):
        return self.mcp_server_adapter.tools
    
    def get_tool_names(self):
        return [ tool.name for tool in self.mcp_server_adapter.tools ]

    def terminate_adapter(self):
        self.mcp_server_adapter.stop()
    