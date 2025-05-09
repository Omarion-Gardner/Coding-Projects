import socket 
import time
import threading

# Safe import of nmap with a helpful error message
try:
    import nmap
except ImportError:
    # Handle the case where 'nmap' module is not installed
    print("[!] Error: The 'nmap' module is not installed.")
    print("    Run this command to install it: pip install python-nmap")
    exit(1)

# Lock for thread-safe list access when collecting open ports
lock = threading.Lock()

def get_valid_target():
    """Prompt user to enter a valid IP address or domain and resolve it to IP."""
    while True:
        target = input("Enter IP address or domain to scan: ")
        if not target.strip():  # Ensure input is not empty
            print("[!] Error: Input cannot be empty. Please try again.\n")
            continue
        try:
            # Resolve the domain to an IP address
            ip = socket.gethostbyname(target)
            print(f"[i] Resolving {target} to IP: {ip}")
            return ip
        except socket.gaierror as e:
            # Handle invalid domain errors
            print(f"[!] Error: {e}. Please try again.\n")

def get_port_range():
    """Prompt user to input a valid port range for scanning."""
    try:
        start = int(input("Enter start port (default 1): ") or 1)
        end = int(input("Enter end port (default 1024): ") or 1024)
        # Validate the port range
        if 1 <= start <= end <= 65535:
            return range(start, end + 1)
        else:
            print("[!] Invalid range. Using default 1–1024.")
            return range(1, 1025)
    except ValueError:
        # Handle invalid port input
        print("[!] Invalid input. Using default 1–1024.")
        return range(1, 1025)

def scan_ports(ip):
    """Scan the provided IP for open ports within the user-defined range."""
    open_ports = []  # List to store open ports
    threads = []  # List to store thread objects for concurrent scanning
    port_range = get_port_range()  # Get port range from user
    print("[i] Scanning ports...")

    # Create a thread for each port to check if it's open
    for port in port_range:
        thread = threading.Thread(target=scan_single_port, args=(ip, port, open_ports))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return open_ports

def scan_single_port(ip, port, open_ports):
    """Check if a specific port on the target IP is open."""
    if is_port_open(ip, port):
        # Add open port to the list in a thread-safe manner
        with lock:
            open_ports.append(port)

def is_port_open(ip, port):
    """Check if a single port on the target IP is open."""
    try:
        # Create a socket and attempt to connect to the target IP and port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.7)  # Set timeout to 0.7 seconds for quick scan
        sock.connect((ip, port))
        sock.close()
        return True  # Return True if port is open
    except (socket.timeout, socket.error):
        return False  # Return False if there is an error (port is closed)

def detect_services(ip, ports):
    """Run Nmap version detection on open ports and return service details."""
    print(f"\n[i] Running Nmap version detection on open ports: {ports}")
    scanner = nmap.PortScanner()  # Initialize Nmap scanner
    ports_str = ",".join(str(p) for p in ports)  # Convert list of ports to a comma-separated string

    try:
        # Run Nmap scan with -sV argument to detect version
        scanner.scan(ip, ports_str, arguments='-sV')
        service_info = []  # List to store service details for each port
        for port in ports:
            try:
                # Extract information for each port
                info = scanner[ip]['tcp'][port]
                name = info.get('name', 'unknown')
                product = info.get('product', '')
                version = info.get('version', '')
                extra = f"{product} {version}".strip()  # Concatenate product and version info

                if not extra:
                    extra = "Unknown service/version"  # Default if no extra info is available

                # Clean output: Only show service name and version, not raw HTML content
                if name.lower() == "http":
                    extra = f"{name} - {product} {version}".strip()

                # Avoid duplicate "http" service name and version in the output
                if name.lower() == "http" and extra.startswith("http -"):
                    extra = f"Apache httpd {version}"

                service_info.append((port, name, extra))  # Append service info for this port
            except KeyError:
                service_info.append((port, "unknown", "Unknown service/version"))  # Handle missing info
        return service_info
    except Exception as e:
        print(f"[!] Nmap scan failed: {e}")
        # Return failed results if Nmap scan doesn't work
        return [(port, "n/a", "Nmap failed") for port in ports]

def main():
    """Main function to run the scanner, handle user input, and display results."""
    target_ip = get_valid_target()  # Get valid target IP
    start_time = time.time()  # Record start time
    open_ports = scan_ports(target_ip)  # Scan for open ports
    end_time = time.time()  # Record end time

    if open_ports:
        # If open ports are found, run Nmap version detection
        services = detect_services(target_ip, open_ports)
        print(f"\n[+] Open ports and detected services on {target_ip}:")
        for port, name, version in services:
            print(f"    Port {port}: {name} - {version}")
    else:
        print(f"\n[-] No open ports found on {target_ip}.")

    # Print the total time taken for the scan
    print(f"[i] Scan completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    try:
        main()  # Run the main function
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")  # Handle keyboard interrupt
    input("Press Enter to exit...")  # Wait for user input before exiting
