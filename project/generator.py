import random
from uuid import uuid4
from datetime import datetime, timedelta
from models import UserProfile, UserRole, LogEntry

def generate_fake_users(count: int = 1000):
    users = []
    for i in range(count):
        user = UserProfile(
            uid=uuid4(),
            username=f"user_{i}",
            role=random.choice(list(UserRole)),
            emails=[f"work_{i}@test.com", f"home_{i}@test.com"],
            logs=[
                LogEntry(datetime.now() - timedelta(days=1), "INFO", "Login success"),
                LogEntry(datetime.now(), "ERROR", "Database timeout")
            ],
            metadata={"login_count": random.randint(1, 100), "ip": "192.168.1.1"}
        )
        users.append(user)
    return users
