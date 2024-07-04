# Personalized Skin Care Routine App with Image Annotation

## Overview

This repository contains a Streamlit-based web application that offers personalized skin care recommendations. The app uses machine learning to detect skin problems from a user's uploaded selfie and provides a tailored skin care routine based on detected issues and user input.

## Features

- **Image Upload**: Users can upload a selfie to the application.
- **Skin Problems Detection**: The app uses the Roboflow API to detect skin problems in the uploaded image.
- **Image Annotation**: Detected skin problems are annotated on the image and displayed back to the user.
- **Personalized Recommendations**: Users receive a customized skin care routine and product recommendations based on their skin type and concerns.

## Technologies Used

### Streamlit

Streamlit is an open-source app framework used to create interactive web applications in Python. It's particularly well-suited for data science and machine learning applications.

### Roboflow

Roboflow is a computer vision platform that provides APIs to manage and deploy custom models. In this app, Roboflow is used to detect skin problems in user-uploaded images.

### Supervision

Supervision is a Python library used for visualizing machine learning model outputs. It is used here for annotating the detected skin problems on the uploaded image.

### OpenCV

OpenCV (Open Source Computer Vision Library) is a powerful library for computer vision tasks. It's used in this application to process and display images.

### NumPy

NumPy is a fundamental package for numerical computation in Python. It is used for array manipulations and handling image data.

## How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/skin-care-app.git
    cd skin-care-app
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    streamlit run skin.py --server.enableXsrfProtection false
    ```

4. **Upload a selfie**: Once the app is running, upload a selfie to get started.

### Expected behaviour 

![Test-image](https://github.com/SonaLakhotia/CareForSkin-SkinPals/assets/169345257/ecaaa424-87ef-4bb7-84b1-69afa8fbfd0b)
![Test-Result](https://github.com/SonaLakhotia/CareForSkin-SkinPals/assets/169345257/48f72eca-7618-441f-8bb5-e710b90356f0)


5. **Get recommendations**: Select your skin type and concerns to receive a personalized skin care routine and product recommendations.

## Custom Knowledge Base Chatbot

This application includes a chatbot trained on a custom knowledge base using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs). RAG combines the power of retrieval systems with generative models to provide more accurate and contextually relevant responses.

### Key Technologies in Generative AI and LLMs

- **Retrieval-Augmented Generation (RAG)**: RAG is a technique that enhances the capabilities of generative models by retrieving relevant documents or information from a knowledge base before generating a response. This approach helps in providing more accurate and informative answers.
  
- **Large Language Models (LLMs)**: LLMs, such as GPT-4, are trained on vast amounts of text data to understand and generate human-like text. These models can perform a variety of natural language processing tasks, including text generation, summarization, translation, and question-answering.

- **Working chatbot**: https://www.coze.com/store/bot/7385888784694427653?panel=1

## Code Structure

- `app.py, skin.py`: The main application file that contains the Streamlit app code.
- `requirements.txt`: A list of Python dependencies required to run the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

