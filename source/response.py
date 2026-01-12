import random
import json

class Response:
  def __init__(self, filename="data.json"):
    self.filename = filename
    self.knowledge = []      # List of strings
    self.recent_history = []  # To prevent immediate repetition
    self.history_limit = 3    # How many past responses to remember
    self.intents = {
      "research": ["what is", "who is", "explain", "how", "why"],
      "command": ["generate", "write a", "expand", "shorter", "formal"],
      "greeting": ["hello", "hi", "hey", "good morning", "tell me"],
      "departure": ["goodbye", "bye", "see ya"],
      "system": ["who are you", "what can you do"],
      "unknown": ["idk", "hmm", "maybe"]
    }
    self.loadMemory()

  def learn(self, data):
    cleaned = data.lower().strip()
    if cleaned and cleaned not in self.knowledge:
      self.knowledge.append(cleaned)
      self.remember()
      return True
    return False

  def generateResponse(self, user_input):
    if not self.knowledge:
        return "I know nothing yet."

    user_words = set(user_input.lower().split())
    best_matches = []
    highest_score = 0

    # --- 1. CONTEXTUAL MATCHING ---
    for sentence in self.knowledge:
        sentence_words = set(sentence.split())
        overlap = [w for w in user_words & sentence_words if len(w) > 2]
        score = len(overlap)

        if score > highest_score and score > 0:
            highest_score = score
            best_matches = [sentence]
        elif score == highest_score and score > 0:
            best_matches.append(sentence)

    # --- 2. REPETITION FILTER ---
    available = [s for s in best_matches if s not in self.recent_history]

    if available:
        chosen = random.choice(available)
        output = chosen.capitalize()
    elif best_matches:
        chosen = random.choice(best_matches)
        output = f"Like I said, {chosen}."
    else:
        return "I don't understand that yet."

    # --- 3. UPDATE HISTORY ---
    self.recent_history.append(chosen)
    if len(self.recent_history) > self.history_limit:
        self.recent_history.pop(0)

    return output
    
def detect_intents(self, user_input):
  found_intents = [] # Use a list instead of returning immediately
  cleaned_input = user_input.lower()
    
  for intent, keywords in self.intents.items():
    for kw in keywords:
      kw_low = kw.lower()
        if kw_low in cleaned_input:
            found_intents.append(intent)
            break # Move to the next category once this intent is found
                
  return found_intents if found_intents else ["unknown"]
  
  def remember(self):
    with open(self.filename, "w") as f:
      json.dump(self.knowledge, f, indent=4)

  def loadMemory(self):
    try:
      with open(self.filename, "r") as f:
        self.knowledge = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
      self.knowledge = []
