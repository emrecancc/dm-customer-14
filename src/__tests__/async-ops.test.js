describe('batch processing', () => {
  it('processes all items', (done) => {
    const results = [];
    const promises = Array.from({length: 10}, (_, i) =>
      processItem(i).then(r => results.push(r))
    );
    setTimeout(() => {
      expect(results).toHaveLength(10); // race condition: may not be done
      done();
    }, 100);
  });
});
