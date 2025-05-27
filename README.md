# CVE Hunter - `huntersh7cve`

**CVE Hunter** is a powerful and user-friendly tool for scanning domains or IP addresses to detect known vulnerabilities (CVEs). Designed with cybersecurity professionals in mind, it simplifies vulnerability detection with an intuitive CLI, interactive mode, and flexible export options.

---

## 🔍 Features

- Scan single or multiple domains/IP addresses.
- Export results in **JSON** or **CSV** format.
- Interactive mode for improved user experience.
- Easy-to-use Command Line Interface (CLI).

---

## ⚙️ Installation

Follow the steps below to install **CVE Hunter**:

```bash
# Clone the repository
git clone https://github.com/hunterSH7/huntersh7cve.git

# Navigate to the project directory
cd huntersh7cve

# Make the script executable
chmod +x huntersh7cve/CVE Exploit hunter tool.py

# Install the required dependencies
pip install .


🚀 Usage
Once installed, use the following command to get started:

Basic Help
huntersh7cve -h

Command-Line Options
usage: huntersh7cve [-h] [-d DOMAIN] [-f FILE] [-o OUTPUT] [--export {json,csv}] [--interactive]

Ultimate CVE Hunter Tool

options:
  -h, --help              Show this help message and exit
  -d DOMAIN, --domain DOMAIN
                          IP address or domain to scan
  -f FILE, --file FILE    File containing list of domains/IPs to scan
  -o OUTPUT, --output OUTPUT
                          Output file to store the results (e.g., result.txt)
  --export {json,csv}     Export results in JSON/CSV format
  --interactive           Run in interactive mode

📌 Examples
Scan a Single Domain
huntersh7cve -d example.com

Scan Multiple Domains from a File
huntersh7cve -f domains.txt -o result.txt --export json

Export Results to JSON
huntersh7cve -d example.com --export json -o results.json

Run in Interactive Mode
huntersh7cve --interactive

📄 License
This project is licensed under the MIT License.

📬 Contact
Connect with the author:

Email: cs6267231@gmail.com

Discord: hunter.sh7cve

GitHub: huntersh7cve

For queries or issues, feel free to reach out on Discord: @hunter.sh7cve





