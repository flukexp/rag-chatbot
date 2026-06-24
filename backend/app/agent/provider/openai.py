from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.core.config import settings

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3, api_key=settings.OPENAI_API_KEY)

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=512, api_key=settings.OPENAI_API_KEY)