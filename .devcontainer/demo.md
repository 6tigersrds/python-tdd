[ python-tdd ] Demo
================================================================================

Examples taken from this course: https://www.udemy.com/course/unit-testing-and-tdd-in-python/

Prereq: Must have Docker running on host (eg. Docker Desktop)

## 1. Open and Build Devcontainder

* F1 --> Remote-Containers: Rebuild and Reopen in Container

## 2. Note .devcontainer configuration

* F1 --> Remote-Containers: Add Development Container Configuration Files
* .devcontainer.json --> Added postCreateCommand to pip install python packages (pytest)

```json
	// Use 'postCreateCommand' to run commands after the container is created.
	"postCreateCommand": "pip3 install --user -r requirements.txt",
```
* Simple Dockerfile for Python 3 install

## 3. Run pytest:

```
pytest -v
```

## 4. Run pytest from VS Code Testing Menu

* Click on flask icon on left nav 
* Discover tests
* Run select tests
* Add a break point and debug tests
