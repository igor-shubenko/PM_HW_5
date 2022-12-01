import uvicorn
from fastapi import FastAPI

from routers import users_routers, bets_routers, events_routers
from handlers.events_handlers import startup_event_handler, shutdown_event_handler

app = FastAPI(title='FastAPICRUDServer',
              description="Server for CRUD operations with postgres database",
              version="2.0")


app.add_event_handler('startup', startup_event_handler(app))
app.add_event_handler('shutdown', shutdown_event_handler(app))

app.include_router(users_routers.users_router)
app.include_router(bets_routers.bets_router)
app.include_router(events_routers.events_router)


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8765, reload=True)
