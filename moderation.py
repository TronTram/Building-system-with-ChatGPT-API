from dotenv import load_dotenv
import os
import openai

def main():
    load_dotenv()
    open_ai_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = open_ai_key
    print(open_ai_key)
    
  
if __name__ == '__main__':
    main()
