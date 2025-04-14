from core.plugin_loader import load_plugins
import traceback

def run_all_plugins(target, user, wordlist):
    print(f"[+] Running all plugins against {target} with user '{user}'...")
    plugins = load_plugins()

    for name, module in plugins:
        try:
            print(f"[*] Launching {name}...")
            # Dynamically find the class
            cracker_class = next(
                getattr(module, attr) for attr in dir(module)
                if attr.endswith("Cracker") or attr.endswith("Forcer")
            )
            cracker = cracker_class(target, user, wordlist)
            cracker.run()
        except Exception as e:
            print(f"[!] Error while running plugin '{name}': {e}")
            traceback.print_exc()
