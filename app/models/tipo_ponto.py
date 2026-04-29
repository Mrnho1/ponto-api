from enum import Enum

class TipoPonto(str, Enum):
    ENTRADA = "ENTRADA"
    SAIDA_ALMOCO = "SAIDA_ALMOCO"
    VOLTA_ALMOCO = "VOLTA_ALMOCO"
    SAIDA = "SAIDA"