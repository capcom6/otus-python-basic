# Copyright 2022 Aleksandr Soloshenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from .db import db


class IdMixin:
    id = Column(Integer, primary_key=True)


class User(IdMixin, db.Model):
    __tablename__ = "users"

    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    posts = db.relationship("Post", back_populates="user")

    def __str__(self) -> str:
        return f"User: {self.name}"


class Post(IdMixin, db.Model):
    __tablename__ = "posts"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    user = db.relationship("User", back_populates="posts")

    def __str__(self) -> str:
        return f"Post: {self.title}"
