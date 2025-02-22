# Project Description
This project is a Python script that uses Selenium to automate the resolution of a reCAPTCHA v2 challenge on a Google demo page. The script utilizes the anticaptchaofficial library to solve the reCAPTCHA automatically without the need for a proxy.

## Requirements
To run this project, you will need the following libraries and tools:

Python 3.x

Selenium

WebDriver Manager

Anticaptcha Official

ChromeDriver (automatically managed by WebDriver Manager)

## Installation
### 1.Clone the repository:
        git clone https://github.com/Denny-Souza/capcha-break
        cd your-repository

### Install dependencies:

        pip install selenium webdriver-manager anticaptchaofficial

### Set up the API key:

Create a file named chave.py in the same directory as the script.

 Add the following line to the key.py file:

    python
        api_key = "YOUR_API_KEY_HERE"
        Replace YOUR_API_KEY_HERE with your AntiCaptcha API key.

## Execution
To run the script, simply execute the following command in your terminal:

    python 
        script_name.py

Replace script_name.py with the name of the file containing the code.

## How the Code Works
### 1.WebDriver Setup:

The script uses ChromeDriverManager to automatically manage the installation of ChromeDriver.

The Chrome browser is launched and navigates to the reCAPTCHA demo page.

### 2.reCAPTCHA Resolution:

 The script locates the reCAPTCHA element on the page and extracts the site key (data-sitekey).

It uses the anticaptchaofficial library to solve the reCAPTCHA.

The solution is then injected into the reCAPTCHA response field on the page.

### 3.Form Submission:

After solving the reCAPTCHA, the script clicks the form submission button.

### 4.Error Handling:

If the reCAPTCHA resolution fails, the script displays an error message and exits after 10 seconds.

## Notes
API Key: You will need a valid AntiCaptcha API key for the script to work correctly.

Wait Time: The script waits for 100 seconds after form submission to allow you to view the result before closing the browser.

## Contribution
Contributions are welcome! Feel free to open issues or pull requests to improve this project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

Note: This script is for educational and demonstration purposes only. Ensure that the use of automation tools and CAPTCHA resolution complies with the terms of service of the website in question.
