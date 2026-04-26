# # # # import os
# # # # from dotenv import load_dotenv
# # # # from openai import OpenAI

# # # # # Load environment variables
# # # # load_dotenv()

# # # # # Get API key
# # # # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # # # # Initialize OpenAI client
# # # # client = OpenAI(api_key=OPENAI_API_KEY)


# # # # # 🎯 Professional Summarization Agent
# # # # def summarize_with_agent(text):
# # # #     try:
# # # #         prompt = f"""
# # # # You are a professional AI assistant specialized in summarizing educational and technical notes.

# # # # Your task:
# # # # - Read the given text carefully.
# # # # - Generate a clear, concise, and meaningful summary.
# # # # - Keep only the most important information.
# # # # - Remove repetition and unnecessary details.
# # # # - Maintain logical flow.
# # # # - Use simple and easy-to-understand language.
# # # # - If the text is long, summarize it into 4–6 meaningful sentences.
# # # # - Do NOT copy sentences directly — rephrase them intelligently.

# # # # Text to summarize:
# # # # {text}
# # # # """

# # # #         response = client.chat.completions.create(
# # # #             model="gpt-4.1-mini",
# # # #             messages=[
# # # #                 {
# # # #                     "role": "system",
# # # #                     "content": "You are an expert note summarization AI."
# # # #                 },
# # # #                 {
# # # #                     "role": "user",
# # # #                     "content": prompt
# # # #                 }
# # # #             ],
# # # #             temperature=0.3,
# # # #             max_tokens=300
# # # #         )

# # # #         summary = response.choices[0].message.content

# # # #         return summary

# # # #     except Exception as e:
# # # #         return f"Error generating summary: {str(e)}"



# # # import os
# # # from dotenv import load_dotenv
# # # from openai import OpenAI

# # # # Load env
# # # load_dotenv()

# # # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # # # OpenRouter client setup
# # # client = OpenAI(
# # #     api_key=OPENAI_API_KEY,
# # #     base_url="https://openrouter.ai/api/v1"
# # # )


# # # def summarize_with_agent(text):
# # #     try:

# # #         prompt = f"""
# # # You are a professional AI summarization assistant.

# # # Your job:
# # # - Read the full text carefully.
# # # - Generate a concise and meaningful summary.
# # # - Keep only the important information.
# # # - Remove repetition.
# # # - Use clear and simple language.
# # # - Write 4–6 sentences.
# # # - Do NOT copy sentences directly.
# # # - Rephrase intelligently.

# # # Text:
# # # {text}
# # # """

# # #         response = client.chat.completions.create(
# # #             model="mistralai/mistral-7b-instruct",

# # #             messages=[
# # #                 {
# # #                     "role": "system",
# # #                     "content": "You are an expert summarization assistant."
# # #                 },
# # #                 {
# # #                     "role": "user",
# # #                     "content": prompt
# # #                 }
# # #             ],

# # #             temperature=0.3,
# # #             max_tokens=300
# # #         )

# # #         summary = response.choices[0].message.content

# # #         return summary

# # #     except Exception as e:
# # #         return f"Error generating summary: {str(e)}"

# # import os
# # from dotenv import load_dotenv
# # from openai import OpenAI

# # # Load environment variables
# # load_dotenv()

# # # Get API key
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # # Debug check
# # if not OPENAI_API_KEY:
# #     raise ValueError("❌ OPENAI_API_KEY not found in .env file")

# # print("✅ API Key Loaded Successfully")

# # # OpenRouter client
# # client = OpenAI(
# #     api_key=OPENAI_API_KEY,
# #     base_url="https://openrouter.ai/api/v1"
# # )


# # def summarize_with_agent(text):
# #     try:

# #         response = client.chat.completions.create(
# #             model="openrouter/auto",

# #             messages=[
# #                 {
# #                     "role": "system",
# #                     "content": """
# # You are a professional AI assistant specialized in summarizing notes.

# # Instructions:
# # - Read the text carefully
# # - Generate a concise summary
# # - Remove repetition
# # - Keep important ideas
# # - Use simple language
# # - Write 4–6 meaningful sentences
# # """
# #                 },
# #                 {
# #                     "role": "user",
# #                     "content": text
# #                 }
# #             ],

# #             temperature=0.3,
# #             max_tokens=300
# #         )

# #         summary = response.choices[0].message.content

# #         return summary

# #     except Exception as e:
# #         return f"Error generating summary: {str(e)}"


# import os
# import requests
# from dotenv import load_dotenv

# # Load .env
# load_dotenv()

# # Get API key
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENAI_API_KEY:
#     raise ValueError("❌ OPENAI_API_KEY not found")

# print("✅ Free Model API Key Loaded")


# def summarize_with_agent(text):

#     try:

#         url = "https://openrouter.ai/api/v1/chat/completions"

#         headers = {
#             "Authorization": f"Bearer {OPENAI_API_KEY}",
#             "HTTP-Referer": "http://localhost:8000",
#             "X-Title": "AI Notes Summarizer",
#             "Content-Type": "application/json"
#         }

#         data = {
#             "model": "mistralai/mistral-7b-instruct:free",

#             "messages": [
#                 {
#                     "role": "system",
#                     "content": """
# You are a professional AI assistant specialized in summarizing notes.

# Rules:
# - Read the text carefully
# - Generate a concise summary
# - Remove repetition
# - Keep only important ideas
# - Use simple language
# - Write 4–6 meaningful sentences
# """
#                 },
#                 {
#                     "role": "user",
#                     "content": text
#                 }
#             ],

#             "temperature": 0.3,
#             "max_tokens": 300
#         }

#         response = requests.post(
#             url,
#             headers=headers,
#             json=data
#         )

#         result = response.json()

#         if "choices" in result:
#             summary = result["choices"][0]["message"]["content"]
#             return summary
#         else:
#             return f"Error generating summary: {result}"

#     except Exception as e:
#         return f"Error generating summary: {str(e)}"

import os
import requests
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Get API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found")

print("✅ OpenRouter API Key Loaded")


def summarize_with_agent(text):

    try:

        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "AI Notes Summarizer",
            "Content-Type": "application/json"
        }

        data = {
            # 🔥 Auto-select working model
            "model": "openrouter/auto",

            "messages": [
                {
                    "role": "system",
                    "content": """
You are a professional AI assistant specialized in summarizing notes.

Instructions:
- Read the full text carefully
- Generate a concise summary
- Remove repetition
- Keep important ideas
- Use simple language
- Write 4–6 meaningful sentences
"""
                },
                {
                    "role": "user",
                    "content": text
                }
            ],

            "temperature": 0.3,
            "max_tokens": 300
        }

        response = requests.post(
            url,
            headers=headers,
            json=data
        )

        result = response.json()

        # Debug print (important)
        print("API RESPONSE:", result)

        if "choices" in result:
            summary = result["choices"][0]["message"]["content"]
            return summary
        else:
            return f"Error generating summary: {result}"

    except Exception as e:
        return f"Error generating summary: {str(e)}"