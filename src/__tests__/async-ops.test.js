import { processBatch } from '../src/async-ops';

describe('batch processing', () => {
  test('processes all items', async () => {
    const items = [...Array(10).keys()];
    const batchPromises = items.map(item => processBatch(item));
    const results = await Promise.all(batchPromises);
    expect(results).toHaveLength(10);
  });
});