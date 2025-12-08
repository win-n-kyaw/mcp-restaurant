# MCP Restaurant

Welcome to the MCP Restaurant project, powered by [crewAI](https://crewai.com). This project features multi-agentic architecture with business data store in mysqlite database. The agents are enquipped with sqlite mcp tool for querying, adding, and generate insights from exisiting tables.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:
(Optional) Lock the dependencies and install them by using the CLI command:

```bash
uv sync
```

Use the virtual environment

```bash
source .venv/bin/activate
```

### Directory Structure

```bash
.
├── README.md                                  #This File
├── db                                         #Db Schemas and filebased sqlite3 db
│   ├── restaurant.db                               # Db file
│   ├── schema.sql                                  # Database Schemas
│   └── seed.sql                                    # Seed data
├── knowledge                                  #Knowledge base (Not Used)
│   └── user_preference.txt                         # Optional knowledge data
├── pyproject.toml
├── src                                        #Module Source
│   ├── app.py                                 #Streamlit Application entry
│   ├── config                                 #Main Config for boostraping webapp
│   │   └── settings.py
│   ├── mcp_restaurant                         #CrewAI Agent Source
│   │   ├── __init__.py
│   │   ├── agent_factory.py                   #Generate Agents from yaml config
│   │   ├── config                             #Agent Config
│   │   │   ├── agents.yaml                       #Agent yaml
│   │   │   └── tasks.yaml                        #Task config yaml
│   │   ├── config.py                          #Flow config
│   │   ├── memory.py                          #Memory class using Mem0
│   │   ├── quorem.py                          #Collection of Agents tied with CrewAI Flow
│   │   └── tools                              # Tools module
│   │       ├── __init__.py
│   │       └── sqlite_tool.py                      #MCP sqlite tool
│   ├── services
│   │   └── crew_service.py                    #Crew Service bridges between streamlit and crewAI
│   └── ui                                     #Streamlit UI module
│       ├── chat.py                                 #chat ui
│       └── sidebar.py                              #configuration side bar
├── tests
└── uv.lock                                    #uv version lock
```

### Customizing

**Change `.env.example` to `.env`**
**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/mcp_restaurant/config/agents.yaml` to define your agents
- Modify `src/mcp_restaurant/config/tasks.yaml` to define your tasks
- Modify `src/mcp_restaurant/agent_factory.py` to create your agents
- Modify `src/mcp_restaurant/quorem.py` to add your agents to crewai flow
- Modify `src/services/crew_service.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
uv run streamlit run src/app.py
```

## Understanding Your Crew

The mcp-restaurant Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
