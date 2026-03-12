# simple log keyword scanner for Project Json

class JsonThreatAnalyzer:

    def __init__(self):

        # basic indicators we want to flag
        self.keywords = [
            "unauthorized",
            "failed login",
            "malware",
            "exploit",
            "suspicious"
        ]

    def analyze_log(self, log_entry):

        # quick input check
        if not log_entry:
            return "[ERROR] empty log entry"

        text = str(log_entry).lower()

        for word in self.keywords:
            if word in text:
                return f"[ALERT] keyword match -> {word}"

        return "[OK] nothing suspicious found"

def main():

    analyzer = JsonThreatAnalyzer()

    log = input("Log entry: ")

    result = analyzer.analyze_log(log)

    print(result)

if __name__ == "__main__":
    main()
