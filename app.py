project_dir="/home/demo/Dropbox/notes/data/2A/A44402-0316-471F-A98C-C8AB2B1CC489/posts/data/2a/dc2abb-67fc-465a-8f90-586e0dc9d579"
import streamlit as st

def summarise(url: str, number_of_sentences: int, lang='english') -> tuple:
    from sumy.parsers.html import HtmlParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lsa import LsaSummarizer as Summarizer
    from sumy.nlp.stemmers import Stemmer
    from sumy.utils import get_stop_words
    
    try:
      parser = HtmlParser.from_url(url, Tokenizer(lang))
    except LookupError:
     # one-off resolution
     import nltk
     nltk.download("punkt")
     parser = HtmlParser.from_url(url, Tokenizer(lang))
     
    stemmer = Stemmer(lang)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(lang)
    return tuple(summarizer(parser.document, number_of_sentences))

def on_click(st, url, number_of_sentences):
    sentences = summarise(url, number_of_sentences)
    st.markdown('\n\n'.join((f'* {s}' for s in sentences)))
    
    
number_of_sentences = st.slider('Number of sentences', 0, 100, 10)

url_input = st.text_input(
    "Enter article URL to summarise",
    key="url_input",
    value="https://www.bbc.com/future/article/20210105-why-our-pursuit-of-happiness-may-be-flawed",
    max_chars=1024,
    type="default",
    placeholder=""
)

st.button("Get the main points", on_click=on_click, args=(st, url_input, number_of_sentences))
