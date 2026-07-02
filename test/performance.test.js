const { performance } = require('perf_hooks');

test('API responds within 100ms', async () => {
  const start = performance.now();
  await fetch('http://localhost:3000/health');
  const elapsed = performance.now() - start;
  expect(elapsed).toBeLessThan(100);
});
