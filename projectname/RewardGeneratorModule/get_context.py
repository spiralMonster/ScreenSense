from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()

def get_context_from_internet(query):
    tool=TavilySearchResults(
        tavily_api_key='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',
        max_results=3,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=False,
        include_images=False
    )
    results=tool.invoke({"query":query})
    # out=[r['content'] for r in results]
    # out="\n\n".join(out)
    return results

