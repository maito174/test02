from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


@app.get("/now")
def get_current_datetime() -> dict[str, str]:
    return {"current_datetime": datetime.now(timezone.utc).isoformat()}
