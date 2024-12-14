import os
import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
# 임시 파일 저장 경로 설정
FILE_DIR = Path(BASE_DIR / "files")
FILE_DIR.mkdir(exist_ok=True)


@app.post("/upload/", description="파일 업로드")
async def upload_file(file: UploadFile = File(...)):
    file_path = FILE_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "path": str(file_path)}


@app.get("/files/", description="파일 목록 조회")
async def list_files():
    files = [f.name for f in FILE_DIR.iterdir() if f.is_file()]
    return {"files": files}
