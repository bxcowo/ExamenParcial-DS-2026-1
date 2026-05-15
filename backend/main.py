from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.controladores.incidencias_controlador import router as incidencias_router

app = FastAPI(
    title="Sistema de Incidencias",
    description="API para gestionar reportes de incidencias ciudadanas",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(incidencias_router)

@app.get("/")
def root():
    """Endpoint raíz para verificar que el servidor está corriendo"""
    return {
        "mensaje": "Sistema de Incidencias API",
        "documentacion": "/docs",
        "documentacion_alternativa": "/redoc"
    }

@app.get("/health")
def health_check():
    """Verificar estado de salud de la API"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
