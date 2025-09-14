from __future__ import annotations

from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class ItemBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Item ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    name: str = Field(
        ...,
        description="Item name.",
        json_schema_extra={"example": "Apple"},
    )
    brand: str = Field(
        ...,
        description="Brand of item.",
        json_schema_extra={"example": "AAA"},
    )
    production_date: datetime = Field(
        None,
        description="The production date of item.",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    expiration_date: datetime = Field(
        None,
        description="The expiration date of item.",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "660e8400-e29b-41d4-a716-446655440111",
                    "name": "Milk",
                    "brand": "DairyBest",
                    "production_date": "2025-02-01T09:00:00Z",
                    "expiration_date": "2025-02-10T09:00:00Z",
                }
            ]
        }
    }
