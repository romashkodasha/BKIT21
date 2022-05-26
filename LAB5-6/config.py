from enum import Enum

# Токент бота
TOKEN = '5082279521:AAGZCqpuWDu2a0F1XMTVCcmdzSRwvaL9_1Y'

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"

SENTENCE = "SENTENCE"

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_FIRST = "STATE_FIRST"
    STATE_SECOND = "STATE_SECOND"
    STATE_THIRD = "STATE_THIRD"
    STATE_OPERATION = "STATE_OPERATION"
