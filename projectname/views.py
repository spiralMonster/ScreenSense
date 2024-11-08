from django.shortcuts import render
from .ActivitySuggestorModule.activity_suggestor import ActivitySuggestor
from .ActivitySuggestorModule.get_input_data import get_data
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from django.http import JsonResponse
from .ParentInsighterModule.parent_insighter import ParentInsighter
from .ParentInsighterModule.get_input_data import get_child_screen_time_results
from .ParentInsighterModule.get_right_screen_time import get_results


model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    api_key='AIzaSyD8-disvMK2_QG5guNwCJrrTg1aYYDGnkM'
)

def form(request,*args, **kwargs):
    return render(request,"info.html",{})

def activity_data(request,*args,**kwargs):

    data = get_data()
    interest = data['Interest']
    timings = data['Available Time']

    # context_getter=GetContext()
    # context=context_getter.get_result(interest)
    parser = JsonOutputParser(pydantic_object=ActivitySuggestor)
    template = """
    Your job is to:
     - Suggest activites to the childern depending upon their interests and which will be fun helpful in their 
       physical and mental growth.
     - Give brief description about suggested activites.
     - Give the benefits that can be acheived after the completion of activity.
     - Timings for completing the activity.
     - Rewards that can be acheived after completing the activity.

    **Note:
     - The rewards should be given depending upon how challenging or creative the activity was.The rewads should be in form of
      coins.
     - The timings for the activity should be given based upon the available time slots and appropriate time for that activity.
     - The output should be in form of json so don't use double quotes within the text.

    Child Interests:
    {interest}
    Available Time Slots:
    {time_slot}

    The ouput should be in the following form:
    {format_instructions}

    Suggest 9 activites in the above format
    """

    prompt = PromptTemplate.from_template(template=template,
                                          input_variable=['interest', 'time_slot'],
                                          partial_variables={"format_instructions": parser.get_format_instructions()})

    chain = prompt | model | parser

    results=chain.invoke({'interest': interest, 'time_slot': timings})

    return JsonResponse(results,safe=False)


def insights_data(request,*args,**kwargs):
    parser = JsonOutputParser(pydantic_object=ParentInsighter)

    template = """
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

    prompt = PromptTemplate.from_template(template=template,
                                          input_variable=['child_activity', 'child_screen_time', 'right_screen_time',
                                                          'format_instructions'],
                                          partial_variables={"format_instructions": parser.get_format_instructions()})

    data = get_child_screen_time_results()
    child_activity = data['child_activity']
    screen_time = data['screen_time']

    right_screen_time = get_results()

    chain = prompt | model | parser
    results = chain.invoke(
        {'child_activity': child_activity, 'child_screen_time': screen_time, 'right_screen_time': right_screen_time})

    return JsonResponse(results, safe=False)






