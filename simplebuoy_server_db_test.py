"""
Arthur: PK-Chen
Purpuse: buoy server simple version
Date: 2022/4/27
"""
import uvicorn
from fastapi import FastAPI
import logging
from datetime import datetime
import numpy as np
from typing import Optional
from datetime import datetime, timezone

logger = logging.getLogger(__name__)
app = FastAPI()
id_number = 0
url = "127.0.0.1"


@app.get("/raw_data/")
async def getPamGuardData(time_stamp: Optional[datetime]=None):#存進來的資料
    global id_number
    fs = 51200
    id_number += 1
    t = np.array(range(0, fs))/fs
    freq = 1000
    amp = 1
    data = np.sin(2*np.pi*freq*t)*amp
    return_time_stamp = datetime.now(timezone.utc).isoformat("T", "milliseconds")
    returnValue = {'id': id_number, 'time_stamp':return_time_stamp, 'fs': fs, 'name':'test_data', 'data':data.tolist()}
    print(id_number)
    return returnValue


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000, log_level="info")