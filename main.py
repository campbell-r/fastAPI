from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI
from models import User, Role


app = FastAPI()

db: List[User] = [
    User(id=UUID('20eb6428-523a-450e-b15f-c032752b58e3'), first_name='Campbell', last_name='Row',
         gender='male', roles=[Role.student]),
    User(id=UUID('9ed16267-49b4-42bd-8f3c-45134700e499'), first_name='John', last_name='Cena',
         gender='female', roles=[Role.admin, Role.user])

]


@ app.get("/")
async def root():
    return {"Hello": "Campbell"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
