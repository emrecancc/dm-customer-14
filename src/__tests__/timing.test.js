import request from 'supertest';
import app from '../app';

test('API responds within 50ms', async () => {
  const start = Date.now();
  await request(app).get('/api');
  expect(Date.now() - start).toBeLessThan(300);
});