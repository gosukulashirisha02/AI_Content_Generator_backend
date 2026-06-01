from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app=FastAPI()

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

@app.post("/generate")
def generte_content(
    topic:str,
    technolofy:str,
    content_type:str,
    tone:str
):
    prompt=f"""
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
                "content":"prompt"
            }
        ]
    )
    
    return{
        "content":response.choices[0].message.content
    }
