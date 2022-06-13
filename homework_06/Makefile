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

init:
	pip install -r requirements.txt

init-dev: init
	pip install -r requirements-dev.txt

start-dev:
	FLASK_APP=blog.app flask run -p 8000

start:
	gunicorn -w 4 -b 0.0.0.0:8000 --access-logfile=- blog:app

db-upgrade:
	FLASK_APP=blog.app flask db upgrade

docker-start: docker-build
	docker compose up --build

docker-build:
	docker build . -t homework_06

.PHONY: init init-dev run-dev