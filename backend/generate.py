### Generate
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
import os
import logging

logging.basicConfig(level=logging.INFO)

# Prompt
prompt = hub.pull("rlm/rag-prompt")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

# LLM
llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    openai_api_key=api_key,
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.poixe.com/v1"),
)




# Post-processing
def format_docs(docs):
    return "\n\n".join(getattr(doc, "page_content", str(doc)) for doc in docs)
    
#def format_docs(docs):
#    return "\n\n".join(doc.page_content for doc in docs)


# Chain
rag_chain = prompt | llm | StrOutputParser()

# Run
#docs_txt = format_docs(docs)
#generation = rag_chain.invoke({"context": docs_txt, "question": question})
#print(generation)