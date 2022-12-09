from enum import Enum

class StatusPartida(Enum):
    AGUARDANDO_INICIO = 1
    FINALIZADO = 2
    SEU_TURNO_EM_ANDAMENTO = 3
    NOT_SEU_TURNO_EM_ANDAMENTO = 5
    DESISTENCIA = 6
