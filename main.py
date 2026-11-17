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


@app.get("/date")
def get_server_date():
    utc_now = datetime.now(timezone.utc)
    local_now = datetime.now()
    return {
        "utc": utc_now.date().isoformat(),
        "local": local_now.date().isoformat(),
        "year": local_now.year,
        "month": local_now.month,
        "day": local_now.day,
        "weekday": local_now.strftime("%A"),
    }
