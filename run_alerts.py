import os
import re
import json
import xml.etree.ElementTree as ET

# Paths relative to root
RULES_DIR = "rules"
LOGS_DIR = "logs"
ALERTS_DIR = "alerts"

# Ensure alerts folder exists
os.makedirs(ALERTS_DIR, exist_ok=True)

def load_rules(rules_dir):
    """Parse Wazuh XML rules and return a list of dicts"""
    rules = []
    for root_dir, _, files in os.walk(rules_dir):
        for file in files:
            if file.endswith(".xml"):
                tree = ET.parse(os.path.join(root_dir, file))
                root = tree.getroot()
                for rule in root.findall(".//rule"):
                    rule_id = rule.attrib.get("id", "unknown")
                    level = rule.attrib.get("level", "5")
                    description = rule.findtext("description", "No description")
                    # Combine all regex patterns in <field> elements
                    patterns = [field.text for field in rule.findall(".//field") if field.text]
                    rules.append({
                        "id": rule_id,
                        "level": level,
                        "description": description,
                        "patterns": patterns,
                        "module": os.path.basename(root_dir)
                    })
    return rules

def load_logs(logs_dir):
    """Load all logs as list of lines or JSON objects"""
    logs = []
    for root_dir, _, files in os.walk(logs_dir):
        for file in files:
            path = os.path.join(root_dir, file)
            if file.endswith(".log"):
                with open(path, "r", encoding="utf-8") as f:
                    logs.extend([{"line": line.strip(), "file": file, "module": os.path.basename(root_dir)} for line in f])
            elif file.endswith(".json"):
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for entry in data:
                        logs.append({"line": str(entry), "file": file, "module": os.path.basename(root_dir)})
    return logs

def generate_alerts(rules, logs):
    """Match logs with rules and return alert list"""
    alerts = []
    for log in logs:
        for rule in rules:
            for pattern in rule["patterns"]:
                if pattern and re.search(pattern, log["line"], re.IGNORECASE):
                    alerts.append({
                        "rule_id": rule["id"],
                        "level": rule["level"],
                        "description": rule["description"],
                        "log_line": log["line"],
                        "module": rule["module"],
                        "file": log["file"]
                    })
    return alerts

def save_alerts(alerts):
    """Save alerts to JSON file"""
    output_file = os.path.join(ALERTS_DIR, "alerts.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(alerts, f, indent=4)
    print(f"[INFO] {len(alerts)} alerts saved to {output_file}")

if __name__ == "__main__":
    print("[INFO] Loading rules...")
    rules = load_rules(RULES_DIR)
    print(f"[INFO] {len(rules)} rules loaded.")

    print("[INFO] Loading logs...")
    logs = load_logs(LOGS_DIR)
    print(f"[INFO] {len(logs)} log entries loaded.")

    print("[INFO] Generating alerts...")
    alerts = generate_alerts(rules, logs)
    save_alerts(alerts)
    print("[INFO] Done.")
