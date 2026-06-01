from fastapi import FastAPI
from groq import Groq

import os



app=FastAPI()
@app.get("/") 
def home(): 
    return{ "msg":"content generated successfully" }

client=Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

@app.post("/generate")
def generte_content(
    topic:str,
    technology:str,
    content_type:str,
    tone:str
):
    prompt = f"""
    Generate a {content_type}
    Topic:{topic}
    Technology:{technology}
    Tone:{tone}
    
    """
    
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    
    return{
        "content":response.choices[0].message.content
    }
