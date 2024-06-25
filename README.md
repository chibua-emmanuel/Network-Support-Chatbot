# Network-Support-Chatbot

This repository contains a Streamlit-based web application for a network support chatbot, created by Emmanuel Chibua. The chatbot is designed to assist with network-related queries, specifically focusing on Cisco and Mikrotik devices. It leverages the Llama3 language model using the Ollama API for natural language processing.

## Table of Contents
- [Network Support Chatbot](#network-support-chatbot)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Usage](#usage)
  - [Customization](#customization)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Features

- **Expertise in Networks**: The chatbot is a subject matter expert in networks, particularly Cisco and Mikrotik devices.
- **Interactive UI**: A user-friendly interface built with Streamlit.
- **Real-time Chat**: Provides instant responses to user queries.
- **Conversation History**: Displays the chat history for easy reference.
- **Styled Interface**: Custom styling for a professional look.

## Installation

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/network-support-chatbot.git
    cd network-support-chatbot
    ```

2. **Install the required packages**:
    ```sh
    pip install streamlit ollama
    ```

3. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

## Usage

1. **Start the application**:
    ```sh
    streamlit run app.py
    ```

2. **Interact with the chatbot**:
    - Enter your network-related query in the input box.
    - Press `Enter` or click the `Submit` button to send your query.
    - View the chatbot's response and the conversation history.

## Customization

You can customize the chatbot's appearance and behavior by modifying the following sections in the `app.py` file:

- **Model Definition**: Adjust the model creation script in the `modelfile` variable.
- **Styling**: Update the CSS styles in the `page_style` variable.
- **Banner and Footer**: Edit the HTML in the `st.markdown` calls for the banner and footer.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch**:
    ```sh
    git checkout -b feature-branch
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```sh
    git commit -m 'Add some feature'
    ```
5. **Push to the branch**:
    ```sh
    git push origin feature-branch
    ```
6. **Open a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the web framework.
- [Ollama](https://ollama.com/) for the language model API.
- Emmanuel Chibua for creating this application.
