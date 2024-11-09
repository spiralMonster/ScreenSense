from pydantic import BaseModel,Field

class RewardGeneratorSpec(BaseModel):
    reward_name:str =Field(description="The name of the reward")
    description:str =Field(description="Description about the reward")
    coins_required:str =Field(description="Minimum coins required to unlock the reward.")