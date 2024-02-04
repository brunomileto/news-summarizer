import uvicorn
from app.api import app


def start_server():
    """Start the FastAPI server."""
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload=True)


if __name__ == '__main__':
    start_server()
