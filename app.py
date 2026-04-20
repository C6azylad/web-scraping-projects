from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

restaurant_info = """
You are a helpful assistant for Bella Italia Restaurant.
Only answer questions related to the restaurant.
If someone asks something unrelated, politely say you can only help with restaurant related questions.

Business Information:
- Name: Bella Italia Restaurant
- Location: 123 Main Street, Kochi, Kerala
- Opening Hours: Monday to Sunday, 11 AM to 11 PM
- Phone: +91 98765 43210
- Speciality: Authentic Italian cuisine
- Popular dishes: Margherita Pizza, Pasta Carbonara, Tiramisu
- Reservations: Available by phone or walk-in
- Delivery: Available through Swiggy and Zomato
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": restaurant_info},
            {"role": "user", "content": user_message}
        ]
    )
    
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)