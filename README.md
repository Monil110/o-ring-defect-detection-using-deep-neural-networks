# O-Ring Defect Detection

An AI-powered quality control application designed to detect defects in O-rings using advanced computer vision models. This project utilizes a modern web interface to allow users to upload images or use a live camera for real-time defect detection.

## 🚀 Features

*   **Dual Model Architecture:**
    *   **CNN Model:** A Convolutional Neural Network trained to classify O-rings as "Good" or having "Breakage".
    *   **YOLO Model:** A YOLOv8 object detection model specialized in detecting specific defects like "Paregi" (Extrusion) and "Pelise" (Intrusion).
*   **Modern Web Interface:** A responsive, animated UI built with FastHTML and custom CSS for a premium user experience.
*   **Live Camera Integration:**
    *   Capture images directly from your device's camera.
    *   **Smart Capture:** Uses OpenCV.js in the browser to automatically detect the presence of an O-ring (using Hough Circle Transform) before capturing and sending the frame for analysis.
*   **Real-time Analysis:** Instant feedback with prediction results and confidence scores.

## 🛠️ Tech Stack

*   **Frontend & Backend:** [FastHTML](https://fastht.ml/) (Python)
*   **Deep Learning Models:**
    *   CNN (Custom Architecture)
    *   YOLOv8 (Ultralytics)
*   **Deployment:** Models are deployed as APIs on [Render](https://render.com/).
    *   CNN API: `https://oring.onrender.com/predict`
    *   YOLO API: `https://oring-2.onrender.com/predict`
*   **Libraries:** `requests`, `opencv-python` (backend logic), `opencv.js` (frontend processing).

## 📂 Project Structure

*   `main.py`: The core application file containing:
    *   **FastHTML App:** Defines the routes and serves the HTML/CSS/JS.
    *   **UI Logic:** Custom CSS animations and JavaScript for file handling and camera interaction.
    *   **API Proxy:** The `/predict` endpoint that forwards images to the respective Render model APIs (CNN or YOLO) and returns the formatted results.

## 🏁 Getting Started

### Prerequisites

*   Python 3.x
*   `fasthtml`
*   `requests`

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  Install dependencies:
    ```bash
    pip install python-fasthtml requests
    ```

### Running the Application

1.  Start the FastHTML server:
    ```bash
    python main.py
    ```

2.  Open your web browser and navigate to the local server address (usually `http://localhost:5001` or similar, check the terminal output).

## 💡 How to Use

1.  **Select Model:** Choose between the **CNN Model** (for general breakage) or **YOLO Model** (for extrusion/intrusion) using the cards on the right.
2.  **Upload or Capture:**
    *   **Upload:** Drag and drop an image or click "Browse" to select a file.
    *   **Camera:** Click "Capture Live" to open the camera stream. The system will auto-capture when an O-ring is detected.
3.  **Analyze:** Click the "Analyze Image" button.
4.  **View Results:** The prediction (e.g., "Good", "Breakage", "Paregi") and confidence score will appear below.

## 🔌 API Reference

The application acts as a client to two external APIs:

*   **POST /predict (Local):** Receives the image and model selection.
    *   Params: `file` (image), `model` ('cnn' or 'yolo')
*   **External Model APIs:**
    *   **CNN:** `POST https://oring.onrender.com/predict`
    *   **YOLO:** `POST https://oring-2.onrender.com/predict`

## 📝 License

This project is open-source and available for educational and commercial quality control purposes.
