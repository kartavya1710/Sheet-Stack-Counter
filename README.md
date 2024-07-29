

---

# Automated Sheet Stack Counter 📊

This project is a web application that automatically counts the number of sheets in a stack using computer vision techniques. Built with Streamlit, the app provides an easy-to-use interface for users to upload images of sheet stacks and receive an estimated sheet count.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features
- **Image Upload**: Users can upload images in various formats (JPG, JPEG, PNG).
- **Image Processing**: The application processes the image using edge detection and line detection techniques.
- **Sheet Counting**: Estimates the number of sheets in the stack based on detected lines.
- **Visualization**: Displays the processed image with detected lines and a bar chart visualization.
- **Confidence Metric**: Provides a simple confidence metric for the estimated sheet count.

## Installation

### Prerequisites
- Python 3.7 or higher
- [Streamlit](https://streamlit.io)
- [OpenCV](https://opencv.org)
- [Pillow](https://python-pillow.org)

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/sheet-stack-counter.git
   cd sheet-stack-counter
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run sheet_counter_app.py
   ```

## Usage

1. **Upload an Image**: Click on the file uploader and select an image of a sheet stack.
2. **Process the Image**: Click the "Process Image" button to analyze the uploaded image.
3. **View Results**: The app will display the processed image with detected lines, the estimated number of sheets, and a confidence metric.

## Project Structure

- `app.py`: Main application code.
- `README.md`: Project documentation.
- `requirements.txt`: Python dependencies.

## Acknowledgements

This project utilizes the following libraries and tools:

- [Streamlit](https://streamlit.io): For building the web application.
- [OpenCV](https://opencv.org): For image processing.
- [Pillow](https://python-pillow.org): For handling image files.


---
