import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import requests
import os

# Placeholder function for ChatGPT integration
def generate_recommendation(predicted_disease):
    # Simulated function to generate treatment recommendation
    recommendations = {
        'Coccidiosis': 'Provide antiparasitic medication and ensure proper hygiene and nutrition.',
        'Healthy': 'No specific treatment needed. Maintain proper care and nutrition.'
    }
    return recommendations.get(predicted_disease, 'No specific recommendation found.')

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # Load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
        else:
            prediction = 'Coccidiosis'
        
        return prediction
    
    def get_recommendation(self):
        predicted_disease = self.predict()
        
        # Integrate with ChatGPT API for recommendation
        recommendation = self.generate_recommendation_chatgpt(predicted_disease)
        
        return recommendation
    
    def generate_recommendation_chatgpt(self, predicted_disease):
        # Simulate calling ChatGPT API (replace with actual API call)
        # Example API endpoint (replace with your actual endpoint)
        api_endpoint = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": f"I have been diagnosed with {predicted_disease}. What treatment do you recommend?"}
            ]
        }
        
        response = requests.post(api_endpoint, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            recommendation = data["choices"][0]["message"]["content"]
        else:
            recommendation = "No specific recommendation found from the sources."
        
        return recommendation

