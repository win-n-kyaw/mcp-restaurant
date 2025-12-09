from crewai import Agent, Task
from mcp_restaurant.config import Config
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

agents_config = Config.load_agents()
tasks_config = Config.load_tasks()

db_knowledge = TextFileKnowledgeSource(
    file_paths=["database.txt"]
)

AGENT_REGISTRY = {
    'intent_classifier': ('intent_classifier', 'classify_intent_task'),
    'menu_expert': ('menu_expert', 'menu_inquiry_task'),
    'order_manager': ('order_manager', 'process_order_task'),
    'order_tracker': ('order_tracker', 'check_order_status_task'),
    'reservation_specialist': ('reservation_specialist', 'make_reservation_task'),
    'response_coordinator': ('response_coordinator', 'coordinate_response_task')
}

def agent_factory(agent_key, task_key, user_id, mem0_client, llm, tools=None, **kwargs) -> str:
    # Retrieve relevant memories for this query
    memory_context = mem0_client.retrieve_memories(user_id, kwargs.get('enquiry', ''))
    
    agent = Agent(
        role = agents_config[agent_key]['role'],
        goal = agents_config[agent_key]['goal'],
        backstory = agents_config[agent_key]['backstory'],
        memory = True,
        knowledge_sources=[db_knowledge],
        max_iter=3,
        llm=llm,
        cache = False,
        max_rpm=4,
        verbose = True
    )
    
    # Add memory context to task description
    description = tasks_config[task_key]['description'].format(**kwargs)
    if memory_context:
        description = description + memory_context
    
    task = Task(
        description=description,
        expected_output=tasks_config[task_key]['expected_output'],
        agent=agent,
        tools=tools
    )
    
    result = task.execute_sync().raw
    return result

def create_agent_task(specialist_key: str, tools, mem0_client, llm, user_id: str, **kwargs):
    agent_key, task_key = AGENT_REGISTRY[specialist_key]
    return agent_factory(agent_key, task_key, user_id, mem0_client, llm, tools, **kwargs)