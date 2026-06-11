from services.chroma_service import store_document
from services.rag_service import rag_answer

store_document(
    "test1",
    """
    Smart Waste Management System uses IoT sensors
    to monitor bin levels and optimize collection routes.
    """
)

print(
    rag_answer(
        "What is the purpose of the Smart Waste Management System?"
    )
)