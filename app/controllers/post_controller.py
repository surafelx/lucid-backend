from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.models.user_model import User
from app.schemas.post_schema import PostCreate, PostResponse
from app.core.database import get_db
from app.controllers.auth import get_current_user

router = APIRouter()

@router.post("/addpost", response_model=PostResponse)
def add_post(post: PostCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if len(post.text.encode('utf-8')) > 1048576:
        raise HTTPException(status_code=400, detail="Post exceeds 1MB limit")
    new_post = Post(text=post.text, owner_id=user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post