from email.message import EmailMessage

from pydantic import EmailStr

from app.config import settings
from app.tasks.utils import plural_days


def create_booking_confirmation_template(
    booking: dict,
    email_to: EmailStr,
):
    email = EmailMessage()

    email["Subject"] = "Подтверждение бронирования"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Подтвердите бронирование</h1>
            Вы забронировали отель с {booking["date_from"]} по {booking["date_to"]}
        """,
        subtype="html"
    )
    return email


def create_booking_reminder_template(
    booking: dict,
    email_to: EmailStr,
    days: int,
):
    email = EmailMessage()

    days_str = plural_days(days)
    email["Subject"] = f"Осталось {days_str} до заселения"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Напоминание о бронировании</h1>
            Вы забронировали отель с {booking["date_from"]} по {booking["date_to"]}
        """,
        subtype="html"
    )
    return email
