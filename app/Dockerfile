FROM python:3.9-slim
# Set the working directory inside the container
WORKDIR /app

# Copy your application code into the container
COPY . /app


RUN pip3 install -r requirements.txt 



# Specify any commands to run your application
CMD ["sh","./run.sh"]