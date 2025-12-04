from fastapi import FastAPI

app = FastAPI()

@app.get("/requests")
def get_my_requests():
    return "yoo!"

if __name__ == '__main__':
    main()