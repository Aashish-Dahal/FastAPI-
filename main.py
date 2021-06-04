# For API Docs use:
#localhost:port/docs
#localhost:port/redoc
from fastapi import FastAPI
app =FastAPI()

@app.get('/') 
def index():return {
     'data':'blog list'
}
@app.get('/blog/unpublished')

def unpublished():
    return {
        'data':'all unpublished blogs'
    }
@app.get('/blog/{id}')
def show(id:int):
    # fetch blog with id=id
    return {'data':id }




@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{
        "Comment1",
        "Comment2"
    }}

