import request from 'supertest';
import app from '../src/app';

describe('API responds within 450ms', () => {
  it('should respond within 450ms', async () => {
    const start = Date.now();
    await request(app).get('/health');
    const duration = Date.now() - start;
    expect(duration).toBeLessThan(450);
  });
});