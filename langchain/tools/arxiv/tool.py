"""Tool for the Wikipedia API."""

from langchain.tools.base import BaseTool
from langchain.utilities.arxiv import ArxivAPIWrapper


class ArxivQueryRun(BaseTool):
    """Tool that adds the capability to search using the Arxiv API and to retrieve specific papers."""

    name = "Arxiv"
    description = (
        "A wrapper around Arxiv. "
        "Useful for when you need to answer specific questions about "
        "medecine, physics, math, or other scientific subjects. "
        "Input should be a search query."
    )
    api_wrapper: ArxivAPIWrapper

    def _run(self, query: str) -> str:
        """Use the Arxiv tool."""
        return self.api_wrapper.run(query)

    async def _arun(self, query: str) -> str:
        """Use the Arxiv tool asynchronously."""
        raise NotImplementedError("ArxivQueryRun does not support async")
