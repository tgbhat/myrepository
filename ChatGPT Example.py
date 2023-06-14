#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai


# In[2]:


openai.api_key = 'insert Secret API Key here'


# In[3]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


# In[4]:


# I can use ChatGPT to generate some text for a given prompt
prompt = f"""
Explain quantum mechanics in a short essay
"""
response = get_completion(prompt)
print(response)


# In[5]:


# I can ask for a shorter response
prompt = f"""
Explain quantum mechanics and use at most 150 words
"""
response = get_completion(prompt)
print(response)


# In[6]:


# I can also translate this text into another languages such as Spanish and French
prompt = f"""
Translate the following  text to Spanish and French: ```{response}```
"""
response = get_completion(prompt)
print(response)

