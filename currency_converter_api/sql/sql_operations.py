from sqlalchemy.orm import Session

from currency_converter_api.sql import models
from currency_converter_api.schemas import CreateUser
from currency_converter_api.sql.database import database_operation


@database_operation
def get_user(db: Session, email: int):
    return db.query(models.User).filter(models.User.email == email).first()


@database_operation
def get_users(db: Session):
    return db.query(models.User).all()


@database_operation
def create_user(db: Session, user: CreateUser):
    db_user = models.User(
        email=user.email,
        subscription=user.subscription,
        api_key=user.api_key,
        concurrency=user.concurrency,
        credits=user.credits,
        expiration=user.expiration
    )
    db.add(db_user)
    db.commit()
    return db_user
