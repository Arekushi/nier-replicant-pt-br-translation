import translators as ts
from tqdm import tqdm

from config import settings
from src.translator_engine import TranslatorEngine


class ConventionalTranslator(TranslatorEngine):
    def __init__(self):
        super().__init__()

    def init(self):
        ts.preaccelerate()
        tqdm.pandas()

    def _translate_single_file(self, file_path, df, columns_to_translate):
        for column in columns_to_translate:
            df[df.columns[column]] = df[df.columns[column]].progress_apply(self.translate_text)

        self.save_df(df, file_path)
        self.write_last_line(file_path)

    @staticmethod
    def translate_text(text) -> str:
        try:
            return ts.translate_html(
                from_language=settings.ARGS.source_language,
                to_language=settings.ARGS.target_language,
                translator=settings.TRANSLATOR.source,
                if_use_preacceleration=False,
                if_ignore_empty_query=True,
                html_text=text
            )
        except (ts.server.TranslatorError, TypeError):
            return str(text)
