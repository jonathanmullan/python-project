FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install flake8 pytest-playwright requests playwright
RUN playwright install
RUN playwright install-deps
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
