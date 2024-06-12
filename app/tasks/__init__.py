# Импорты ниже необходимы для корректной работы celery beat
# так как celery не загружает файл main.py, который импортирует все модули
# приложения.
from app.hotels.models import Hotels  # noqa
from app.hotels.rooms.models import Rooms  # noqa
from app.bookings.models import Bookings  # noqa
from app.users.models import Users  # noqa
