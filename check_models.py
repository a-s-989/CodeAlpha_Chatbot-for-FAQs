import google.generativeai as genai

# Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyA11lO9v35eidQ5y3foEMKWnWf-H8AlPvQ")

models = genai.list_models()

print("Available models:")
for model in models:
    print(model.name)
