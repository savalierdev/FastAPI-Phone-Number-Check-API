from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class APIKey(BaseModel):
    key: str
    owner: str
    created_at: datetime = datetime.now()
    expires_at: Optional[datetime] = None
    is_active: bool = True

# In a real application, you would use a database to store API keys
# For now, we'll use an in-memory dictionary for demonstration
API_KEYS = {
    "fake-super-secret": APIKey(
        key="fake-super-secret",
        owner="admin",
        created_at=datetime.now(),
        is_active=True
    ),
    # You can add more API keys here
}

def validate_api_key(api_key: str) -> bool:
    """
    Validate if an API key exists and is active.
    """
    if api_key not in API_KEYS:
        return False
    
    key_data = API_KEYS[api_key]
    if not key_data.is_active:
        return False
    
    if key_data.expires_at and key_data.expires_at < datetime.now():
        return False
    
    return True
