from typing import Optional
from mem0 import MemoryClient
import os

class Mem0_Service:
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv('MEM0_API_KEY')
        if not self.api_key:
            raise ValueError("MEM0_API_KEY not found in environment or parameters")
        
        self.client = MemoryClient(api_key=self.api_key)

    ## Memory Helper Functions
    def retrieve_memories(self, user_id: str, query: str, limit: int = 5):
        """Retrieve relevant memories for the current query"""
        try:
            # Use search with proper filters for Mem0 API
            memories = self.client.search(
                query=query, 
                user_id=user_id, 
                limit=limit,
                filters={"user_id": user_id}  # Required by Mem0 API
            )
            if memories and len(memories) > 0:
                memory_context = "\n\nRelevant information from previous interactions:\n"
                for mem in memories["results"]:
                    print(mem)
                    memory_context += f"- {mem['memory']}\n"
                return memory_context
        except Exception as e:
            print(f"Error retrieving memories: {e}")
        return ""

    def store_conversation(self, user_id: str, user_message: str, assistant_message: str):
        """Store conversation in Mem0"""
        try:
            messages = [
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": assistant_message}
            ]
            self.client.add(messages, user_id=user_id)
            print(f"[Memory] Stored conversation for user {user_id}")
        except Exception as e:
            print(f"Error storing conversation: {e}")

    def get_all_user_memories(self, user_id: str):
        """Get all memories for a user"""
        try:
            return self.client.get_all(user_id=user_id)
        except Exception as e:
            print(f"Error getting memories: {e}")
            return []

    def delete_user_memories(self, user_id: str):
        """Delete all memories for a user"""
        try:
            memories = self.client.get_all(user_id=user_id)
            for mem in memories:
                self.client.delete(memory_id=mem['id']) #type: ignore
            print(f"Deleted all memories for user {user_id}")
        except Exception as e:
            print(f"Error deleting memories: {e}")