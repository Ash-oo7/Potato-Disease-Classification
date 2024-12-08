# Potato Disease Classification 🌱

A deep learning project designed to classify potato leaf diseases, offering an efficient tool for farmers and agricultural experts to diagnose and manage crop health.

## Key Highlights

- **Objective**: Detect and classify potato leaf diseases into the following categories:  
  - Healthy  
  - Late Blight  
  - Early Blight  
  - Bacterial Wilt  
  - Nematode  
  - Pests  
  - Virus  
  - Phytophthora  
- **Model**: Built using the **EfficientNetB0** architecture, known for its balance of speed and accuracy.  
- **Backend**: Deployed with **FastAPI**, ensuring fast, reliable API responses for real-time disease detection.  
- **Frontend**: A dynamic and responsive web interface built using **React.js**, allowing users to upload leaf images effortlessly.  
- **Deployment**: The trained model is saved in `.keras` format and seamlessly integrated into the backend for predictions.

## Features

- **Image Upload**: Users can upload images of potato leaves through an intuitive web interface.  
- **Real-Time Predictions**: Provides disease classification results instantly upon submission.  
- **Modular Architecture**: The project's design ensures scalability and easy integration with additional datasets or models.  
- **Agricultural Impact**: Helps farmers identify diseases early, preventing crop loss and improving yield.

## Dataset

**Dataset Link**: [Plant Diseases Training Dataset on Kaggle](https://www.kaggle.com/datasets/nirmalsankalana/plant-diseases-training-dataset/data)

## Why This Project?

- **Real-World Application**: Addresses a common agricultural challenge using AI-driven solutions.  
- **Scalable & Efficient**: Combines state-of-the-art machine learning with modern web technologies for a seamless user experience.  
- **Future Potential**: Forms a foundation for advanced applications, such as real-time field diagnosis or drone-based monitoring.

## How to Run Locally 🚀

### 1. Clone the Repository
```bash
git clone https://github.com/Ash-oo7/Potato-Disease-Classification.git
cd Potato-Disease-Classification
```

### 2. Set Up the Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Set Up the Frontend
```bash
cd ../frontend
npm install
npm start
```


### 4. Upload a Leaf Image
- Open your browser and navigate to `http://localhost:3000`
- Use the interface to upload an image of a potato leaf
- View the disease classification result in real-time


## Example Output

<img width="576" alt="Screenshot 2024-12-03 at 1 15 38 PM" src="https://github.com/user-attachments/assets/e878a3aa-5b55-43f3-a0dc-9ae04901597d">
