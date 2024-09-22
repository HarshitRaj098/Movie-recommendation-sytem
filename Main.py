from fastapi import FastAPI

from fastapi.responses import JSONResponse

import json

import openai



app = FastAPI()



# Load movie data from JSON file

with open('movies.json', 'r') as file:

    movies = json.load(file)



# Set your OpenAI API key

openai.api_key = 'YOUR_OPENAI_API_KEY'



@app.get("/")

def read_root():

    return {"message": "Welcome to the Movie Recommendation System!"}



@app.get("/recommendations/{genre}")

def get_recommendations(genre: str):

    recommended_movies = [movie for movie in movies if genre in movie["genres"]]

    if not recommended_movies:

        return JSONResponse(content={"message": "No movies found for this genre."}, status_code=404)

    return recommended_movies



@app.post("/chatgpt/recommend")

async def chatgpt_recommendation(prompt: str):

    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",

        messages=[{"role": "user", "content": prompt}]

    )

    return {"recommendation": response.choices[0].message['content']}



if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

