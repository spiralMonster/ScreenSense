from pydantic import BaseModel,Field
from typing import List

class ParentInsighter(BaseModel):
    insights: List =Field(description="List of insights about the child screen time")