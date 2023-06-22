FROM python:3.8
WORKDIR pmsapp
COPY . . 
RUN python -m pip install --upgrade pip 
EXPOSE 1234
CMD ["python","pms.py"]
