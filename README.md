# ASSIGNMENT 2: Creating a Python Code and Packaging it into a Docker Container

## Python code description
A basic calculator that can add, subtract, multiply, divide, and take nth roots of numbers.  
Calculator has the following methods:

- value: returns current value in memory
- reset_value: resets current value in memory to 0
- add: adds a given number to the current value in memory
- subtract: subtracts given number from the current value in memory
- multiply: multiplies the current value in memory by the given number
- divide: divides the current value in memory by the given number
- n_root: takes nth root from the current value in memory

The calculator was tested using **pytest** package:

```bash
============================= test session starts =============================
collecting ... collected 8 items

test_calculator.py::test_value PASSED                                    [ 12%]
test_calculator.py::test_set_value PASSED                                [ 25%]
test_calculator.py::test_reset_value PASSED                              [ 37%]
test_calculator.py::test_add PASSED                                      [ 50%]
test_calculator.py::test_subtract PASSED                                 [ 62%]
test_calculator.py::test_multiply PASSED                                 [ 75%]
test_calculator.py::test_divide PASSED                                   [ 87%]
test_calculator.py::test_n_root PASSED                                   [100%]

============================== 8 passed in 0.08s ==============================

Process finished with exit code 0
```
## Requirements
requiremets.txt file was obtained using command:
```commandline
pip freeze > requirements.txt
```
And it includes the following dependencies:
```bash
colorama==0.4.6
exceptiongroup==1.2.1
iniconfig==2.0.0
packaging==24.0
pluggy==1.5.0
pytest==8.2.0
tomli==2.0.1
```

## Dockerfile
```dockerfile
# uses the official Python 3.10 slim image
FROM python:3.10-slim

# sets the working directory inside the Docker container to /app
WORKDIR /app

# copies the contents of the local calculator directory and requirements.txt to the /app directory in the Docker container.
COPY . /app

#  runs pip install to install any dependencies listed in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# sets the default command to run when the container starts
CMD ["python", "./calculator/calculator.py"]
```

## Commands used
### To build Docker image and run the container:
1. **The Docker image was created and tagged  as 'simplecalculator' using the following command:**
   ```bash
    docker build -t simplecalculator .
   ```
2. The Docker container from the image was tested locally using command:
   ```bash
    docker run -it simplecalculator
   ```
### To push the Docker Image to Docker Hub

1. **Logging in to Docker Hub**:
   ```bash
   docker login
   ```
2. **Tagging the Docker image**:
   ```bash
    docker tag simplecalculator 392781243/simplecalculator:latest
   ```
3. **Pushing the image to Docker Hub**:
   ```bash
    docker push 392781243/simplecalculator:latest
   ```
## Tag of the image
```bash
docker.io/392781243/simplecalculator:latest
```

## Usage

1. **Pull the Image**
   ```bash
   docker pull 392781243/simplecalculator:latest
   ```
2. **Run the Container**
   ```bash
   docker run 392781243/simplecalculator:latest
   ```
3. **Use the Calculator**
   ```bash
   Enter command (add, subtract, multiply, divide, root, reset, exit): add
   Enter number: 5
   Result: 5.0
   
   Enter command (add, subtract, multiply, divide, root, reset, exit): multiply
   Enter number: 10
   Result: 50.0
   ```