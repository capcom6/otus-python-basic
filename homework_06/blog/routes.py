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

from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for

import blog.database as db
from blog.forms import PostForm

bp = Blueprint("blog", __name__)


@bp.get("/")
def index():
    last_posts = db.posts_select(limit=5, with_user=True)

    return render_template("index.html", posts=last_posts)


@bp.get("/users")
def users():
    return render_template("users.html", users=db.users_select())


@bp.route("/posts", methods=["GET", "POST"])
def posts():
    form = PostForm()
    user_id = None
    if "user_id" in request.args:
        user_id = int(request.args["user_id"])
        if user_id <= 0:
            return (
                render_template(
                    "error.html", message="User Id must be greater than zero"
                ),
                400,
            )

    if request.method == "POST":
        user_id = form.user_id.data
        if form.validate_on_submit():
            db.posts_create(
                user_id=form.user_id.data, title=form.title.data, body=form.body.data  # type: ignore
            )
            flash("Post created", "info")
            return redirect(url_for("blog.posts", user_id=form.user_id.data))

    user = None
    if user_id:
        user = db.users_get(user_id)
        if user is None:
            return (
                render_template(
                    "error.html",
                    message="User with id {} not found".format(user_id),
                ),
                404,
            )
        form.user_id.data = user_id
        posts = db.posts_select(user_id=user_id)
    else:
        posts = db.posts_select()

    return render_template("posts.html", posts=posts, user=user, form=form)
