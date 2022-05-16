FROM python:3.9.12-buster  
#FROM command similar to a from statement. Just importing python, docker hub
COPY requirements.txt requirements.txt
#copy this file we have and paste it into another computer and will be accessible to others( the folder structure)
RUN apt-get update
RUN apt install -y libgl1-mesa-glx

RUN pip install -r requirements.txt
#tell gitbash to download all the libraries
COPY data/sample data/sample
#copying all our code one by one, second sample will create a new folder for them to copy all of their stuff
COPY models models
#telling computer what folder you want into "models", keep the names the same 
COPY app app
#""
CMD streamlit run --server.port 8080 app/Galaxy_Classification_Button.py

