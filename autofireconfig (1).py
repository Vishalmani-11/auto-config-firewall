import subprocess
import pyfiglet
import sys
import time


def title_card():
    title = pyfiglet.figlet_format("AUTO CONFIG FIREWALL")
    print("#" * 60)
    print(title)
    print("#" * 60)
    print("   THIS IS AN AUTOMATION TOOL FOR FIREWALL")
    print("  !! Works only for built-in firewalls in Linux !!")
    print("*" * 60)
    print("   AUTHOR: GOD$EYE")
    print("*" * 60)
    print("[!!] TOOL IS ON .......")
    print()


def run_cmd(cmd, check=True):
    """Helper to run shell commands safely."""
    result = subprocess.run(cmd, shell=True, check=check,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.stdout:
        print(result.stdout.decode().strip())
    if result.stderr:
        print(result.stderr.decode().strip())
    return result


def loading_bar(message="Loading", length=40, delay=0.05):
    print(f"\n{message} ", end="")
    for _ in range(length):
        print("#", end="", flush=True)
        time.sleep(delay)
    print("\nDone!")


def main_menu():
    print("\n" + "=" * 50)
    print("            ---- MAIN MENU ----")
    print("=" * 50)
    print("  1. UFW Firewall")
    print("  2. IPTables Firewall")
    print("  99. Exit")
    print("=" * 50)


# ─────────────────────────────────────────────────
#  UFW SECTION
# ─────────────────────────────────────────────────

def menu_ufw():
    print("\n" + "^" * 50)
    print("           --- UFW MENU ---")
    print("^" * 50)
    print("  1. Install UFW")
    print("  2. Default Settings")
    print("  3. Add Custom Port Rule")
    print("  4. Delete a Port Rule")
    print("  5. Show Status")
    print("  6. Enable UFW")
    print("  7. Disable UFW")
    print("  8. Reset UFW (clear all rules)")
    print("  99. Back to Main Menu")
    print("v" * 50)


def install_ufw():
    print("\n[!!] Checking if UFW firewall is present ........")
    if run_cmd("which ufw", check=False).returncode != 0:
        print("[*] UFW not found. Installing ...")
        run_cmd("apt-get install ufw -y")
        run_cmd("apt-get upgrade ufw -y")
        loading_bar("Installing")
        print("[+] Installation Complete!\n")
    else:
        print("[+] UFW is already installed.")


def ufw_default_settings():
    print("\n[*] Configuring UFW default settings ....")
    run_cmd("ufw default deny incoming")
    run_cmd("ufw default allow outgoing")
    run_cmd("ufw allow ssh")
    run_cmd("ufw allow http")
    run_cmd("ufw allow https")
    run_cmd("ufw --force enable")
    print("[+] Default settings applied successfully.")


def ufw_show_status():
    print("\n*** UFW Status ***")
    run_cmd("ufw status verbose")


def ufw_enable():
    print("\n[*] Enabling UFW ...")
    run_cmd("ufw --force enable")
    print("[+] UFW enabled.")


def ufw_disable():
    print("\n[*] Disabling UFW ...")
    run_cmd("ufw disable")
    print("[+] UFW disabled.")


def ufw_reset():
    confirm = input("\n[!!] This will CLEAR ALL UFW rules. Are you sure? (yes/no): ").strip().lower()
    if confirm == "yes":
        run_cmd("ufw --force reset")
        print("[+] UFW has been reset.")
    else:
        print("[-] Reset cancelled.")


def ufw_custom_ports():
    print("\n---- Adding Custom Port Rules ----")
    while True:
        action = input("\n  Action - (allow/deny/reject) or 'done' to finish: ").strip().lower()
        if action == "done":
            break
        if action not in ("allow", "deny", "reject"):
            print("[-] Invalid action. Use allow / deny / reject.")
            continue

        port = input("  Enter port number (e.g. 8080): ").strip()
        if not port.isdigit():
            print("[-] Invalid port number.")
            continue

        proto = input("  Enter protocol (tcp/udp/both): ").strip().lower()
        if proto == "both":
            run_cmd(f"ufw {action} {port}/tcp")
            run_cmd(f"ufw {action} {port}/udp")
        elif proto in ("tcp", "udp"):
            run_cmd(f"ufw {action} {port}/{proto}")
        else:
            print("[-] Invalid protocol. Use tcp / udp / both.")
            continue

        print(f"[+] Rule added: {action} {port}/{proto}")

    print("\n[+] Done adding custom port rules.")


def ufw_delete_rule():
    print("\n---- Delete a UFW Rule ----")
    ufw_show_status()
    rule = input("\n  Enter the rule to delete (e.g. 'allow 8080/tcp'): ").strip()
    run_cmd(f"ufw delete {rule}")
    print(f"[+] Rule '{rule}' deleted (if it existed).")


def ufw_loop():
    while True:
        menu_ufw()
        choice = input("\n[*] Enter your option: ").strip()
        if choice == "1":
            install_ufw()
        elif choice == "2":
            ufw_default_settings()
        elif choice == "3":
            ufw_custom_ports()
        elif choice == "4":
            ufw_delete_rule()
        elif choice == "5":
            ufw_show_status()
        elif choice == "6":
            ufw_enable()
        elif choice == "7":
            ufw_disable()
        elif choice == "8":
            ufw_reset()
        elif choice == "99":
            print("[*] Returning to main menu ...")
            break
        else:
            print("[-] Invalid option. Try again.")


# ─────────────────────────────────────────────────
#  IPTABLES SECTION
# ─────────────────────────────────────────────────

def menu_iptables():
    print("\n" + "^" * 50)
    print("         --- IPTABLES MENU ---")
    print("^" * 50)
    print("  1.  Install iptables")
    print("  2.  Default Settings (deny in / allow out)")
    print("  3.  Allow a Port")
    print("  4.  Block a Port")
    print("  5.  Block an IP Address")
    print("  6.  Allow an IP Address")
    print("  7.  Block Ping (ICMP)")
    print("  8.  Allow Ping (ICMP)")
    print("  9.  Show Current Rules")
    print("  10. Save Rules (persistent)")
    print("  11. Delete a Rule by Line Number")
    print("  12. Flush / Clear ALL Rules")
    print("  99. Back to Main Menu")
    print("v" * 50)


def install_iptables():
    print("\n[!!] Checking if iptables is present ........")
    if run_cmd("which iptables", check=False).returncode != 0:
        print("[*] iptables not found. Installing ...")
        run_cmd("apt-get install iptables -y")
        run_cmd("apt-get install iptables-persistent -y")
        loading_bar("Installing")
        print("[+] Installation Complete!\n")
    else:
        print("[+] iptables is already installed.")


def iptables_default_settings():
    print("\n[*] Applying iptables default settings ...")

    # Flush existing rules
    run_cmd("iptables -F")
    run_cmd("iptables -X")
    run_cmd("iptables -Z")

    # Set default policies
    run_cmd("iptables -P INPUT DROP")
    run_cmd("iptables -P FORWARD DROP")
    run_cmd("iptables -P OUTPUT ACCEPT")

    # Allow loopback
    run_cmd("iptables -A INPUT -i lo -j ACCEPT")
    run_cmd("iptables -A OUTPUT -o lo -j ACCEPT")

    # Allow established/related connections
    run_cmd("iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")

    # Allow SSH, HTTP, HTTPS
    run_cmd("iptables -A INPUT -p tcp --dport 22 -j ACCEPT")
    run_cmd("iptables -A INPUT -p tcp --dport 80 -j ACCEPT")
    run_cmd("iptables -A INPUT -p tcp --dport 443 -j ACCEPT")

    print("[+] Default iptables settings applied successfully.")


def iptables_allow_port():
    print("\n---- Allow a Port ----")
    port = input("  Enter port number (e.g. 8080): ").strip()
    if not port.isdigit():
        print("[-] Invalid port.")
        return
    proto = input("  Protocol (tcp/udp/both): ").strip().lower()
    if proto == "both":
        run_cmd(f"iptables -A INPUT -p tcp --dport {port} -j ACCEPT")
        run_cmd(f"iptables -A INPUT -p udp --dport {port} -j ACCEPT")
    elif proto in ("tcp", "udp"):
        run_cmd(f"iptables -A INPUT -p {proto} --dport {port} -j ACCEPT")
    else:
        print("[-] Invalid protocol.")
        return
    print(f"[+] Port {port}/{proto} allowed.")


def iptables_block_port():
    print("\n---- Block a Port ----")
    port = input("  Enter port number (e.g. 8080): ").strip()
    if not port.isdigit():
        print("[-] Invalid port.")
        return
    proto = input("  Protocol (tcp/udp/both): ").strip().lower()
    if proto == "both":
        run_cmd(f"iptables -A INPUT -p tcp --dport {port} -j DROP")
        run_cmd(f"iptables -A INPUT -p udp --dport {port} -j DROP")
    elif proto in ("tcp", "udp"):
        run_cmd(f"iptables -A INPUT -p {proto} --dport {port} -j DROP")
    else:
        print("[-] Invalid protocol.")
        return
    print(f"[+] Port {port}/{proto} blocked.")


def iptables_block_ip():
    print("\n---- Block an IP Address ----")
    ip = input("  Enter IP address to block (e.g. 192.168.1.100): ").strip()
    run_cmd(f"iptables -A INPUT -s {ip} -j DROP")
    run_cmd(f"iptables -A OUTPUT -d {ip} -j DROP")
    print(f"[+] IP {ip} blocked (inbound + outbound).")


def iptables_allow_ip():
    print("\n---- Allow an IP Address ----")
    ip = input("  Enter IP address to allow (e.g. 192.168.1.100): ").strip()
    run_cmd(f"iptables -I INPUT -s {ip} -j ACCEPT")
    print(f"[+] IP {ip} allowed.")


def iptables_block_ping():
    print("\n[*] Blocking ICMP (ping) ...")
    run_cmd("iptables -A INPUT -p icmp --icmp-type echo-request -j DROP")
    print("[+] Ping (ICMP) blocked.")


def iptables_allow_ping():
    print("\n[*] Allowing ICMP (ping) ...")
    run_cmd("iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT")
    print("[+] Ping (ICMP) allowed.")


def iptables_show_rules():
    print("\n*** Current iptables Rules (numbered) ***")
    run_cmd("iptables -L INPUT --line-numbers -n -v")
    print()
    run_cmd("iptables -L OUTPUT --line-numbers -n -v")
    print()
    run_cmd("iptables -L FORWARD --line-numbers -n -v")


def iptables_save_rules():
    print("\n[*] Saving iptables rules ...")
    # Try iptables-save to a file
    result = run_cmd("which netfilter-persistent", check=False)
    if result.returncode == 0:
        run_cmd("netfilter-persistent save")
    else:
        run_cmd("iptables-save > /etc/iptables/rules.v4")
    print("[+] Rules saved. They will persist after reboot.")


def iptables_delete_rule():
    print("\n---- Delete a Rule by Line Number ----")
    iptables_show_rules()
    chain = input("\n  Enter chain to delete from (INPUT/OUTPUT/FORWARD): ").strip().upper()
    if chain not in ("INPUT", "OUTPUT", "FORWARD"):
        print("[-] Invalid chain.")
        return
    line = input(f"  Enter line number to delete from {chain}: ").strip()
    if not line.isdigit():
        print("[-] Invalid line number.")
        return
    run_cmd(f"iptables -D {chain} {line}")
    print(f"[+] Rule {line} deleted from {chain}.")


def iptables_flush():
    confirm = input("\n[!!] This will CLEAR ALL iptables rules and reset policies. Are you sure? (yes/no): ").strip().lower()
    if confirm == "yes":
        run_cmd("iptables -F")
        run_cmd("iptables -X")
        run_cmd("iptables -Z")
        run_cmd("iptables -P INPUT ACCEPT")
        run_cmd("iptables -P OUTPUT ACCEPT")
        run_cmd("iptables -P FORWARD ACCEPT")
        print("[+] All iptables rules flushed and policies reset to ACCEPT.")
    else:
        print("[-] Flush cancelled.")


def iptables_loop():
    while True:
        menu_iptables()
        choice = input("\n[*] Enter your option: ").strip()
        if choice == "1":
            install_iptables()
        elif choice == "2":
            iptables_default_settings()
        elif choice == "3":
            iptables_allow_port()
        elif choice == "4":
            iptables_block_port()
        elif choice == "5":
            iptables_block_ip()
        elif choice == "6":
            iptables_allow_ip()
        elif choice == "7":
            iptables_block_ping()
        elif choice == "8":
            iptables_allow_ping()
        elif choice == "9":
            iptables_show_rules()
        elif choice == "10":
            iptables_save_rules()
        elif choice == "11":
            iptables_delete_rule()
        elif choice == "12":
            iptables_flush()
        elif choice == "99":
            print("[*] Returning to main menu ...")
            break
        else:
            print("[-] Invalid option. Try again.")


# ─────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    # Check for root privileges
    import os
    if os.getpid() != 0:
        print("[!!] ERROR: This tool must be run as root (sudo).")
        sys.exit(1)

    title_card()

    while True:
        main_menu()
        choice = input("\n[*] Enter your choice: ").strip()

        if choice == "1":
            ufw_loop()
        elif choice == "2":
            iptables_loop()
        elif choice == "99":
            print("\n[*] Exiting... Cyaa! 👋")
            sys.exit(0)
        else:
            print("[-] Invalid choice. Try again.")