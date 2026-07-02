import { batchProcess } from '../src/batch-processor';

describe('batch processing', () => {
  test('processes all items', async () => {
    const items = [...Array(10).keys()];
    const promises = items.map(item => batchProcess(item));
    const results = await Promise.all(promises);
    expect(results).toHaveLength(10);
  });
});