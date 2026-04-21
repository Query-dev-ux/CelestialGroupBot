from .start import router as start_router
from .company import router as company_router
from .vacancies import router as vacancies_router
from .contacts import router as contacts_router


def register_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(company_router)
    dp.include_router(vacancies_router)
    dp.include_router(contacts_router)
