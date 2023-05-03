from django.conf import settings
import openai

openai.organization = "org-uefh0cvT4xGeQhPAdqc3Ce1T"
openai.api_key = settings.OPENAI_API_KEY

sample_natwest_jd = """

Join us as a Data Engineer

This is an exciting opportunity to use your technical expertise to collaborate with colleagues and build effortless, digital first customer experiences
You’ll be simplifying the bank by developing innovative data driven solutions, using insight to be commercially successful, and keeping our customers’ and the bank’s data safe and secure
Participating actively in the data engineering community, you’ll deliver opportunities to support the bank’s strategic direction while building your network across the bank
What you'll do
As a Data Engineer, you’ll play a key role in driving value for our customers by building data solutions. You’ll be carrying out data engineering tasks to build, maintain, test and optimise a scalable data architecture, as well as carrying out data extractions, transforming data to make it usable to data analysts and scientists, and loading data into data platforms.

You’ll also be:

Developing comprehensive knowledge of the bank’s data structures and metrics, advocating change where needed for product development
Practicing DevOps adoption in the delivery of data engineering, proactively performing root cause analysis and resolving issues
Collaborating closely with core technology and architecture teams in the bank to build data knowledge and data solutions
Developing a clear understanding of data platform cost levers to build cost effective and strategic solutions
Sourcing new data using the most appropriate tooling and integrating it into the overall solution to deliver for our customers
The skills you'll need
To be successful in this role, you’ll need a good understanding of data usage and dependencies with wider teams and the end customer, as well as experience of extracting value and features from large scale data.

You’ll also demonstrate:

Experience of ETL technical design, including data quality testing, cleansing and monitoring, and data warehousing and data modelling capabilities
Experience of using programming languages alongside knowledge of data and software engineering fundamentals
Good knowledge of modern code development practices
Strong communication skills with the ability to proactively engage with a wide range of stakeholders

"""

natwest_values = """

1.	Connected: 
    a.	Valuing differences
    b.	Collaborating
    c.	Team working
    d.	Communication
    e.	Community connections
2.	Improver innovator
    a.	Creative thinking
    b.	Continuous improvement
    c.	One Bank thinking
    d.	Digital literacy
    e.	Working at pace
    f.	Agile methodology
3.	Critical thinker	
        a.	Understanding problems
        b.	Decision making
        c.	Data literacy
        d.	Challenging decisions
        e.	Strategic thinking
    f.	Cyber Safety 
4.	Trusted advisor
    a.	Building relationships
    b.	Focusing on customers
    c.	Considering others
    d.	Doing the right thing
    e.	Taking ownership
    f.	Expertise
5.	Change ready
    a.	Resilience and wellbeing
    b.	Adaptability
    c.	Self-directed learning
    d.	Learns from experience
    e.	Constructive feedback
    f.	Coaching
    g.	Achieving results
"""

skills_needed = """
    1.	Ability to perform ETL.
    2.	Experience in spark/snowflake/python
"""

values_emobdied = """
    Connnected and critical thinker
"""

def generate_description(
        title, required_skills, yoe
):  
    prompt = f"""

    Given this sample template Job description of a data scientist in Natwest - 
    {sample_natwest_jd}
    
    Given these natwest values - 
    {natwest_values}

    Generate a job description of a {title} in NatWest where the ideal candidate has at least {yoe} years of experience and the below technical skills 
    {required_skills} and emodies these values {values_emobdied}
"""

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=600,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    return response.get("choices")[0].get("text")


def generate_questions(job_description):
    prompt2 = f"""

    Given these natwest values - 
    {natwest_values}

    Create a curated interview for this job description {job_description} and these natwest values {values_emobdied}, divide the interview process into 5 techincal questions, 5 apptitude questions and 2 case study questions.

    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt2,
        temperature=0.7,
        max_tokens=600,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.get("choices")[0].get("text")


def generate_summary(resume):
    prompt=f"Could you summarise the CV for this person with major technical and non-technical skills, key strengths and limitations, each in five bullet points. Finally, write in 5 points how you think this the CV: {resume}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=700,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.get("choices")[0].get("text")