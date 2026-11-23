
from crewai import Agent, LLM, Crew,Task,Process

# 1. Connect to the local LLM
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0.2
)

# 2. Create an AI agent
researcher = Agent(
    role="Technical Research Assistant",

    goal="Explain technical concepts accurately and clearly.",

    backstory="""
    You are an experienced software engineer.
    """,

    llm=llm,
    verbose=True
)


# 3. create a task

research_task = Task(
    description="""
    Explain {topic}.

    Include:
    1. Definition
    2. How it works
    3. Main components
    4. Real-world applications
    5. Advantages and limitations
    """,

    expected_output="""
    A well-structured technical report
    with headings, explanations and examples.
    """,

    agent=researcher
)


crew =  Crew(
    agents = [researcher],
    tasks = [research_task],
    process=Process.sequential
)

result = crew.kickoff(
    inputs={"topic": "CrewAI Framework"},
)

print("\nFINAL REPORT:\n")
print(result)