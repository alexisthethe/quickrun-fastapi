from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with if {id} is not available",
        )
    return blog


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session):
    q = db.query(models.Blog).filter(models.Blog.id == id)
    blog = q.first()
    if not blog:
        raise HTTPException(
            status=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found"
        )
    q.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Blog, db: Session):
    q = db.query(models.Blog).filter(models.Blog.id == id)
    blog = q.first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found"
        )
    q.update(request.dict())
    db.commit()
    db.refresh(blog)
    return blog
