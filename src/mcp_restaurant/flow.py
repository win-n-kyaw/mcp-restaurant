from crewai.flow.flow import Flow, listen, start
from crewai import Agent
from mcp_restaurant.skills import Skills
from crewai.flow.persistence.base import FlowPersistence
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from mcp_restaurant.memory import Mem0_Service
from typing import Any
from pydantic import BaseModel

db_knowledge = TextFileKnowledgeSource(
    file_paths=["database.txt"]
)

mem0_client = Mem0_Service()

class TestState(BaseModel):
    enquiry: str = ""
    intent: str = ""
    customer_name: str = ""

class TestFlow(Flow[TestState]):
    def __init__(self, llm=None, persistence: FlowPersistence | None = None, tracing: bool | None = None, **kwargs: Any) -> None:
        super().__init__(persistence, tracing, **kwargs)
        self.llm = llm
        self.agent = Agent(
            role = "Multi Skilled Agent",
            goal = "Provide customers with the request they wanted with clear and precise response",
            backstory = "You are a skilled agent with access to multiple skills/tools. Your excel at choosing right skillset for providing best support to customers",
            llm = self.llm,
            verbose = True,
            knowledge_sources = [db_knowledge]
        )
        self.skill = Skills(self.agent)

    @start()
    def classify_intent(self):
        self.state.intent = self.skill.use_skill(enquiry=self.state.enquiry, user_id=self.state.customer_name)
        self.skill.update_skill(skill_context=self.state.intent)

    @listen(classify_intent)
    def handle_request(self):
        answer = self.skill.use_skill(enquiry=self.state.enquiry, user_id=self.state.customer_name,customer_name=self.state.customer_name)
        final_response = self.skill.generate_response(enquiry=self.state.enquiry, answer=answer)
        return final_response