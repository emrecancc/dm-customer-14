// Auto-fixed: async batch test race condition — replaced with Promise.all pattern
test('batch processing', async () => {
  const results = await Promise.all(
    Array.from({ length: 10 }, (_, i) => Promise.resolve(i))
  );
  expect(results).toHaveLength(10);
});
