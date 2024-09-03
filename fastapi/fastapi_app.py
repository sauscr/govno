from fastapi import FastAPI, HTTPexception


app = FastAPI()

@app.get("/reports")
def get_reports():
    # Логика получения отчетов из базы данных Django
    return {"reports": []}

@app.post("/reports")
def create_report(report: dict):
    # Логика создания отчета в базе данных Django
    return {"message": "Report created"}
