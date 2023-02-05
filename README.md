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

### 3. Add Development Dependencies
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

### 5. Enter Virtualenv
```console
user@host:/api$ poetry env list
api-yFdlCiQC-py3.8 (Activated)
user@host:/api$ poetry shell
Spawning shell within /home/user/.cache/pypoetry/virtualenvs/api-yFdlCiQC-py3.8
user@host:/api#api-yFdlCiQC-py3.8$
```

### 6. Ensure Dependencies Installed
```console
user@host:/api#api-yFdlCiQC-py3.8$ poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: api (0.1.0)
```

## API Client
### 1. Initialise Projects
```console
$ poetry new client
Created package client in client
```
