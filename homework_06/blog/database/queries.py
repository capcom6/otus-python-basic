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

from sqlalchemy.orm import joinedload
from typing import List, Union
from .models import Post, User
from .db import db


def users_select() -> List[User]:
    return User.query.all()


def users_get(user_id: int) -> Union[User, None]:
    return User.query.get(user_id)


def posts_select(
    *,
    user_id: Union[int, None] = None,
    limit: Union[int, None] = None,
    with_user: bool = False
) -> List[Post]:
    query = Post.query

    if with_user:
        query = query.options(joinedload(Post.user))

    if user_id is not None:
        query = query.filter(Post.user_id == user_id)

    query = query.order_by(Post.id.desc())

    if limit is not None:
        query = query.limit(limit)

    return query.all()


def posts_create(*, user_id: int, title: str, body: str) -> Post:
    post = Post(user_id=user_id, title=title, body=body)  # type: ignore
    db.session.add(post)
    db.session.commit()
    return post
