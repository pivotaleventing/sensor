FROM python:3
ADD endpoint.py /
RUN pip install fastapi uvicorn
CMD ["python", "./endpoint.py"]
