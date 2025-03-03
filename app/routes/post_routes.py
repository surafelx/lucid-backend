from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.post_schema import PostCreate, PostResponse
from app.models.post_model import Post
from app.core.database import get_db
from app.controllers.auth import get_current_user
from app.models.user_model import User
from typing import List


router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/addpost", response_model=PostResponse)
def add_post(post: PostCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if len(post.text.encode('utf-8')) > 1048576:
        raise HTTPException(status_code=400, detail="Post exceeds 1MB limit")
    new_post = Post(text=post.text, owner_id=user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if post.owner_id != user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this post")

    db.delete(post)
    db.commit()
    return {"detail": "Post deleted successfully"}

@router.get("/getposts", response_model=List[PostResponse])
def get_posts(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.owner_id == user.id).all()
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found.")
    
    return posts