import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from user.controller.user import router as user
from owner.controller.owner import router as owner
from core.database_controller import router as database

app = FastAPI()

origins = [
    # "https://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],      # 모든 HTTP 메서드 허용
    allow_headers=["*"]       # 모든 헤더 허용
)

app.include_router(router=user)
app.include_router(router=owner)
app.include_router(router=database)

if __name__ == '__main__':
    import os
    port = int(os.getenv('PORT', 8000))
    uvicorn.run("main:app", host='0.0.0.0', port=port, reload=True)