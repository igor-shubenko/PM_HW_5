from fastapi import FastAPI, Request
import uvicorn

from handlers.event_handlers import startup_event_handler, shutdown_event_handler

app = FastAPI(title="Math Operations Server",
              description="Server provides math operations with users data",
              version="2.0")

app.add_event_handler('startup', startup_event_handler(app))
app.add_event_handler('shutdown', shutdown_event_handler(app))

@app.get("/median")
async def median(request: Request):
    return await request.app.task_maker.median()


@app.get("/unique_names_histogram")
async def unique_names_histogram(request: Request):
    return await request.app.task_maker.unique_names_histogram()


@app.get("/age_range")
async def age_range(request: Request, frm: int, to: int):
    return await request.app.task_maker.age_range(frm, to)


if __name__ == '__main__':
    uvicorn.run("math_operations_server:app", host='0.0.0.0', port=8766, reload=True)
