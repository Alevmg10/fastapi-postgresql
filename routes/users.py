from fastapi import APIRouter, Response, status
from typing import Optional
from pydantic import BaseModel
from starlette.status import HTTP_204_NO_CONTENT
from database import *

user = APIRouter()


class User(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    phone: str
    email: str
    department: str


@user.get("/users", tags=["users"])
def get_users():
    connect_db()
    mycur = myconn.cursor()
    query = ''' SELECT * FROM employees '''
    mycur.execute(query)
    myconn.commit()
    
    return mycur.fetchall()


@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user_by_id(id: int):
    connect_db()
    mycur = myconn.cursor()
    query = ''' SELECT * FROM employees WHERE id = %s'''
    mycur.execute(query, [str(id)])
    myconn.commit()

    return mycur.fetchone()


@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    connect_db()
    mycur = myconn.cursor()
    query = ''' INSERT INTO employees (first_name, last_name, phone, email, department) VALUES (%s, %s, %s, %s, %s) '''
    new_user = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "email": user.email,
        "deparment": user.department}
    record = mycur.execute(query, new_user)
    myconn.commit()

    return "Registered employee", new_user


@user.delete(
    "/users/{id}",
    tags=["users"],
    status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int):
    connect_db()
    mycur = myconn.cursor()
    query = ''' DELETE FROM employees WHERE id = %s '''
    mycur.execute(query, [str(id)])
    myconn.commit()

    return "Employee data deleted", Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: int, user: User):

    connect_db()
    mycur = myconn.cursor()
    query = ''' UPDATE employees SET first_name= %s, last_name= %s, phone=%s, email=%s, department=%s WHERE id=%s '''
    edit_user = (
        user.first_name,
        user.last_name,
        user.phone,
        user.email,
        user.department,
        id)
    mycur.execute(query, edit_user)
    myconn.commit()

    return "Data update", edit_user
