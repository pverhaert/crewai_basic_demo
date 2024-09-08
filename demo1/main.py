from crewai import Agent, Task, Crew

researcher = Agent(
    role="Information Agent",
    goal="Provide comprehensive and accurate information about {topic}",
    backstory="""
        You are an advanced information agent with access to vast databases and resources.
        Your primary objective is to deliver detailed, factual, and well-organized information on any given topic.
        You must avoid giving personal opinions or making unsupported assumptions.
        """,
    verbose=True,
)

get_info_task = Task(
    description="Gather and present detailed information about {topic} in {language}",
    agent=researcher,
    expected_output="""
        Provide an extensive summary of {topic} in {language}, followed by a thorough explanation and 5 key points about {topic}.
        Also translate the titles in the output to {language}.
        Format the result in markdown.

        Output format:
            # {topic}
            ## Summary
            A comprehensive summary in paragraph format.

            ## Detailed Explanation
            An in-depth explanation covering various aspects of {topic}.

            ## 5 Key Points about {topic}
            - **1**: Detailed explanation of point 1.
            - **2**: Detailed explanation of point 2.
            - **3**: Detailed explanation of point 3.
            - **4**: Detailed explanation of point 4.
            - **5**: Detailed explanation of point 5.
    """,
)

crew = Crew(
    agents=[researcher],
    tasks=[get_info_task],
    full_output=True,
    verbose=True,
)

# Get user input for the topic
user_topic = input("\nEnter the topic you want information about: \n")
language = input("\nEnter the language you want the information in:").strip() or "English"

inputs = {
    'topic': user_topic,
    'language': language,
}

result = crew.kickoff(inputs=inputs)
print("*************************************************\n")
print(result)
print("\n*************************************************")
# Write the result to a file

output_filename = f"demo1/{inputs['topic'].replace(' ', '_')}.md"
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(str(result))

print(f"\nOutput has been saved as {output_filename}")
