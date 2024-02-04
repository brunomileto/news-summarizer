from app.enums.enum_settings import EnumSettings
from app.enums.enum_ai_models import EnumAiModels
from langchain_core.language_models.chat_models import BaseChatModel
import os
from dotenv import load_dotenv
load_dotenv()


class Settings():
    DATABASE_URL = os.getenv(EnumSettings.DATABASE_URL.value)
    OPENAI_KEY = os.getenv(EnumSettings.OPENAI_API_KEY.value)
    HUGGINGFACE_KEY = os.getenv(EnumSettings.HUGGINGFACEHUB_API_TOKEN.value)
    AI_CHAT_MODEL = EnumAiModels[os.getenv(
        EnumSettings.AI_MODEL.value, EnumAiModels.CHAT_OPENAI.name)]
    SUMMARIZE = os.getenv(EnumSettings.EXECUTE_SUMMARIZER.value) == 'True'


SETTINGS = Settings()
