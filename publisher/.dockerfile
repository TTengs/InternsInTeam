#Deriving the latest base image
FROM python:3.6.7

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY publisher/publish.py ./
COPY publisher/tools.txt ./
# Now the structure looks like this '/usr/app/src/test.py'

RUN pip3 install paho-mqtt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./publish.py"]