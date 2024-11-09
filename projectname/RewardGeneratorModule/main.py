from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from .reward_generator_specs import RewardGeneratorSpec
from .get_context import get_context_from_internet
from .get_input_data import get_data_results

model=ChatGoogleGenerativeAI(
      model="gemini-1.5-pro",
      api_key='AIzaSyD8-disvMK2_QG5guNwCJrrTg1aYYDGnkM'
)

template="""
Your job is to:
 - Suggest parents the reward which can be given to their child.
 - The reward can be a trip to zoo,watching a movie,cooking something special or buying a toy,etc.
 - Suggest rewards which will make the child happy and help the child to grow.
 - Use the interest of a child for suggesting rewards.

*Note:
  - For each reward you should also provide the minimum coins required to unlock the reward.

The interests of child are:
{child_interest}

You can use the following context from internet for suggesting the rewards:
{internet_context}

The ouput should be in the following form:
{format_instructions}

Suggest at least 7-10 rewards.
Provide the output in the form of json.So don't include double quotes within the text.
"""

parser=JsonOutputParser(pydantic_object=RewardGeneratorSpec)

prompt=PromptTemplate.from_template(template=template,
                                    input_variable=['child_interest','internet_context'],
                                    partial_variables={"format_instructions":parser.get_format_instructions()})

data=get_data_results()

child_interest=data['interest']
child_interest=",".join(child_interest)

query=f"My child has interest in {child_interest}.Where can i take them or what activity should i perform with them."
internet_context=get_context_from_internet(query)

chain=prompt|model|parser

results=chain.invoke({'child_interest':child_interest,'internet_context':internet_context})
