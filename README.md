# fastapi-httpx-demo
FastAPI x HTTPX Demo

## API Server
### 1. Initialise Project
```console
user@host:/$ poetry new api
Created package api in api
```

### 2. Change Working Directory
```console
user@host:/$ cd api
user@host:/api$
```

### 3. Add Standard Development Dependencies
```console
user@host:/api$ poetry add --group dev black isort mypy pytest
Using version ^23.1.0 for black
Using version ^5.12.0 for isort
Using version ^0.991 for mypy
Using version ^7.2.1 for pytest

Updating dependencies
Resolving dependencies... (0.7s)

Writing lock file

Package operations: 14 installs, 0 updates, 0 removals

  • Installing attrs (22.2.0)
  • Installing click (8.1.3)
  • Installing exceptiongroup (1.1.0)
  • Installing iniconfig (2.0.0)
  • Installing mypy-extensions (1.0.0)
  • Installing packaging (23.0)
  • Installing pathspec (0.11.0)
  • Installing platformdirs (2.6.2)
  • Installing pluggy (1.0.0)
  • Installing tomli (2.0.1)
  • Installing black (23.1.0)
  • Installing isort (5.12.0)
  • Installing mypy (0.991)
  • Installing pytest (7.2.1)
```

### 4. Add FastAPI Dependency
```console
user@host:/api$ poetry add fastapi
Using version ^0.89.1 for fastapi

Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file

Package operations: 7 installs, 0 updates, 0 removals

  • Installing idna (3.4)
  • Installing sniffio (1.3.0)
  • Installing anyio (3.6.2)
  • Installing typing-extensions (4.4.0)
  • Installing pydantic (1.10.4)
  • Installing starlette (0.22.0)
  • Installing fastapi (0.89.1)
```

### 5. Add Additional Development Dependency
```console
user@host:/api$ poetry add --group dev httpie uvicorn
Using version ^3.2.1 for httpie
Using version ^0.20.0 for uvicorn

Updating dependencies
Resolving dependencies... Downloading https://files.pythonhosted.org/packages/ab/43/508c403c38eeaa5fc86516eb13bb470ce77601b6d2bbcdb16e26Resolving dependencies... Downloading https://files.pythonhosted.org/packages/ab/43/508c403c38eeaa5fc86516eb13bb470ce77601b6d2bbcdb16e26Resolving dependencies... Downloading https://files.pythonhosted.org/packages/ab/43/508c403c38eeaa5fc86516eb13bb470ce77601b6d2bbcdb16e26Resolving dependencies... (9.4s)

Writing lock file

Package operations: 15 installs, 2 updates, 0 removals

  • Updating pip (22.2.2 -> 23.0)
  • Installing certifi (2022.12.7)
  • Installing charset-normalizer (3.0.1)
  • Installing mdurl (0.1.2)
  • Installing urllib3 (1.26.14)
  • Installing markdown-it-py (2.1.0)
  • Installing pygments (2.14.0)
  • Installing pysocks (1.7.1)
  • Installing requests (2.28.2)
  • Installing defusedxml (0.7.1)
  • Installing h11 (0.14.0)
  • Installing multidict (6.0.4)
  • Installing requests-toolbelt (0.10.1)
  • Installing rich (13.3.1)
  • Updating setuptools (65.3.0 -> 67.1.0)
  • Installing httpie (3.2.1)
  • Installing uvicorn (0.20.0)
```

### 6. Enter Virtualenv
```console
user@host:/api$ poetry env list
api-yFdlCiQC-py3.8 (Activated)
user@host:/api$ poetry shell
Spawning shell within /home/user/.cache/pypoetry/virtualenvs/api-yFdlCiQC-py3.8
user@host:/api#api-yFdlCiQC-py3.8$
```

### 7. Ensure Dependencies Installed
```console
user@host:/api#api-yFdlCiQC-py3.8$ poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: api (0.1.0)
```

### 8. Create a "Hello, World!" Application
```python
from fastapi import FastAPI
from typing import Mapping

app: FastAPI = FastAPI()


@app.get("/")
def get_root() -> Mapping[str, str]:
    return {"message": "Hello, World!"}
```

### 9. Use Development Dependencies
```console
user@host:/api#api-yFdlCiQC-py3.8$ isort .
Fixing /home/user/Documents/git/tombulled/fastapi-httpx-demo/api/api/__init__.py
user@host:/api#api-yFdlCiQC-py3.8$ black .
All done! ✨ 🍰 ✨
2 files left unchanged.
user@host:/api#api-yFdlCiQC-py3.8$ mypy .
Success: no issues found in 2 source files
user@host:/api#api-yFdlCiQC-py3.8$ pytest .
========================================================= test session starts ==========================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/user/Documents/git/tombulled/fastapi-httpx-demo/api
plugins: anyio-3.6.2
collected 0 items                                                                                                                      

======================================================== no tests ran in 0.01s =========================================================
```

### 10. Start the Server
```console
user@host:/api#api-yFdlCiQC-py3.8$ uvicorn api:app
INFO:     Started server process [170685]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### 11. Hit the Server
```console
user@host:/api#api-yFdlCiQC-py3.8$ http :8000
HTTP/1.1 200 OK
content-length: 27
content-type: application/json
date: Sun, 05 Feb 2023 19:26:58 GMT
server: uvicorn

{
    "message": "Hello, World!"
}
```

### 12. Improve the Implementation
```console
# TODO
```

## API Client
### 1. Initialise Projects
```console
$ poetry new client
Created package client in client
```
