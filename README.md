# GENAPTCHA: Proof-of-Concept for Solving Amazon CAPTCHAs using Generative AI

This project demonstrates a proof-of-concept for automating the solution of Amazon's CAPTCHA using Selenium for web automation and Google's Gemini 1.5 Pro model for image analysis and text extraction.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

GENAPTCHA is designed to automate the process of solving Amazon's CAPTCHA challenges. By leveraging Selenium for web automation and Google's Gemini 1.5 Pro model for image analysis, this project showcases the potential of generative AI in overcoming simple CAPTCHA barriers.

## Features

- **Web Automation**: Uses Selenium to navigate and interact with Amazon's CAPTCHA.
- **Image Analysis**: Utilizes Google's Gemini 1.5 Pro model to analyze and extract text from CAPTCHA images.
- **Automated CAPTCHA Solving**: Integrates web automation and image analysis to solve CAPTCHAs efficiently.

## Installation

To get started with GENAPTCHA, follow these steps:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/nassiramn/Genaptcha.git
   cd Genaptcha
   ```

2. **Install the required dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   - Rename the `.env.example` file to `.env`.
   - Add your Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - You can obtain the Gemini API key from [Google AI Studio](https://aistudio.google.com/).

4. **Download ChromeDriver**:
   Download the ChromeDriver executable from [here](https://googlechromelabs.github.io/chrome-for-testing/) by choosing the appropriate version for your operating system. Place it in your project directory and update the `chrome_driver_path` variable in the script if necessary.

## Usage

To run the GENAPTCHA, execute the following command:

```sh
python main.py
```

The script will navigate to Amazon, capture the CAPTCHA image, extract the text using the Gemini model, and attempt to solve the CAPTCHA.

Keep in mind: Amazon.com may not display the CAPTCHA on the first try. To see the program in action, you may need to re-run it multiple times.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any inquiries or support, please contact me at git.nassir@gmail.com.
