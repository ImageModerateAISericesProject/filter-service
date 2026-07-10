class ProcessImageUseCase:
    def __init__(self, cash_repository, s3_repository, publisher):
        """Принимаем инфровые адаптеры, чтоб работать с ифрой не на прямую"""
        self.cash_repository = cash_repository
        self.s3_repository = s3_repository
        self.publisher = publisher

    def execute(self, image) -> int:
        pass
        # мне надо:
        # 1) проверить есть ли фотка в кеше
        # 2) елси есть - отдать
        # 3) елси нет, то положить в s3, в кафку(pending)
        # 4) в любом случае вернуть Image.id, чтоб потом через полинг его получить
        # ВАЖНО!!! я хочу получить от вас сущность Image
