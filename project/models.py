from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum
from typing import List, Dict, Any

class UserRole(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str

@dataclass
class UserProfile:
    uid: UUID
    username: str
    role: UserRole
    emails: List[str]
    logs: List[LogEntry] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
