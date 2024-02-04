from langchain.schema import HumanMessage
from langchain_openai.chat_models import ChatOpenAI


class Summarizer:
    def __init__(self) -> None:
        self.chat = ChatOpenAI(model_name='gpt-4-0125-preview', temperature=0)

    def summarize(self, article_title, article_text, template):
        prompt = template.format(
            article_title=article_title, article_text=article_text, template=template)
        summary = self.chat.invoke([HumanMessage(content=prompt)]).content
        return summary
