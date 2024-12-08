from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os




# Set TensorFlow environment variable to disable oneDNN optimizations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Initialize FastAPI app
app = FastAPI()

# CORS Configuration
origins = [
    "http://localhost:5173",  # React frontend
    "http://localhost:8000",  # FastAPI backend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the model path and validate it
MODEL_PATH = r"D:\Potato Disease Analysis\backend\saved_model\staple_crops_model.keras"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# Load the trained model
MODEL = tf.keras.models.load_model(MODEL_PATH)

# Define class names
CLASS_NAMES = [
    'Potato__bacterial_wilt',
    'Potato_early_blight',
    'Potato_healthy',
    'Potato_late_blight',
    'Potato_nematode',
    'Potato_pests',
    'Potato_phytophthora',
    'Potato__virus'
]

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Potato Disease Analysis API!"}

# Health Check Endpoint
@app.get("/ping")
async def ping():
    return {"message": "Server is alive and ready!"}

# Image Processing Function
def read_file_as_image(data: bytes) -> np.ndarray:
    try:
        image = Image.open(BytesIO(data))
        image = image.resize((224, 224))  # Adjust size based on model's expected input
        return np.array(image)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")

# Prediction Endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and process the uploaded image
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, 0)  # Expand dimensions for batch processing
        
        # Normalize the image to match training preprocessing
        #img_batch = img_batch / 255.0  # Normalize to [0, 1] range
        
        # Make prediction using the loaded model
        predictions = MODEL.predict(img_batch)
      
        predicted_index = np.argmax(predictions[0])
        print(predicted_index)
        predicted_class = CLASS_NAMES[predicted_index]
        confidence = float(np.max(predictions[0]))
        
        # Return the prediction result
        return {
            'class': predicted_class,
            'confidence': confidence
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
