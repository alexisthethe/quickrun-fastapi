from sqlalchemy.orm import Session

from app import models, schemas
from app.core.exceptions import NotFound


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise NotFound(models.Blog, id)
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
        raise NotFound(models.Blog, id)
    q.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Blog, db: Session):
    q = db.query(models.Blog).filter(models.Blog.id == id)
    blog = q.first()
    if not blog:
        raise NotFound(models.Blog, id)
    q.update(request.dict())
    db.commit()
    db.refresh(blog)
    return blog
