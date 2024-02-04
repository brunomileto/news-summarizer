from langchain.schema import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel, BaseMessage
from app.enums.enum_models_name import EnumModelsName
from app.enums.enum_template_language import EnumTemplateLanguage
from app.config.settings import SETTINGS


class Summarizer:
    def __init__(self, chat_model: BaseChatModel, model_name=EnumModelsName.GPT_4_PREV) -> None:
        self.chat: BaseChatModel = chat_model(
            model_name=model_name.value, temperature=0)

    def summarize(self, article_title, article_text, language: EnumTemplateLanguage = EnumTemplateLanguage.ENGLISH):
        template = self.__get_template()
        prompt = template.format(
            article_title=article_title,
            article_text=article_text,
            language=language.value,
            template=template
        )
        if (SETTINGS.SUMMARIZE):
            summary = self.chat.invoke([HumanMessage(content=prompt)]).content
            return summary
        else:
            return ''

    def __get_template(self) -> str:
        return """You are an advanced AI assistant that summarizes the given articles and
        translates them to {language} language, making the necessary adjustments.

        Here is the article you need to summarize:
        Title: {article_title}
        Text: {article_text}

        Provide a summarized version of the article in a bulleted list format of max 5 bullets in {language}.
        Important, add the article title to your answer.
        """
