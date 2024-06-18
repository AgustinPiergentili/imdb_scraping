from textblob import TextBlob
from scrapear import Scrapear


class Sentimiento(Scrapear):

    @staticmethod
    def analizar_sentimiento(texto):
        """Analiza el sentimiento de un texto y devuelve un valor numérico"""
        blob = TextBlob(texto)
        sentimiento = blob.sentiment.polarity
        if sentimiento > 0:
            return 1  # positivo
        elif sentimiento < 0:
            return -1  # negativo
        else:
            return 0  # neutro