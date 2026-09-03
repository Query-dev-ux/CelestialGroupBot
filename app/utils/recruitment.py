"""Submits an inbound Telegram application to Recruitment Service —
POST /telegram/applications, see RecruitmentService's
docs/API_INTEGRATION.md for the full contract.

Optional and best-effort by design: if RECRUITMENT_SERVICE_URL/TOKEN aren't
configured, or the request fails for any reason, this only logs. The
existing forward to HR_GROUP_ID (utils/hr.py) is the bot's real,
unconditional behavior and must never be blocked or delayed by a
Recruitment Service hiccup.
"""

import logging
from typing import Optional

import httpx

from app.config import settings

logger = logging.getLogger(__name__)


async def submit_telegram_application(
    *,
    telegram_user_id: int,
    telegram_full_name: Optional[str] = None,
    telegram_username: Optional[str] = None,
    vacancy_ref: Optional[str],
    candidate_text: Optional[str],
    resume_file_ref: Optional[str],
) -> None:
    if not settings.RECRUITMENT_SERVICE_URL or not settings.RECRUITMENT_SERVICE_TOKEN:
        logger.info("RECRUITMENT_SERVICE_URL/TOKEN not configured — skipping submission")
        return

    payload = {
        "telegram_user_id": telegram_user_id,
        "telegram_full_name": telegram_full_name,
        "telegram_username": telegram_username,
        "vacancy_ref": vacancy_ref,
        "candidate_text": candidate_text,
        "resume_file_ref": resume_file_ref,
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                f"{settings.RECRUITMENT_SERVICE_URL.rstrip('/')}/telegram/applications",
                json=payload,
                headers={"Authorization": f"Bearer {settings.RECRUITMENT_SERVICE_TOKEN}"},
            )
            response.raise_for_status()
    except Exception:
        logger.exception("Failed to submit Telegram application to Recruitment Service")
