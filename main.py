from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Server Time API")


@app.get("/")
def root():
    return {"message": "Server Time API", "docs": "/docs"}


@app.get("/time")
def get_server_time():
    now = datetime.now(timezone.utc)
    return {
        "utc": now.isoformat(),
        "unix": int(now.timestamp()),
        "local": datetime.now().isoformat(),
    }
