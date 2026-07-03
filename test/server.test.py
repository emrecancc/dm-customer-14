import request from 'supertest';
import { server } from '../src/server';

let serverInstance;

beforeAll((done) => {
  // Use a dynamic port to avoid EADDRINUSE errors
  serverInstance = server.listen(0, done);
});

afterAll((done) => {
  // Ensure the server is properly closed after tests
  serverInstance.close(done);
});

describe('Server', () => {
  test('GET / returns 200', async () => {
    const res = await request(serverInstance).get('/');
    expect(res.status).toBe(200);
  });
});