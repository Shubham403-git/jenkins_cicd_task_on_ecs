FROM centos:8
RUN yum install python3 -y
RUN pip3 install Flask
COPY . .
EXPOSE 5000
#CMD "pip3 install Flask"
CMD [ "python3","app.py" ]