from fastapi import FastAPI, Depends, Request
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse

#import .py file
import schema
from database import SessionLocal, engine
from model import User
import model

#import setting for static file and server
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#Forms
from fastapi import Depends, FastAPI, Request, Form
from starlette.responses import RedirectResponse






#date and time 
app = FastAPI()

@app.get("/")
def get_datetime():
    return {"datetime": datetime.now()}


#db settings
model.Base.metadata.create_all(bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


#statics
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


#name and familiname and age and ...
@app.get("/user", response_class=HTMLResponse)
async def users(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(User).all()
    return templates.TemplateResponse("index.html", {"request": request, "data": records})

@app.get("/user/{name}", response_class=HTMLResponse)
def user(request: Request, name: schema.User.name, db: Session = Depends(get_database_session)):
    item = db.query(User).filter(User.phone==name).first()
    print(item)
    return templates.TemplateResponse("overview.html", {"request": request, "user": item})



#creat user from form

@app.post("/user/")
async def create_user(db: Session = Depends(get_database_session), name: schema.User.name = Form(...), lastname: schema.User.lastname = Form(...), age: schema.User.age = Form(...), adress: schema.User.adress = Form(...), phone: schema.User.phone = Form(...)):
    movie = User(name=name, lastname=lastname, age=age, adress=adress, phone=phone)
    db.add(user)
    db.commit()
    response = RedirectResponse('/', status_code=303)
    return response
