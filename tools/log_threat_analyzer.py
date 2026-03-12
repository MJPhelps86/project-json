"""
Project: Project Json
Module: security_log_analyzer.py

Description:
Simple log analysis utility that scans log entries for known threat indicators
such as unauthorized access attempts, failed logins, malware references, or
exploit activity. The tool returns a basic alert if suspicious keywords are
detected in the input.

Purpose:
This script is part of Project Json and demonstrates a lightweight approach
to automated security log analysis for identifying potential threats.

Usage:
Run the script and enter a log entry when prompted.

Example:
Log entry: "Unauthorized login attempt from 192.168.1.5"

Output:
[ALERT] keyword match -> unauthorized

Author: Mike Phelps

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
