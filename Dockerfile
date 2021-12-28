# Dockefile

# the image we would be using as a base, in our case we are using official Python runtime as a parent image.
FROM  python:3.8    

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirments.txt

# mounting the application code to the image
COPY . .


EXPOSE 8000


# start to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]