# Instagram Scraper

This project provides a Python-based tool to scrape your Instagram followers and following lists, and identify users who don’t follow you back. It uses the [`instagrapi`](https://github.com/adw0rd/instagrapi) library for API interactions with Instagram and `.env` files to securely store your credentials.

---

## Features

- Retrieve and compare your Instagram followers and following lists.
- Identify users who are not following you back.
- Securely store and manage Instagram credentials using environment variables.
- Easy-to-use and extendable code.

---

## Prerequisites

Before using the tool, ensure that you have the following:

1. **Python**: Python 3.8 or above installed.
2. **Instagram Account**: An Instagram account is required to log in.
3. **Two-Factor Authentication**: If enabled, you may need to handle OTP manually or adjust the script for two-factor login.

---

## Installation

Follow the steps below to set up the Instagram Scraper:

### 1. Clone the Repository:

```bash
git clone https://github.com/Vanillaicee17/Instragram-Scraper.git
cd Instragram-Scraper
```

### 2. Set Up Virtual Environment (Optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables:

Create a `.env` file in the project directory and add your Instagram credentials:

```bash
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
```

---

## Usage

Once the setup is complete, run the scraper with the following command:

```bash
python scraper.py
```

The script will:

- Log in to Instagram.
- Retrieve your followers and following lists.
- Compare them to identify users who don't follow you back.
- Print the results in the console.

---

## Dependencies

- **instagrapi**: A lightweight library to interact with Instagram's API.
- **python-dotenv**: A library to manage sensitive credentials in `.env` files.

---

## Limitations

- The script relies on Instagram's API, which may impose rate limits or restrictions.
- If Instagram's API changes, the `instagrapi` library or this script may need updates.
- Ensure compliance with Instagram's Terms of Service when using this tool.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Disclaimer

This tool is intended for personal use only. Scraping data from Instagram must adhere to Instagram's terms and policies.
```
