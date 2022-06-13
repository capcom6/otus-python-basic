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

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=255)])
    body = TextAreaField("Body", validators=[DataRequired()])
    user_id = IntegerField("User Id", validators=[DataRequired()])


class UserForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired(), Length(min=1, max=255)])
    username = StringField(
        "Login name", validators=[DataRequired(), Length(min=1, max=255)]
    )
    email = EmailField("Email", validators=[DataRequired()])
