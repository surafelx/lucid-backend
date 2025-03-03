import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI
from app.routes import user_routes, post_routes
from app.core.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(post_routes.router)
