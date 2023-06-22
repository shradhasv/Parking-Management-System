FROM python:3.8
WORKDIR pmsapp
COPY . . 
RUN pip install pillow 
EXPOSE 1234
CMD ["python","./pms.py"]
