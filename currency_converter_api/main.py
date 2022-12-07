from fastapi import FastAPI

from routers.converter import router as converter_router
from routers.users import router as user_router
from sql.database import database


description = """
Currency Converter allows you to:

* get all supported currencies
* convert currencies
* fetch a single currency exchange rate
* fetch all currency exchange rate

Data fetched from fastforex.io api.
"""

app = FastAPI(
    title="Currency Converter",
    description=description,
    contact={
        "name": "FastForex",
        "url": "https://www.fastforex.io/",
    },
)

app.include_router(user_router)
app.include_router(converter_router)


@app.on_event("startup")
async def startup():
    database.create_session()


@app.on_event("shutdown")
async def shutdown():
    database.dispose_session()
