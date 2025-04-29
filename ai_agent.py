import requests
import json
import os

# Load knowledge base
def load_knowledge_base():
    if os.path.exists("knowledge_base.json"):
        with open("knowledge_base.json", "r") as file:
            return json.load(file)
    else:
        return {}

knowledge_base = load_knowledge_base()

def simulate_call(customer_name, customer_question):
    print(f"\n📞 Incoming call from {customer_name}: {customer_question}")
    
    if customer_question in knowledge_base:
        print(f"🤖 AI Agent Response: {knowledge_base[customer_question]}")
    else:
        # ✅ The host-style response
        print("🤖 AI Agent: Let me check with my supervisor and get back to you.")
        print(f"📩 Text to Supervisor: Hey, I need help answering — '{customer_question}'")

        payload = {
            "customer_name": customer_name,
            "question": customer_question
        }
        try:
            response = requests.post("http://127.0.0.1:8000/request_help/", json=payload)
            if response.status_code == 200:
                print("✅ Help request submitted successfully!")
            else:
                print(f"❌ Failed to submit help request. Status code: {response.status_code}")
        except Exception as e:
            print(f"❌ Error submitting request: {e}")

if __name__ == "__main__":
    simulate_call("Jane Smith", "What are your working hours?")
    simulate_call("John Doe", "Do you offer threading services?")
