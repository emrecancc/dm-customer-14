const request = require('supertest');
const app = require('../app');

describe('API performance', () => {
  it('responds within 400ms', async () => {
    const start = Date.now();
    await request(app).get('/api/endpoint');
    const duration = Date.now() - start;
    expect(duration).toBeLessThan(400);
  });
});