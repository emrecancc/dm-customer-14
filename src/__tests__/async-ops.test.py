import asyncio
import pytest
from app.service import process_batch

def test_batch_processing():
    results = []
    loop = asyncio.get_event_loop()
    async def run():
        tasks = [process_batch(i) for i in range(10)]
        results.extend(await asyncio.gather(*tasks))
    loop.run_until_complete(run())
    assert len(results) == 10  # Fails ~30% of the time
    assert all(r['status'] == 'done' for r in results)
