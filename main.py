from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models import User, Role, UpdateUser


app = FastAPI()

db: List[User] = [
    User(id=UUID('20eb6428-523a-450e-b15f-c032752b58e3'), first_name='Craig', last_name='Lister',
         gender='male', roles=[Role.student]),
    User(id=UUID('9ed16267-49b4-42bd-8f3c-45134700e499'), first_name='John', last_name='Cena',
         gender='male', roles=[Role.admin, Role.user])

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


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user.id} does not exist"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(update_body: UpdateUser, user_id: UUID):
    for user in db:
        print('user', user.id, "body id, ", user_id)
        if user.id == user_id:
            print("match found")
            if update_body.first_name is not None:
                user.first_name = update_body.first_name
            if update_body.last_name is not None:
                user.last_name = update_body.last_name
            if update_body.middle_name is not None:
                user.middle_name = update_body.middle_name
            if update_body.roles is not None:
                user.roles = update_body.roles
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user.id} does not exist"
        )
