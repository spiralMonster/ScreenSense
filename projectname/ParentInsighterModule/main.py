from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from parent_insighter import ParentInsighter
from get_input_data import get_child_screen_time_results
from get_right_screen_time import get_results

model=ChatGoogleGenerativeAI(
      model="gemini-1.5-pro",
      api_key='AIzaSyD8-disvMK2_QG5guNwCJrrTg1aYYDGnkM'
)
parser=JsonOutputParser(pydantic_object=ParentInsighter)

template="""
Your are given the information about the screen time of the child.
Your job is to:
 - Provide insights about the child activity.
 - If valid provide the warnings.
 - Informing parents whether the child exceeded or subceed the right screen limit.
 - Asking parent to motivate child for social interactions.
 - Asking parent to limit the screen time.
 - Asking parent to change the timings of screen.For example not having a screen time just before sleep.
 
Child Screen Activity:
{child_activity}

Child Screen Time:
{child_screen_time}

Right Screen Time:
{right_screen_time}

The ouput should be in the following form:
{format_instructions}
Provide at least two-three insights in a list.
Provide the output in the form of json.So don't include double quotes within the text.
"""

prompt=PromptTemplate.from_template(template=template,
                                    input_variable=['child_activity','child_screen_time','right_screen_time','format_instructions'],
                                    partial_variables={"format_instructions": parser.get_format_instructions()})

data=get_child_screen_time_results()
child_activity=data['child_activity']
screen_time=data['screen_time']

right_screen_time=get_results()

chain=prompt|model|parser

print(chain.invoke({'child_activity':child_activity,'child_screen_time':screen_time,'right_screen_time':right_screen_time}))

