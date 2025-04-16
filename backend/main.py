from fastapi import FastAPI
<<<<<<< HEAD
from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router

app = FastAPI()

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router)
app.include_router(quiz_router)
=======
from routes.users import router as users_router
from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- Add CORS Middleware ---
# This should be placed before including routers
# Allows requests from any origin (adjust in production!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Or specify frontend origin e.g., ["http://localhost:8080"]
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, DELETE, etc.)
    allow_headers=["*"], # Allows all headers
)

# --- Include Routers ---
app.include_router(items_router, prefix="/items")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(users_router, prefix="/users")
app.include_router(quiz_router, prefix="/quiz")
>>>>>>> d78737ca44aebbb43c528f6425ce1b3c85a49559

# why the hell did I write this function?
@app.get("/home")
async def get_home():
<<<<<<< HEAD
    return {"message": "Welcome to the Multi-Page FastAPI App!"}
=======
    return {"message": "Welcome to the Multi-Page FastAPI App!"}

# --- Run the application (optional, for direct execution) ---
# The CORS configuration added earlier applies when run this way too.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> d78737ca44aebbb43c528f6425ce1b3c85a49559
