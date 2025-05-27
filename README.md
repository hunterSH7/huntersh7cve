# huntersh7cve
CVE Hunter
CVE Hunter is a powerful and user-friendly tool for scanning domains or IP addresses to detect vulnerabilities (CVEs). Designed for cybersecurity professionals, it provides efficient domain/IP scanning, interactive mode, and export options for results.

Features
Scan single or multiple domains/IP addresses.
Export results in JSON or CSV format.
Interactive mode for a better user experience.
Easy-to-use CLI interface.

Installation
Follow these steps to install CVE Hunter:

┌──(rooter㉿rooter)-[/huntersh7cve]

└─$ git clone https://github.com/hunterSH7/huntersh7cve.git

┌──(rooter㉿rooter)-[/tmp/huntersh7cve]

└─$ cd huntersh7cve

┌──(rooter㉿rooter)-[/huntersh7cve]

└─$ chmod +x huntersh7cve/CVE Exploit hunter tool.py

┌──(rooter㉿rooter)-[/huntersh7cve]

└─$ pip install .

Usage Once installed, use the following commands to run CVE Hunter:

Basic Help Command
┌──(rooter㉿rooter)-[/huntersh7cve]

└─$ huntersh7cve -h
Output Example
image image

Command-Line Options
usage: huntersh7cve [-h] [-d DOMAIN] [-f FILE] [-o OUTPUT] [--export {json,csv}] [--interactive]

Ultimate CVE Hunter Tool

options:
  -h, --help            Show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        IP address or domain to scan
  -f FILE, --file FILE  File containing list of domains/IPs to scan
  -o OUTPUT, --output OUTPUT
                        Output file to store the results (e.g., result.txt)
  --export {json,csv}   Export results in JSON/CSV format
  --interactive         Run in interactive mode
Examples
Scan a Single Domain
huntersh7cve -d example.com 
Scan Multiple Domains from a File
huntersh7cve -f domains.txt -o result.txt --export json
Export Results to JSON
huntersh7cve -d example.com --export json -o results.json
Run in Interactive Mode
huntersh7cve --interactive
Contributions
CVE Hunter is open for contributions! Feel free to submit issues, feature requests, or pull requests to help improve the tool.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Connect with huntersh7 via:

Email: cs6267231@gmail.com

Discord: 

Twitter: 

GitHub Repository: huntersh7cve

For queries or issues, contact @Shubhamrooter on GitHub. Special thanks to @mr-kasim-mehar for the support

