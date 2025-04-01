# TestGenie: AI-Powered Test Automation

TestGenie is an AI-driven test automation framework that automatically **generates test cases** using GPT-4 and **executes them** with Selenium. It significantly reduces manual effort in test case creation and enhances software testing efficiency.

## 🚀 Features

- **AI-Powered Test Case Generation** - Uses GPT-4 to generate detailed test cases.
- **Automated Web Testing** - Executes generated test cases using Selenium.
- **Reduces Manual Effort** - Automates test writing and execution for faster testing cycles.

---

## 📌 Installation

Ensure you have **Python 3.7+** installed on your system.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/TestGenie.git
cd TestGenie
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up OpenAI API Key

You need an API key from OpenAI to generate test cases.

1. Go to [OpenAI](https://openai.com/) and create an account.
2. Get your **API Key** from the API section.
3. Set it up in your environment:
   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

---

## 📜 How It Works

### **Step 1: Generate AI Test Cases**

Run the AI test case generator:

```bash
python test_generator.py
```

#### **Example Output:**

```
Test Case 1: Login with valid credentials
- Open the login page.
- Enter a valid email and password.
- Click the "Login" button.
- Verify that the user is redirected to the dashboard.
```

---

### **Step 2: Run Automated Selenium Tests**

Make sure you have **Google Chrome** and the [Chrome WebDriver](https://sites.google.com/chromium.org/driver/) installed.

Run the Selenium test script:

```bash
python test_executor.py
```

#### **What Happens?**

- Opens a web browser.
- Enters test credentials.
- Clicks the login button.
- Verifies if login was successful or failed.

---

## 🛠 Configuration

Modify `test_generator.py` to change the input requirements for test case generation. Modify `test_executor.py` to add new test cases and website interactions.

---

## ⚡ Example Use Cases

- **Automate repetitive test case writing.**
- **Validate web application functionality efficiently.**
- **Enhance AI-powered automation in software testing.**

---

## 🌟 Contributions

Want to contribute? Feel free to fork the repository and submit a pull request!

---

## 📧 Contact

For questions or collaboration, reach out at [**your.email@example.com**](mailto\:your.email@example.com)

---

🚀 **Happy Testing with TestGenie!** 🎩✨

