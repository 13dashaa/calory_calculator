# Calorie Calculator Telegram Bot

A Python-based Telegram bot designed to help users calculate their daily calorie intake and macro-nutrient (PFC) requirements based on personal metrics and fitness goals. It also provides informative lists of food products categorized by their main nutrients.

## 🌟 Features

*   **Calorie and BMR Calculation:** Calculates your Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE) using standard formulas, incorporating age, height, weight, and gender.
*   **Goal-Oriented Recommendations:** Provides a recommended calorie range and macro-nutrient split (Protein, Fat, Carbohydrates) for three primary goals:
    *   Weight Loss
    *   Muscle Gain
    *   Maintenance
*   **Activity Level Adjustment:** Incorporates various activity coefficients to accurately estimate TDEE.
*   **Nutrient Information:** Offers interactive lists of foods rich in Protein, Fats, and Carbohydrates.
*   **Interactive Interface:** Uses inline keyboards for a smooth and intuitive user experience.

## 🚀 Technologies

*   **Python 3.x**
*   **`pyTelegramBotAPI`** (imported as `telebot`)

## ⚙️ Setup and Installation

### Prerequisites

1.  **Python 3** installed on your system.
2.  A **Telegram Bot Token** obtained from BotFather.

### Steps

1.  **Clone the repository:**

    ```bash
    git clone <your_repo_link>
    cd calorie-calculator-bot
    ```

2.  **Install dependencies:**

    ```bash
    pip install pyTelegramBotAPI
    ```

3.  **Configure the Bot Token:**

    Open the `main.py` file and replace the placeholder with your actual Telegram Bot Token:

    ```python
    # main.py
    bot = telebot.TeleBot("YOUR_BOT_TOKEN_HERE")
    ```

4.  **Ensure required files exist:**

    The project relies on external files for functionality and resources:
    *   `functions.py` (which contains `load_message` and potentially other helper functions).
    *   A `resourses/images/` directory containing images (`protein.jpg`, `fats.jpg`, `carbs.jpg`).
    *   External files used by `load_message` for nutrient text data.

5.  **Run the bot:**

    ```bash
    python main.py
    ```

## 🤖 Usage

Start a chat with your bot on Telegram and use the following commands or inline buttons:

| Command | Description |
| :--- | :--- |
| `/start` | Greets the user and presents initial options (Calculate Calories or Nutrient Info). |
| `/calorie` | Initiates the calorie calculation process (prompts for Age, Height, etc.). |
| `/products` | Displays options to view nutrient information (Protein, Fats, Carbs). |

### Calorie Calculation Flow:

1.  Start the bot (`/start`).
2.  Select **'Рассчитать калорийность рациона'**.
3.  Enter **Age** (years).
4.  Enter **Height** (cm).
5.  Enter **Weight** (kg).
6.  Select **Gender** (Male/Female).
7.  Select **Activity Level**.
8.  Select **Goal** (Weight Loss, Muscle Gain, Maintenance).
9.  The bot outputs your BMR, TDEE, target calorie range, and recommended macro-nutrient ranges.

---
*(Note: The code uses Russian prompts and variable names. Ensure your `functions.py` and resource files are set up to match the expected structure, especially for the nutrient information feature.)*
