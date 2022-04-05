from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import database, schemas
from app.core import blog
from app.oauth2 import get_current_user

router = APIRouter(tags=["blogs"], prefix="/blog")


@router.get("/", response_model=List[schemas.ShowBlog])
def all(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.get_all(db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.get(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.delete(id, db)


@router.put(
    "/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog
)
def update(
    id,
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return blog.update(id, request, db)
