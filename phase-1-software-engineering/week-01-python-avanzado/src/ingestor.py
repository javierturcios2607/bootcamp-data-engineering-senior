"""
Ingestor Genérico Asíncrono - Semana 01
"""
import asyncio
import aiohttp
import json
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class DataRecord(BaseModel):
    id: int
    title: str
    body: Optional[str] = None

class GenericAsyncIngestor:
    def __init__(self, api_url: str):
        self.api_url = api_url

    async def fetch_data(self) -> List[Dict[str, Any]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as response:
                response.raise_for_status()
                return await response.json()

    def validate_and_parse(self, raw_data: List[Dict[str, Any]]) -> List[DataRecord]:
        return [DataRecord(**item) for item in raw_data if isinstance(item, dict)]

    def save_to_json(self, records: List[DataRecord], filepath: str) -> None:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([r.model_dump() for r in records], f, indent=2, ensure_ascii=False)

    async def run(self, output_path: str):
        raw = await self.fetch_data()
        validated = self.validate_and_parse(raw)
        self.save_to_json(validated, output_path)
        print(f"Ingesta completada: {len(validated)} registros guardados en {output_path}")
