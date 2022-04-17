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


import http
from http.client import responses
from typing import List, Optional
import uu
from uuid import UUID, uuid4
from fastapi import APIRouter
import fastapi
from fastapi.responses import Response

from .models import Recipe, Ingredient, RecipeIn, RecipeIngredient


router = APIRouter(tags=["Рецепты"])

recipes = {
    UUID("c21f83f4-565b-4f63-b0b0-a27d6e46fe60"): Recipe(
        uuid="c21f83f4-565b-4f63-b0b0-a27d6e46fe60",
        name="Рецепт №1",
        ingredients=[
            RecipeIngredient(
                ingredient=Ingredient(uuid=uuid4(), name="Вода"),
                quantity=200,
                measure_name="мл",
            )
        ],
    )
}


@router.get("", response_model=list[Recipe])
def select():
    return list(recipes.values())


@router.get("/{uuid}", response_model=Recipe)
def get(uuid: UUID):
    recipe = recipes[uuid]
    if recipe is None:
        return Response(status_code=http.HTTPStatus.NOT_FOUND)
    return recipe


@router.post("", response_model=Recipe, status_code=http.HTTPStatus.CREATED)
def post(item: RecipeIn):
    uuid = uuid4()

    recipe = Recipe(uuid=uuid, **item.dict())

    recipes[uuid] = recipe

    return recipe
