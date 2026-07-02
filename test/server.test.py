import { server } from '../server';
import request from 'supertest';

beforeAll(() => {
  server.listen(3059);
});

afterAll(() => {
  server.close();
});

describe('API tests', () => {
  test('GET /', async () => {
    const res = await request(server).get('/');
    expect(res.status).toBe(200);
  });
});