from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import os , json

app = FastAPI()


@app.post("/upload")
async def upload(companyname: str = Form(...),version: str = Form(...), file: UploadFile = File(...)):
    isExist = os.path.exists(companyname)
    file_path = os.path.join(companyname, file.filename)
    json_path = os.path.join(companyname, 'version.json')
    json_value = {
        'version':version,
        'companyname':companyname,
        'filename':file.filename
    }
    if not isExist:
    # Create a new directory because it does not exist
        os.makedirs(companyname)
    with open(json_path, 'w') as f:
        json.dump(json_value, f)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename}


@app.post("/download/version")
async def upload(companyname: str = Form(...)):
    with open(companyname, "r") as f:
        items = json.load(f)
    return items

@app.get("/items/{file_path}")
async def read_item(file_path: str):
   
    return  FileResponse(file_path+'/surveillens_ai_dummy.exe', media_type='application/octet-stream',filename='surveillens_ai_dummy.exe')

