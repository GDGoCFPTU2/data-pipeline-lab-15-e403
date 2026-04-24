from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    Đây là "hợp đồng dữ liệu" chung cho toàn bộ pipeline.
    """
    document_id: str
    source_type: str
    author: str
    category: str
    content: str
    timestamp: str
