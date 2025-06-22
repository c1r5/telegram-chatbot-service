from typing import Optional
from pydantic import BaseModel


class UserMessage(BaseModel):
    message_id: int
    chat_id: int
    message: Optional[str] = None 
    
class BotMessage(BaseModel):
    message: str
    chat_id: int
    reply_to_message_id: Optional[int] = None