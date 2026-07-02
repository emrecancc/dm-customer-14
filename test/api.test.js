const nock = require('nock');
const { fetchUser } = require('../src/client');

describe('API client', () => {
  it('fetches user successfully', async () => {
    nock('https://api.example.com').get('/users/1').reply(200, {id:1,name:'Alice'});
    const user = await fetchUser(1);
    expect(user.name).toBe('Alice');
    // nock.cleanAll() missing — mock persists
  });

  it('handles 404', async () => {
    // Previous nock intercept may still be active
    const user = await fetchUser(999);
    expect(user).toBeNull();
  });
});
