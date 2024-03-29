# Use an official Python runtime as a parent image
FROM pypy:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
#COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir scrapy pillow jsonlines

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["pypy3", "app.py"]


# reference: https://medium.com/@jeffochoa/using-docker-for-local-development-3f7d975bbadb
