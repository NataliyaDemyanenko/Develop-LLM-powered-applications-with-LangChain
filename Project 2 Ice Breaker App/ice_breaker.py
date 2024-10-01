from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables = "information", template = summary_template)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock = True)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)