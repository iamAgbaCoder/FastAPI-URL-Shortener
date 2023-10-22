from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import random
import string 

app = FastAPI()

# In-memory storage for URL mappings
url_db = {
    "pas123": "www.google.com",
    "devfest23": "www.devfest.com"
}

class URLShortenRequest(BaseModel):
    long_url: str
    
class URLShortenResponse(BaseModel):
    short_url: str


def generate_short_url():
    # Generate a random 6-character short URL
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(6))

@app.get("/")
async def index():
    for url in url_db:
        return url_db

@app.post("/shorten/", response_model=URLShortenResponse)
async def shorten_url(link: URLShortenRequest):
    long_url = link.long_url
    short_url = generate_short_url()

    url_database[short_url] = long_url

    return {"short_url": request.url_for("redirect_to_long_url", short_url=short_url)}


@app.get("/{short_url}", response_model=URLShortenResponse)
async def redirect_to_long_url(short_url: str):
    if short_url in url_db:
        long_url = url_db[short_url]
        return {"short_url": long_url}
    print(url_db)
    raise HTTPException(status_code=404, detail="URL Not Found!")