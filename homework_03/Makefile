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

dev-start:
	uvicorn main:app --app-dir=api --reload

docker-start: docker-build
	docker run -p 8000:8000 homework_03

docker-build:
	docker build . -t homework_03
