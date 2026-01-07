FROM python:3.10-slim 

WORKDIR /app

# Copy requirements and install dependencies
COPY /Document/requirements.txt . 
RUN pip install --no-cached-dir -r requirements.txt

# Copy source code 
COPY main.py . 

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]