import os

from fastapi import FastAPI, HTTPException

from fastapi.responses import JSONResponse

import openai



# Initialize FastAPI

app = FastAPI()



# Set your OpenAI API key

openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set your API key in the environment



@app.get("/")

async def read_root():

    return {"message": "Welcome to the OpenAI ASGI application!"}



@app.post("/chat")

async def chat_with_openai(prompt: str):

    try:

        # Call OpenAI's ChatCompletion API

        response = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",

            messages=[{"role": "user", "content": prompt}]

        )

        return JSONResponse(content={"response": response.choices[0].message['content']})

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

