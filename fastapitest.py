from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Che Workspace FastAPI Example",
    description="A simple FastAPI service running inside Eclipse Che",
    version="1.0.0"
)

# Example data model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "ok"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello from FastAPI inside Eclipse Che!"}

# POST endpoint example
@app.post("/items")
async def create_item(item: Item):
    return {
        "message": "Item received",
        "item": item,
    }
