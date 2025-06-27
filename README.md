# Gemini CLI

A simple, interactive command-line interface (CLI) to chat with Google's Gemini AI models directly from your terminal.

## Features

-   **Interactive Chat**: Engage in a continuous conversation with Gemini.
-   **Easy Setup**: Uses a `.env` file to securely manage your API key.
-   **Configurable Model**: Easily switch between different Gemini models.
-   **Error Handling**: Gracefully handles potential API errors during the conversation.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   A Google Gemini API Key. You can get one from Google AI Studio.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Candaka/gemini-cli.git
    cd gemini-cli
    ```

2.  **Create and activate a virtual environment (recommended):**
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    Create a file named `.env` in the project's root directory and add your API key:
    ```env
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## Usage

Once the setup is complete, run the script from your terminal:

```bash
python main.py
```

The script will start, and you can begin asking questions. To quit the application, simply type `exit`.

## Configuration

You can change the Gemini model by editing the `MODEL_NAME` constant at the top of the `main.py` file.