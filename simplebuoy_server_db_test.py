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
from datetime import datetime, timezone, timedelta
import random

logger = logging.getLogger(__name__)
app = FastAPI()
id_number = 0
url = "127.0.0.1"
return_time_stamp = datetime.now(timezone.utc)


@app.get("/connect_pamguard/")
async def getConnection():
    fs = 51200
    return {'status':'success', 'fs':fs}

@app.get("/raw_data/")
async def getPamGuardData(time_stamp: Optional[datetime]=None):#存進來的資料
    global id_number, return_time_stamp
    fs = 51200
    t = np.array(range(0, fs))/fs
    freq = 1000
    amp = 1
    data = np.sin(2*np.pi*freq*t)*amp

    record = int(random.uniform(0, 4))
    print("Amount of return values: ", record)
    if record == 0:
        return [{'record':record}]
    else:
        returnList = [{'record':record}]
        for i in range(record):
            return_time_stamp += timedelta(seconds=1)
            id_number += 1
            returnValue = {'id': id_number, 'time_stamp':return_time_stamp.isoformat("T", "milliseconds"), 'fs': fs, 'name':'test_data', 'data':data.tolist()}
            returnList.append(returnValue)
        print("last time stamp: ", return_time_stamp.isoformat("T", "milliseconds"))
        return returnList


if __name__ == "__main__":
    uvicorn.run(app=app, host=url, port=8000, log_level="info")