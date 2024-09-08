from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI

# LLM
llm = ChatOpenAI(
    temperature=0.3,
)

# Initialize the search tool
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Define agents
researcher = Agent(
    role="Researcher",
    goal="Research the latest trends about {topic}",
    backstory="You are an expert researcher with a keen eye for detail and years of experience in {topic}.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
)

summarizer = Agent(
    role="Summarizer",
    goal="Summarize the research provided by the researcher",
    backstory="""
        You are an expert summarizer who can extract the key points from a webpage and present them in a concise and coherent summary.
        """,
    verbose=True,
    allow_delegation=False,
    max_iter=50,
    tools=[scrape_tool],
    dependencies=['researcher'],
)

writer = Agent(
    role="Writer",
    goal="Write a long, detailed paper based on the content provided by the researcher",
    backstory="""
        You are an experienced paper writer who can explain complex topics clearly.
    """,
    verbose=True,
    allow_delegation=False,
    dependencies=['summarizer'],
)

# Define tasks
research_task = Task(
    agent=researcher,
    description="""
        Research the latest trends about {topic}.
        Ensure that the information retrieved is not older than 1 month.
        """,
    expected_output="""
        A markdown file containing 10 links to articles about {topic}.

        Output format:
            # Research Paper about {topic}
            ## Title of article 1
            - Link to article 1
            - Snippes of article 1
    
            ## Title of article 2
            - Link to article 2
            - Snippes of article 2
            
            ...
        """,
    output_file="./demo2/1_research.md",
)

summarize_task = Task(
    agent=summarizer,
    description="Summarize every webpage provided by the researcher",
    expected_output="""
        You will receive a markdown file containing 10 linke to articles about {topic}.
        
        Steps to take:
            - Visit each article link in the markdown file
            - Extract only the text from the article that is relevant to {topic}
            - Summarize the extracted text in 3 to 5 sentences
            - Adding numbered citations to each article
            - Formatting references in APA version 7 style
            - Skip articles that cannot be summarized
        
        Output format:
            # Summarized paper about {topic}
            
            # Title of article 1
            summary of the article 1 [1]
            
            reference [1]
            
            # Title of article 2
            summary of the article 2 [2]
            
            reference [2]
            
            ...
        """,
    output_file="./demo2/2_summary.md",
    )

writing_task = Task(
    agent=writer,
    description="""
        Rearrange the content you receive from the summarizer into a comprehensive and high-quality paper.
        Only ues the consent provided by the summarizer and do not make up any new information.
    """,
    expected_output="""
    You will receive a markdown file containing a summary of articles about {topic}.
    Your job is to rearrange and restructure the content into a comprehensive and high-quality paper.
    
    Steps to take:
    - Create a new, engaging title for the paper 
    - Combine all the summaries together into a long, coherent narrative
    - Don't forget to include the citation number for each reference
    - Group all the APA style references into a numbered list
    
    Output format:
        # Title of the paper
        combined summary here
    
        ## References
        reference numbered list here
    
    """,
    output_file="./demo2/3_final.md",
)

# Create a crew with the agents and tasks
crew = Crew(
    agents=[researcher, summarizer, writer],
    tasks=[research_task, summarize_task, writing_task],
    verbose=True,
)

# Prompt user for the topic or use a default value
topic = input("What is your research topic? ").strip() or "Grok-2 by xAI"

inputs = {
    "topic": topic,
}

# Run the crew
result = crew.kickoff(inputs=inputs)

# Print the result
print(result)
