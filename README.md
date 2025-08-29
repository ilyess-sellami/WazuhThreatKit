![Python](https://img.shields.io/badge/python-3.8+-blue)
![MIT License](https://img.shields.io/badge/license-MIT-green)
![Wazuh](https://img.shields.io/badge/Wazuh-Rules-orange)


**WazuhThreatKit** is a SOC-focused project that provides **custom Wazuh rules for detecting modern cyber threats**. It is designed for cybersecurity enthusiasts and **detection engineers** who want to **practice writing, testing, and implementing detection rules** in Wazuh, without needing a full Wazuh deployment.

---

## 🚀 Project Goals
- Develop **custom detection rules** for modern attack techniques with MITRE ATT&CK mapping:
  - Ransomware activity
  - Cloud & container threats (AWS CLI, Docker misuse)    
  - Living-off-the-land attacks (PowerShell, WMI)  
  - Lateral movement (SMB, RDP)  
- Test rules against **simulated logs** using Python  
- Generate **JSON alert files** for demonstration and validation  
- Provide **structured, reusable rule sets** to help detection engineers implement them in Wazuh  


---

## 📌 Features
- **Modular Wazuh rule sets**: Each threat type has its own folder with multiple ready-to-implement rules  
- **Python testing engine**: Applies Wazuh XML rules to sample logs to validate detection  
- **Comprehensive sample logs**: Simulated Linux, Windows, and cloud activity covering multiple attack techniques  
- **MITRE ATT&CK mapping**: Each rule references the corresponding tactic and technique for SOC relevance  
- **Alert generation**: Produces alerts in console output and as JSON files for testing and demonstration  
- **Detection engineer-friendly**: Rules and logs are structured to help engineers implement them directly in Wazuh  


---

## 🛠 Requirements
- Python 3.8+
- pip (latest version recommended)

---


## 🧪 Clone the Project and Start Scan

Follow these steps to get started with **WazuhThreatKit**:

### 1. Clone the Repository
```bash
git clone https://github.com/ilyess-sellami/WazuhThreatKit.git
cd WazuhThreatKit
```

### 2. Run the Scan Script
```bash
python run_alerts.py
```

---

## 📜 Rules Section

This project contains **four main modules of custom rules**, each focusing on modern cyber threats:

### 1️⃣ Ransomware Rules
The **Ransomware module** contains **10 custom rules** designed to detect common and modern ransomware behaviors. Each rule is mapped to MITRE ATT&CK tactics for impact and exfiltration, such as T1486 (Data Encrypted for Impact) and T1490 (Inhibit System Recovery).  

**Highlights of the ransomware rules include:**
- Detection of encryption commands like `cipher` or PowerShell-based file encryption.  
- Identification of suspicious file renaming patterns (`.locked`, `.encrypted`).  
- Monitoring for mass file deletion or backup deletion attempts.  
- Detection of shadow copy deletion to prevent recovery.  
- Tracking known ransomware binaries (WannaCry, Ryuk, Conti) execution.  
- Alerts for unusual rapid file creation in sensitive directories.  
- Monitoring for suspicious network activity that may indicate data exfiltration.  


### 2️⃣ Cloud Threat Rules
The **Cloud Threats module** contains **15 custom rules** designed to detect modern cloud attack behaviors across AWS, Azure, GCP, and Docker. Each rule is mapped to MITRE ATT&CK tactics for impact, persistence, initial access, and discovery, such as T1531 (Account / Resource Impact), T1078 (Valid Accounts), and T1087 (Account Discovery).

**Highlights of the cloud threat rules include:**
- Detection of destructive cloud commands, like recursive S3 or GCP bucket deletion.  
- Monitoring for termination of cloud VMs or EC2 instances.  
- Identification of suspicious IAM policy changes or privilege escalations.  
- Alerts for creation of public cloud storage buckets.  
- Detection of privileged Docker container execution.  
- Tracking unauthorized cloud CLI usage from unusual IPs or locations.  
- Monitoring for cloud resource enumeration across AWS, Azure, or GCP.  


### 3️⃣ Living-Off-the-Land (LOL) Rules
The **Living-Off-the-Land (LOL) module** contains **5 custom rules** designed to detect modern attacks using legitimate system tools such as PowerShell, WMI, and other Windows utilities. Each rule is mapped to MITRE ATT&CK tactics for execution, persistence, and lateral movement, such as T1059.001 (PowerShell), T1047 (WMI), and T1547.001 (Registry Run Keys / Startup Folder).

**Highlights of the LOL rules include:**
- Detection of encoded PowerShell commands executed for malicious purposes.  
- Identification of remote script downloads using PowerShell.  
- Monitoring for WMI process creation and lateral movement attempts.  
- Alerts for accessing or modifying startup registry keys for persistence.  
- Detection of execution of suspicious scripts from temporary folders.  


### 4️⃣ Lateral Movement Rules
The **Lateral Movement module** contains **10 custom rules** designed to detect attackers moving across the network after gaining initial access. Each rule is mapped to MITRE ATT&CK tactics for lateral movement, execution, and discovery, such as T1076 (Remote Desktop Protocol), T1021.002 (SMB/Windows Admin Shares), and T1047 (WMI).

**Highlights of the lateral movement rules include:**
- Detection of suspicious RDP logins from unusual IP addresses.  
- Monitoring PsExec execution for remote process execution.  
- Alerts for WMI remote process creation.  
- Detection of network enumeration using Windows net commands.  
- Monitoring unusual SMB connections from non-local IPs.  


---


## 📜 Sample Logs Module
The **Logs module** contains **comprehensive sample logs** for each of the four rule modules (Ransomware, Cloud Threats, Living-Off-the-Land, and Lateral Movement). Each log file includes **multiple attack techniques**, allowing you to test and demonstrate the effectiveness of the custom rules.

**Highlights of the sample logs:**
- **Ransomware log**: Detects file encryption, shadow copy deletion, backup deletion, known ransomware binaries, rapid file creation, and suspicious network activity.
- **Cloud Threats log**: Simulates destructive cloud commands across AWS, Azure, GCP, and privileged Docker container execution.
- **Living-Off-the-Land log**: Covers encoded PowerShell commands, remote script downloads, WMI process creation, registry modification, and temp folder script execution.
- **Lateral Movement log**: Includes suspicious RDP logins, PsExec execution, WMI remote process creation, network enumeration, and unusual SMB connections.


---


## 🐍 Python Scan Module

This project includes a simple Python engine that helps **Detection Engineers** test and validate Wazuh rules in a lightweight environment.

The module performs the following tasks:
- 📖 Reads Wazuh XML rules from the `rules/` folder  
- 📜 Reads sample logs from the `logs/` folder  
- ⚡ Scans logs against the rules to check for matches  
- 🛠️ Generates JSON alerts in the `alerts/` folder  

### 🎯 Objective  
The main objective of this module is to **simulate and test Wazuh rules** outside of a full Wazuh deployment, making it easier for engineers to:
- Verify if rules are triggered correctly  
- Debug and fine-tune detection logic  
- Quickly iterate on rule changes before production deployment  


---


## ⚙️ Integrating WazuhThreatKit Rules into Your Wazuh

You can easily add the custom rules from **WazuhThreatKit** into your Wazuh environment by following these steps:

### 1️⃣ Organize Your Custom Rules
1. Create a folder for your custom rules (if not already existing):

```bash
sudo mkdir -p /var/ossec/etc/rules/local_rules
```

2. Copy the XML rule files from this project into the folder

### 2️⃣ Include the Custom Rules in Wazuh
1. Open the Wazuh configuration file:

```bash
sudo nano /var/ossec/etc/ossec.conf
```

1. sure the <rules> section includes your custom folder:
```xml
<include>/var/ossec/etc/rules/local_rules/*.xml</include>
```

---

## 🔮 Future Work
- Add decoders for more advanced log parsing  
- Expand rule modules (Phishing, Insider Threats, Supply Chain Attacks)  
- Add CI/CD testing pipeline for rules validation  
- Integrate with Wazuh API for live testing  


---


## 🤝 Contributing
Contributions are welcome!  
To add new rules:
1. Fork the repo  
2. Add your rule in `rules/<module_name>/`  
3. Add corresponding test logs in `logs/`  
4. Submit a pull request 🚀  
