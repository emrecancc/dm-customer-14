import request from 'supertest';
import app from '../app';

describe('API latency', () => {
  it('responds within 500ms', async () => {
    const start = Date.now();
    await request(app).get('/');
    const duration = Date.now() - start;
    expect(duration).toBeLessThan(500);
  });
});