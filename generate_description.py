import os
import openai
openai.organization = "org-uefh0cvT4xGeQhPAdqc3Ce1T"
openai.api_key = open("keys/openai").read()


# TODO: chnage to read from file
skills = {
    "required": "Spark, Python, Scala, SQL",
    "nice_to_have": "AWS"
  }
job_title = "Data Engineer"
other = "bank industry, 3 years of experience"

prompt = "I need job description for {} with required skills {} and maybe with knowledge of {} and {} ".format(
      job_title, skills.get("required"), skills.get("nice_to_have"), other
  ),

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=300,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response.get("choices")[0].get("text"))