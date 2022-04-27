"""
Arthur: PK-Chen
Purpuse: buoy server simple version
Date: 2022/4/27
"""
import uvicorn
from fastapi import FastAPI
import logging
from datetime import datetime, timezone
import numpy as np
from typing import Optional

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/pamguard/")
def sendPamGuardData(time_stamp: Optional[datetime]=None):#存進來的資料
    if time_stamp:
        fs = 51200
        t = np.array(range(0, fs))/fs
        data = np.sin(2*np.pi*1000*t)*1
        returnValue = [{'id': int, 'time_stamp': datetime.now(timezone.utc), 'fs': 51200.0, 'name': 'test_data', 'data': data}]
        return returnValue


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000, log_level="info")