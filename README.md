# VikiWebsiteAutomation

This project aims at automation on the series streaming website Viki.com. Coded with Python and Selenium.

In this automation, the goal is extract the names of korean series published by Viki platform. For this, is need do login on Viki website and filter the series list by "TV" in format, "Korea" in country and "Popular-all time" in order list. Done this filter so, is possible to extract the names of series in the current page, and doing this until not exist more next page for enter in.

# Prerequisite

As prerequisite for executing the script is necessary have installed the Firefox browser in latest version and others technologies mentioned below:

* Mozilla Firefox Browser
* Windows PowerShell 5.1
* Python 3.10
* Selenium WebDriver
* WebDriver do navegador

# Dependencies installation

* ###### Mozilla Firefox Browser:

  To install the Mozilla Firefox browser follow the steps in this link:

  [How to install Firefox on Windows | Firefox Help (mozilla.org)](https://support.mozilla.org/en-US/kb/how-install-firefox-windows)
* ###### Windows PowerShell:

  Windows PowerShell comes installed by default in every Windows, starting with Windows 7 SP1 and Windows Server 2008 R2 SP1.
  To check the version of Windows PowerShell, search it in Windows menu and type the follow command inside Windows PowerShell:

  ``$Host``

  This command display some informations about the current instance of terminal. Check the version and see if it is equal or superior to informed in this project. If not, follow the steps in this link:

  [Installing Windows PowerShell - PowerShell | Microsoft Docs
  ](https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/install/installing-windows-powershell?view=powershell-5.1)
* ###### Python

  To install Python 3 follow the steps in this link below:

  [Python Brasil-Instalando o Python 3 no Windows
  ](https://python.org.br/instalacao-windows/#:~:text=O%20processo%20de%20instala%C3%A7%C3%A3o%20%C3%A9%20bem%20simples.%201.,--version.%20Este%20comando%20retornar%C3%A1%20a%20vers%C3%A3o%20do%20)
* ###### SeleniumWebDriver and WebDriver do navegador

  **To intall the Selenium WebDriver follow the steps in this link below:**

  [Install a Selenium library | Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)

  **To install WebDriver of browser follow the steps in this link below:**

  [Install browser drivers | Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

# Executing the script

1. Clone or download and extract this project in any directory of your preference
2. Open Windows PowerShell in this cloned or downloaded directory path
3. Copy and paste the code sequence below into Windows PowerShell and press Enter for each command

``python -m venv venv``

``& ./venv/Scripts/Activate.ps1``

``python -m pip install -r requirements.txt``

4. Execute the command below to effectively run the script in production

``python .\main.py``

at the end of the process will be generated a log as stated in the documentation of this project. You can obtain the process details, logs and more accessing the documentation folder in this project.

# Authors

Allan de Oliveira Almeida
