from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.schema import AIMessage
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.2)

def generate_outline(topic: str) -> str:
    outline_template = """
    You are a blog content creator. Given a topic, generate a structured outline for a blog.

    Topic: {topic}
    Outline:
    - 
    """
    outline_prompt = PromptTemplate(input_variables=["topic"], template=outline_template)
    outline_chain = outline_prompt | llm
    outline = outline_chain.invoke({"topic": topic})
    
    # Ensure the outline is a string and format it
    return str(outline).replace('\n', ' ').replace('- ', '').strip()

def fill_content(outline: str) -> str:
    content_filler_template = """
    You are a content creator. Given an outline, fill in the details with rich, informative content.

    Outline: {outline}
    Content:
    """
    content_filler_prompt = PromptTemplate(input_variables=["outline"], template=content_filler_template)
    content_filler_chain = content_filler_prompt | llm
    content = content_filler_chain.invoke({"outline": outline})
    
    # Ensure the content is a string and format it
    return str(content).replace('\n', ' ').strip()

def format_content(content: str) -> str:
    content_formatter_template = """
    You are a content creator. Given the filled content, format it properly for readability and flow.

    Content: {content}
    Formatted Content:
    """
    content_formatter_prompt = PromptTemplate(input_variables=["content"], template=content_formatter_template)
    content_formatter_chain = content_formatter_prompt | llm
    formatted_content = content_formatter_chain.invoke({"content": content})
    
    # Ensure the formatted content is a string and format it
    return str(formatted_content).replace('\n', ' ').strip().split('additional_kwargs=')[0]  # Remove unwanted metadata

# topic = "The Impact of Artificial Intelligence on Society"
topic = ""

outline = generate_outline(topic)
print("Outline Generated:")
print(outline)

content = fill_content(outline)
print("\nContent Filled:")
print(content)

formatted_content = format_content(content)
print("\nFormatted Content:")
print(formatted_content)

print("\nFinal Formatted Blog Content:")
print(formatted_content)
