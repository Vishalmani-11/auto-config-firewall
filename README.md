# 🔥 AUTO CONFIG FIREWALL

<div align="center">

```
     _   _   _ _____ ___     ____ ___  _   _ _____ ___ ____
    / \ | | | |_   _/ _ \   / ___/ _ \| \ | |  ___|_ _/ ___|
   / _ \| | | | | || | | | | |  | | | |  \| | |_   | | |  _
  / ___ \ |_| | | || |_| | | |__| |_| | |\  |  _|  | | |_| |
 /_/   \_\___/  |_| \___/   \____\___/|_| \_|_|   |___\____|
```

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux-orange?style=for-the-badge&logo=linux)
![Firewall](https://img.shields.io/badge/Firewall-UFW%20%7C%20IPTables-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A powerful Linux firewall automation tool for UFW and iptables — built for speed, simplicity, and control.**

</div>

---

## 📌 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Menu Overview](#-menu-overview)
- [UFW Options](#-ufw-options)
- [iptables Options](#-iptables-options)
- [Examples](#-examples)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Security Warning](#-security-warning)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 📖 About

**AUTO CONFIG FIREWALL** is a terminal-based Python automation tool that simplifies the process of configuring Linux firewalls. Instead of memorizing complex `ufw` and `iptables` commands, this tool gives you a simple numbered menu to manage your firewall rules quickly and safely.

Whether you are a beginner setting up a server for the first time or an experienced sysadmin who wants to speed up repetitive tasks — this tool is built for you.

> ⚠️ This tool is designed exclusively for **Linux** systems with built-in firewall support (Ubuntu, Debian, Kali, etc.)

---

## ✨ Features

### UFW (Uncomplicated Firewall)
- ✅ Auto-install UFW if not present
- ✅ Apply secure default settings in one click
- ✅ Add custom port rules (allow / deny / reject)
- ✅ Delete existing rules
- ✅ Enable / Disable UFW
- ✅ Reset all UFW rules
- ✅ View live UFW status

### iptables
- ✅ Auto-install iptables and iptables-persistent
- ✅ Apply secure default policies (DROP incoming, ACCEPT outgoing)
- ✅ Allow or block specific ports (TCP / UDP / both)
- ✅ Block or allow specific IP addresses
- ✅ Block or allow ICMP (ping)
- ✅ View all rules with line numbers
- ✅ Delete rules by line number
- ✅ Save rules persistently across reboots
- ✅ Flush and reset all rules

---

## 🖥️ Requirements

| Requirement | Version |
|---|---|
| Operating System | Linux (Ubuntu / Debian / Kali recommended) |
| Python | 3.6 or higher |
| Privileges | Root / sudo required |
| pip package | `pyfiglet` |

---

## ⚙️ Installation

### Step 1 — Clone the repository
```bash
git clone https://github.com/YourUsername/auto-config-firewall.git
cd auto-config-firewall
```

### Step 2 — Install Python dependency
```bash
pip install pyfiglet
```

### Step 3 — Give execute permission (optional)
```bash
chmod +x auto_config_firewall.py
```

### Step 4 — Run the tool
```bash
sudo python3 auto_config_firewall.py
```

---

## 🚀 Usage

Always run with `sudo` since firewall changes require root privileges:

```bash
sudo python3 auto_config_firewall.py
```

If you try to run without sudo, you will see:
```
[!!] ERROR: This tool must be run as root (sudo).
```

---

## 📋 Menu Overview

```
==================================================
            ---- MAIN MENU ----
==================================================
  1. UFW Firewall
  2. IPTables Firewall
  99. Exit
==================================================
```

---

## 🛡️ UFW Options

```
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           --- UFW MENU ---
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  1. Install UFW
  2. Default Settings
  3. Add Custom Port Rule
  4. Delete a Port Rule
  5. Show Status
  6. Enable UFW
  7. Disable UFW
  8. Reset UFW (clear all rules)
  99. Back to Main Menu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

| Option | Description |
|---|---|
| Install UFW | Checks if UFW is installed and installs it if missing |
| Default Settings | Sets deny incoming, allow outgoing, opens SSH/HTTP/HTTPS |
| Add Custom Port Rule | Allows you to allow/deny/reject any port with TCP/UDP/both |
| Delete a Port Rule | Removes an existing UFW rule by name |
| Show Status | Displays all active UFW rules in verbose format |
| Enable UFW | Turns UFW on |
| Disable UFW | Turns UFW off (does NOT delete rules) |
| Reset UFW | Wipes ALL rules and disables UFW completely |

---

## 🔒 iptables Options

```
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         --- IPTABLES MENU ---
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  1.  Install iptables
  2.  Default Settings (deny in / allow out)
  3.  Allow a Port
  4.  Block a Port
  5.  Block an IP Address
  6.  Allow an IP Address
  7.  Block Ping (ICMP)
  8.  Allow Ping (ICMP)
  9.  Show Current Rules
  10. Save Rules (persistent)
  11. Delete a Rule by Line Number
  12. Flush / Clear ALL Rules
  99. Back to Main Menu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

| Option | Description |
|---|---|
| Install iptables | Installs iptables and iptables-persistent |
| Default Settings | DROP all incoming, ACCEPT outgoing, allow loopback + SSH + HTTP + HTTPS |
| Allow a Port | Opens a port for incoming connections |
| Block a Port | Drops all traffic on a specific port |
| Block an IP | Drops all inbound and outbound traffic to/from an IP |
| Allow an IP | Inserts an ACCEPT rule for a specific IP |
| Block Ping | Drops ICMP echo requests (makes server invisible to ping) |
| Allow Ping | Accepts ICMP echo requests |
| Show Rules | Lists all INPUT / OUTPUT / FORWARD rules with line numbers |
| Save Rules | Saves rules so they survive a reboot |
| Delete a Rule | Removes a rule from a chain by its line number |
| Flush All | Clears ALL rules and resets all policies to ACCEPT |

---

## 💡 Examples

### Lock down a new server with UFW:
```
Main Menu → 1 (UFW)
UFW Menu  → 1 (Install UFW)
UFW Menu  → 2 (Default Settings)
```
This will: deny all incoming, allow all outgoing, open SSH/HTTP/HTTPS, and enable UFW.

---

### Allow a custom port (e.g. 3306 for MySQL) with UFW:
```
UFW Menu → 3 (Add Custom Port Rule)
Action   → allow
Port     → 3306
Protocol → tcp
```

---

### Block a suspicious IP with iptables:
```
Main Menu      → 2 (iptables)
iptables Menu  → 5 (Block an IP Address)
IP             → 192.168.1.50
```
This drops ALL traffic from and to that IP.

---

### Save iptables rules after changes:
```
iptables Menu → 10 (Save Rules)
```
Uses `netfilter-persistent save` or `iptables-save` to persist across reboots.

---

## 📁 Project Structure

```
auto-config-firewall/
│
├── auto_config_firewall.py     # Main script
├── README.md                   # This file
└── LICENSE                     # MIT License
```

---

## 🔧 How It Works

1. The script first checks if it is running as **root**. If not, it exits immediately.
2. It displays the ASCII art title card using `pyfiglet`.
3. The user selects a firewall type from the **main menu**.
4. Each sub-menu runs specific `subprocess` calls to the actual system firewall commands.
5. All commands are executed with `shell=True` via Python's `subprocess.run()`.
6. Output from each command is printed live to the terminal.

---

## ⚠️ Security Warning

- **Always run on a machine you control.** Misconfiguring a firewall can lock you out of your own server.
- **If using over SSH:** make sure SSH (port 22) is allowed BEFORE enabling the firewall. The Default Settings option does this automatically.
- **Flushing iptables rules** resets all policies to ACCEPT — this temporarily leaves the system open. Save new rules immediately after.
- **This tool does NOT replace professional security auditing.** It is meant for quick setup and learning purposes.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork this repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add: your feature description"
   ```
4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a **Pull Request**

### Ideas for contributions:
- [ ] Add ip6tables (IPv6) support
- [ ] Add nftables support
- [ ] Add logging / audit trail of all changes made
- [ ] Add import/export of rule sets
- [ ] Add a config file for saving preferred defaults
- [ ] Port to support CentOS / RHEL (firewalld)

---

## 👤 Author

**GOD$EYE**

- GitHub: [@YourUsername](https://github.com/YourUsername)

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

```
MIT License

Copyright (c) 2024 GOD$EYE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software.
```

---

<div align="center">

Made with 🔥 by **GOD$EYE**

⭐ If this tool helped you, give it a star on GitHub!

</div>
