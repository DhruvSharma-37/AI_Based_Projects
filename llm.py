from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()

        # 👇 Yaha change kiya — 3 sentences summary
        summary = summarizer(parser.document, 3)

        result = ""
        for sentence in summary:
            result += str(sentence) + " "

        return result.strip()

    except Exception as e:
        return f"Error generating summary: {str(e)}"