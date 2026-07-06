from app.domain.entities import Image


class HandleImageProcessedEvent:
    def __init__(self, cash_repository):
        self.cash_repository = cash_repository

    def execute(self, image:Image) -> Image:pass
        #Здесь прсото кладете фотку в кеш и пока все




