from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

restaurant_info = """
You are a helpful assistant for Bella Italia Restaurant.

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

print("Bella Italia Restaurant Chatbot")
print("Type 'quit' to exit")
print("-" * 40)

conversation = [{"role": "system", "content": restaurant_info}]

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break
    
    conversation.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation
    )
    
    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})
    
    print(f"Bot: {reply}\n")