"""
Dependency injection setup for RAG components.
"""

from src.history import get_history_service
from src.rag import RAGService
from src.rag.repositories import rag_repository


def get_rag_repository():
    """Return the singleton RAG repository instance.
    
    This ensures models are not re-initialized on each request.
    """
    return rag_repository


def get_rag_service() -> RAGService:
    return RAGService(
        rag_repository=get_rag_repository(), history_service=get_history_service()
    )
