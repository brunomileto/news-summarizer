from enum import Enum
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models.anthropic import ChatAnthropic


class EnumAiModels(Enum):
    CHAT_OPENAI = ChatOpenAI
    CHAT_ANTHROPIC = ChatAnthropic
