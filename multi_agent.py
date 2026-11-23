from crewai import Agent, Task, Crew, Process, LLM

# LLM connection
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434",
    temperature=0.2
)


# AGENT 1: RESEARCHER
researcher = Agent(
    role="Junior Technology Researcher",
    goal="Explain the given technology and its core concepts.",
    backstory="You are an enthusiastic technology researcher.",
    llm=llm,
    verbose=True
)

# AGENT 2: ANALYST
analyst = Agent(
    role="Technical Analyst",
    goal="Analyze research findings and identify practical implications.",
    backstory="You are an experienced software architect.",
    llm=llm,
    verbose=True
)

# AGENT 3: WRITER
writer = Agent(
    role="Technical Report Writer",
    goal="Produce a clear and structured technical report.",
    backstory="You are an expert technical documentation writer.",
    llm=llm,
    verbose=True
)


# TASK 1: RESEARCH
research_task = Task(
    description="""
    Research the topic: {topic}.

    Explain its definition, architecture,
    important concepts and applications.
    """,
    expected_output="A detailed research document.",
    agent=researcher
)

# TASK 2: ANALYSIS
analysis_task = Task(
    description="""
    Analyze the research findings.

    Identify:
    - Important technical insights
    - Pros and cons
    - Practical applications
    - Implementation challenges
    - Recommendations for developers

    """,
    expected_output="A structured technical analysis.",
    agent=analyst,
    context=[research_task]
)

# TASK 3: REPORT GENERATION
writing_task = Task(
    description="""
    Create a comprehensive report using
    the research and analysis.

    Include an introduction, technical
    explanation, applications, limitations , Use cases,
    and conclusion.
    """,
    expected_output="A professional technical report.",
    agent=writer,
    context=[research_task, analysis_task],
    output_file="research_report_changed.md"
)

# CREATE CREW
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential,
    verbose=True
)

# EXECUTE
result = crew.kickoff(
    inputs={"topic": "AI Agent Architecture"}
)

print("\nFINAL RESULT:\n")
print(result)