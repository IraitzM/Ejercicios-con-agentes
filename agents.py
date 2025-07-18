from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from tools import get_circle_area, get_square_area

from dotenv import load_dotenv

load_dotenv(override=True)


def create_main_agent():
    """
    Creates the main agent
    """

    # Tools it can use
    tools = [get_circle_area, get_square_area]

    # Main instructions
    prompt_template = """You are an assistant than helps people with geometry.
                        Answer the following questions as best you can
                        You have access to the following tools:

                        {tools}

                        Use the following format:

                        Question: the input question you must answer
                        Thought: you should always think about what to do
                        Action: the action to take, should be one of [{tool_names}]
                        Action Input: the input to the action
                        Observation: the result of the action
                            ... (this Thought/Action/Action Input/Observation can repeat N times)
                        Thought: I now know the final answer
                        Final Answer: the final answer to the original input question

                        Begin!

                        {chat_history}
                        Question: {input}
                        Thought:{agent_scratchpad}"""

    prompt = PromptTemplate.from_template(prompt_template)

    # Added input_key and output_key params because the extra {plan} variable in the prompt. TODO: why?
    # You need to add set the input_key when you define your memory so that the memory save_context method knows
    # where to place the user input. If not, arises an error because there's ambiguity about whether "input" or "plan"
    # are the keys that should contain the new user input.
    memory = ConversationBufferMemory(memory_key="chat_history")

    # Choose the LLM to use
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Construct the ReAct agent
    main_agent = create_react_agent(llm, tools, prompt)

    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(
        agent=main_agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        return_intermediate_steps=True,
    )

    return agent_executor
