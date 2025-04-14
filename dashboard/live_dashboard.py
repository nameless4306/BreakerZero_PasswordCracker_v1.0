import threading
import time
import sys
import os
from datetime import datetime

class LiveDashboard:
    def __init__(self):
        self.total_attempts = 0
        self.successes = []
        self._running = True
        self._lock = threading.Lock()
        self._thread = threading.Thread(target=self.display_loop)

    def log_attempt(self):
        with self._lock:
            self.total_attempts += 1

    def log_success(self, msg):
        with self._lock:
            self.successes.append(msg)

    def start(self):
        self._thread.start()

    def stop(self):
        self._running = False
        self._thread.join()
        self.save_stats()

    def display_loop(self):
        while self._running:
            with self._lock:
                sys.stdout.write("\033[2J\033[H")  # Clear terminal screen
                print("[BreakerZero] Live Attack Dashboard")
                print("=" * 40)
                print(f"Attempts: {self.total_attempts}")
                print(f"Successes: {len(self.successes)}")
                for msg in self.successes:
                    print(f" [+] {msg}")
            time.sleep(2)

    def save_stats(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/session_stats_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("BreakerZero Session Stats\n")
            f.write("=" * 40 + "\n")
            f.write(f"Total Attempts: {self.total_attempts}\n")
            f.write(f"Successes: {len(self.successes)}\n")
            for msg in self.successes:
                f.write(f" [+] {msg}\n")
        print(f"[+] Session stats saved to {filename}")
