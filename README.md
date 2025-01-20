# NeuroServe

This is a development server for testing APIs integration with [NeuroVis](https://github.com/Carnaux/NeuroVis).

## Development

### Requirements
* [Python 3](https://www.python.org/downloads/)
* venv - Python3 should have installed it already
* [FastAPI](https://fastapi.tiangolo.com/)

### Architecture
  - /static/
  - main.py

  * `/static/` holds the files you want to serve, they will become available at http://localhost:8000/FILE-NAME
 
  * `main.py` holds all the server setup, start and routes configurations

#### Routes

 `/handshake` - To check is the server is OK. return `{"status": "OK"}`

 `/listFiles` - Will send all the file names inside the `static` folder. return `{ "files": string[]}`

`http://localhost:8000/FILE-NAME` - Public route to directly access a file. return `file data`

### Tips

Make sure the server runs on port 8000, [NeuroVis](https://github.com/Carnaux/NeuroVis) looks for the server there, or change the url in NeuroVis files.

## Setup

1. Create a Virtual Environment

    On a terminal, run:
    ```
    python -m venv .venv
    ```

2. Activate it
    ```
    source .venv/bin/activate
    ```

    2.5 You might need to update 'pip' ```python -m pip install --upgrade pip```

3. Install FastAPI
    ```
    pip install "fastapi[standard]"
    ```

4. Start the server
    ```
    python main.py
    ```

For any issues check the [FastAPI guide](https://fastapi.tiangolo.com/virtual-environments/#create-a-virtual-environment)