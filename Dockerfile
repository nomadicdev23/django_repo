# Dockefile

# the image we would be using as a base, in our case we are using official Python runtime as a parent image.
From python:3.7     

# allow Docker to cache the installed dependencies between builds

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirments.txt

# mounting the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000


# start to run the server
ENTRYPOINT ["python", "fruit_veg/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

