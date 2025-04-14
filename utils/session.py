from datetime import datetime
import os

class SessionTracker:
    def __init__(self):
        self.entries = []
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = f"reports/session_stats_{self.timestamp}.txt"

    def log(self, message):
        print(message)
        self.entries.append(message)

    def save(self):
        with open(self.filename, "w") as f:
            f.write("BreakerZero Session Log\n")
            f.write("=" * 40 + "\n")
            for entry in self.entries:
                f.write(f"{entry}\n")
        print(f"[+] Session log saved to {self.filename}")
