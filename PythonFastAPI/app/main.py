# def main():
#     print("Hello from app!")


# if __name__ == "__main__":
#     main()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI + uv!"}

@app.get("/up")
def read_root():
    return {"message": "UP and running!"}
