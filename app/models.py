from pydantic import BaseModel
from typing import Optional
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    email: str

class Reactions(BaseModel):
    name: str
    user: Person
    count: int

class Message(BaseModel):
    user: Person
    text: str
    channel: str
    ts: str
    reactions: Reactions

class ItemEvent(BaseModel):
    type: str
    channel: Optional[str]
    ts: Optional[str]

class ReactionEvent(BaseModel):
    type: str
    user: str
    reaction: str
    item_user: str
    item: ItemEvent