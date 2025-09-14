from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4
from .person import PersonBase
from .items import ItemBase

class StoreBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Store ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    street: str = Field(
        ...,
        description="Street address and number.",
        json_schema_extra={"example": "123 Main St"},
    )
    city: str = Field(
        ...,
        description="City or locality.",
        json_schema_extra={"example": "New York"},
    )
    items: List[ItemBase] = Field(
        ...,
        description="Items in Store.",
    )
    workers: List[PersonBase] = Field(
        ...,
        description="Workers in Store.",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "street": "123 Main St",
                    "city": "New York",
                    "items": [
                        {
                            "id": "660e8400-e29b-41d4-a716-446655440111",
                            "name": "Milk",
                            "brand": "DairyBest",
                            "production_date": "2025-02-01T09:00:00Z",
                            "expiration_date": "2025-02-10T09:00:00Z",
                        }
                    ],
                    "workers": [
                        {
                            "uni": "xy123",
                            "first_name": "Grace",
                            "last_name": "Hopper",
                            "email": "grace.hopper@navy.mil",
                            "phone": "+1-202-555-0101",
                            "birth_date": "1906-12-09",
                            "addresses": [
                                {
                                    "id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                                    "street": "1701 E St NW",
                                    "city": "Washington",
                                    "state": "DC",
                                    "postal_code": "20552",
                                    "country": "USA",
                                }
                            ],
                        }
                    ]
                }
            ]
        }
    }
