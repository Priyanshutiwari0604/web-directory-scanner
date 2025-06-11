# Web Directory Scanner

A Python tool for discovering hidden directories and files on web servers.

## Legal Notice

**AUTHORIZED USE ONLY** - This tool is for authorized security testing and educational purposes only. Unauthorized scanning of web servers may be illegal.

## Installation

```bash
git clone https://github.com/username/web-directory-scanner.git
cd web-directory-scanner
pip install requests
```

## Usage

```bash
python directory_scanner.py
```

Follow the prompts:
- **Target URL**: Website URL (without http://)
- **Directory File**: Path to file containing directory names

## Example

```
[*] Enter Target URL: example.com
[*] Enter Name of the File Containing Directories: directories.txt
```

## Directory File Format

One directory/path per line:
```
admin
admin/login
backup
config
uploads
api/v1
dashboard
test
robots.txt
sitemap.xml
```

## Features

- Simple directory enumeration
- HTTP connection handling
- Clean output format
- Error handling for connection issues

## Sample Directory Lists

Common paths to test:
- admin, admin/login, admin/panel
- backup, backups, backup.zip
- config, config.php, configuration
- uploads, files, documents
- api, api/v1, api/users
- test, testing, dev
- robots.txt, sitemap.xml, .htaccess

## How It Works

1. Reads directory names from file
2. Constructs URLs by appending directories to target
3. Sends GET requests to each URL
4. Reports accessible directories (HTTP 200 responses)

## Requirements

- Python 3.6+
- requests library

## Output

```
[*] Discovered Directory AT This Path : http://example.com/admin
[*] Discovered Directory AT This Path : http://example.com/backup
```

## Troubleshooting

**Connection errors**: Check target URL format (don't include http://)
**File not found**: Verify directory file path
**No results**: Target may have no accessible directories or may be blocking requests

