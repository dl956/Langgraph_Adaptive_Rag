### Build Index

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

### from langchain_cohere import CohereEmbeddings

# Set embeddings
'''client = openai.OpenAI(
    api_key="your-api-key",
    http_client=httpx.Client(proxies="http://127.0.0.1:7890")
)
embd = OpenAIEmbeddings(client=client)
'''

embd = OpenAIEmbeddings(
    openai_api_base="https://open.bigmodel.cn/api/openai/v1",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)


# Docs to index
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# Load
docs = [WebBaseLoader(url).load() for url in urls]
#docs = [WebBaseLoader(url, requests_kwargs={"verify": False}).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

# Split
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

# Add to vectorstore
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=embd,
)
retriever = vectorstore.as_retriever()
