from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {'Hello root'}

@app.get("/ping")
def root():
    return {'Hello ping'}

# run the app
if __name__ == '__main__':
    app.run()
