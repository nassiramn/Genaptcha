"""
GENAPTCHA: Proof-of-Concept for solving Amazon CAPTCHAs using Generative AI

This script automates solving Amazon's CAPTCHA using Selenium for web automation 
and Google's Gemini 1.5 Pro model for image analysis and text extraction.

Author: Nassir
Project: GENAPTCHA
"""

import os
import time

import google.generativeai as genai
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Constants
SCREENSHOT_PATH = "captcha_screenshot.png"
TARGET_URL = "https://www.amazon.com/"
TEXT_FIELD_ELEMENT_LOCATOR = (By.CLASS_NAME, "a-span12")
WAIT_TIMEOUT = 10

class AmazonCaptchaSolver:
    """
    Encapsulates the logic for solving Amazon CAPTCHAs using Gemini.
    """

    def __init__(self, gemini_api_key: str, chrome_driver_path: str):
        """
        Initializes the CAPTCHA solver with API key and sets up Selenium WebDriver.

        Args:
            gemini_api_key (str): API key for Google's Gemini model.
            chrome_driver_path (str): Path to the ChromeDriver executable.
        """
        self.gemini_api_key = gemini_api_key
        self.chrome_driver_path = chrome_driver_path
        self.driver = None
        self.model = None
        self._setup_gemini()
        self._setup_selenium()

    def _setup_gemini(self):
        """Configures the Gemini API and initializes the generative model."""
        genai.configure(api_key=self.gemini_api_key)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro")

    def _setup_selenium(self):
        """Sets up the Selenium WebDriver for Chrome."""
        service = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def navigate_to_page(self, url: str):
        """Navigates to a specified URL."""
        self.driver.get(url)
        self.driver.maximize_window()

    def _wait_for_element(self, locator: tuple, timeout: int = WAIT_TIMEOUT) -> bool:
        """Waits for a specific element to be present on the page.

        Args:
            locator (tuple): Locator strategy (e.g., By.ID, By.CLASS_NAME) and the value.
            timeout (int): Maximum time to wait for the element.

        Returns:
            bool: True if the element is found within the timeout, False otherwise.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            print(f"Element with locator '{locator}' not found within {timeout} seconds.")
            return False

    def capture_captcha(self, screenshot_path: str = SCREENSHOT_PATH) -> Image:
        """
        Captures a screenshot of the current page and saves it.

        Args:
            screenshot_path (str): Path to save the screenshot.

        Returns:
            Image: The captured screenshot as a PIL Image object.
        """
        self.driver.save_screenshot(screenshot_path)
        screenshot = Image.open(screenshot_path)
        return screenshot

    def extract_captcha_text(self, image: Image) -> str:
        """
        Extracts CAPTCHA text from an image using the Gemini model.

        Args:
            image (Image): The PIL Image containing the CAPTCHA.

        Returns:
            str: The extracted CAPTCHA text.
        """
        prompt = (
            "Analyze the image to identify and extract the alphanumeric "
            "characters present in the CAPTCHA. Ignore any background "
            "elements, noise, or distortions. Return only the extracted "
            "text, ensuring accuracy and clarity."
        )
        response = self.model.generate_content([prompt, image])
        return response.text.strip()

    def solve_captcha(self):
        """
        Organizes the process of navigating to Amazon, capturing, 
        extracting, and solving the CAPTCHA.
        """
        try:
            self.navigate_to_page(TARGET_URL)

            if not self._wait_for_element(TEXT_FIELD_ELEMENT_LOCATOR):
                return

            captcha_image = self.capture_captcha()
            captcha_text = self.extract_captcha_text(captcha_image)

            input_element = self.driver.find_element(*TEXT_FIELD_ELEMENT_LOCATOR)
            input_element.send_keys(captcha_text)
            input_element.send_keys(Keys.ENTER)

            print(f"The extracted CAPTCHA is: {captcha_text}")

            # Keep the browser open for observation
            time.sleep(10)

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if self.driver:
                self.driver.quit()

def main():
    """
    Main function to execute the Amazon CAPTCHA solver.
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("Environment variable GEMINI_API_KEY is not set.")
    chrome_driver_path = "chromedriver.exe"

    solver = AmazonCaptchaSolver(gemini_api_key, chrome_driver_path)
    solver.solve_captcha()

if __name__ == "__main__":
    main()