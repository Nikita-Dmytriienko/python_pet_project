from google import genai

from config import config_obj

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=config_obj.gemini_api_key)

def main():
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    )
    print(response.text)

if __name__ == '__main__':
    main()



