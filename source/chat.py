import json
import uuid
from datetime import datetime

class Chat:
  def __init__(self) -> None:
    self.chat_id = uuid.uuid4()
    self.memory = []

  def addMemory(self, sender, message, intent="unknown"):
    data = {
      "id": str(uuid.uuid4()),
      "sender": sender,
      "message": message,
      "intent": intent,
      "timestamp": datetime.now().isoformat()
    }
    self.memory.append(data)
    if len(self.memory) % 5 == 0:
        self.saveChat()
    return data
    
  def saveChat(self,filename="chats.json"):
    with open(filename, "w") as f:
      json.dump(self.memory, f, indent=4)
      
  def loadChat(self,filename="chats.json"):
    try:
      with open(filename, "r") as f:
        self.memory = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
      self.memory = []
        
