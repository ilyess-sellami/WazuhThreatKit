# ThreatSentinel – Modern Threat Detection with Custom Wazuh Rules


**ThreatSentinel** is a SOC-focused project that demonstrates **custom Wazuh rules for detecting modern cyber threats**. It is designed for cybersecurity enthusiasts and SOC analysts who want to **practice threat detection, log analysis, and alert simulation** without needing a full Wazuh deployment.

---

## 🚀 Project Goals
- Develop **custom detection rules** for modern attack techniques:
  - Ransomware activity
  - Cloud & container threats (AWS CLI, Docker misuse)    
  - Living-off-the-land attacks (PowerShell, WMI)  
  - Lateral movement (SMB, RDP)  
- Simulate **log monitoring and alerting** using Python  
- Provide **structured, reusable rule sets** for SOC learning and demonstration  


---

## 🛠️ Features
- **Modular rule sets**: Each threat type has its own folder with multiple rules  
- **Python engine**: Applies Wazuh XML rules to sample logs for testing  
- **Sample logs**: Preloaded with Linux, Windows, and cloud activity  
- **MITRE ATT&CK mapping**: Each rule references the corresponding tactic  
- **Alert output**: Terminal, JSON, or CSV  


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
The **Cloud Threats module** contains **10 custom rules** designed to detect modern cloud attack behaviors across AWS, Azure, GCP, and Docker. Each rule is mapped to MITRE ATT&CK tactics for impact, persistence, initial access, and discovery, such as T1531 (Account / Resource Impact), T1078 (Valid Accounts), and T1087 (Account Discovery).

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
The **Lateral Movement module** contains **5 custom rules** designed to detect attackers moving across the network after gaining initial access. Each rule is mapped to MITRE ATT&CK tactics for lateral movement, execution, and discovery, such as T1076 (Remote Desktop Protocol), T1021.002 (SMB/Windows Admin Shares), and T1047 (WMI).

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
