from app.config.settings import load_environment
from app.http.session import HttpSession
from app.articles.processor import ArticleProcessor
from app.summarization.summarizer import Summarizer
from pprint import pprint


def main():
    load_environment()
    http_session = HttpSession()
    article_processor = ArticleProcessor(http_session=http_session)
    latest_articles = article_processor.process_articles()
    for article in latest_articles:
        summarizer = Summarizer()
        template = """Your are an advanced AI assistant that summarizes the given articles and
        translate them to {language} language, making the necessary adjustments.
         
        Here is the article you need to summarize:
        Title: {article_title}
        Text: {article_text}

        Provide a summarized version of the article in a bulleted list format of max 5 bullets in {language}.
        Important, add the article title to your answer.
        """
        summary = summarizer.summarize(
            article_title=article.title, article_text=article.text, template=template, language='brazilian portuguese')
        pprint(summary.cont)
        print("===========================================================================")
        print("===========================================================================")


if __name__ == '__main__':
    main()
