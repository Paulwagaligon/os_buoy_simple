# os_buoy_simple
## Enivornment
- Windows10 or MAC OS
- python 3.7.6 above

## Install package
Window  

    $ pip install numpy fastapi uvicorn[standard]

Mac OS

    $ pip install numpy fastapi uvicorn


FastAPI and uvicorn are used as the frame  
FastAPI web: https://fastapi.tiangolo.com/zh/  
uvicorn web: https://www.uvicorn.org/


## Run and test
- First Terminal
    $ uvicorn simplebuoy_server_db_test:app 

- Second Terminal
    $ python simplebuoy_client.py (example)