from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from app.api.utils.password import get_password_hash, verify_password
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def set_password(self, new_password: str):
        self.password = get_password_hash(new_password)

    def check_password(self, password: str):
        return verify_password(password, self.password)

