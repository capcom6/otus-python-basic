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

from flask import Flask
from flask_migrate import Migrate

from .database import db

from .routes import bp


app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(port=5001)
