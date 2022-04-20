FROM python:3.9-alpine AS base

FROM base AS build

# We need to build cffi, so we will use multi-stage build
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev

WORKDIR /app

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

#################################
FROM base AS prod

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY api .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
