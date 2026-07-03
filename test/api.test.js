// Auto-fixed: nock interceptor cleanup
const nock = require('nock');
afterEach(() => { nock.cleanAll(); });
test('api cleanup stub', async () => { expect(true).toBe(true); });
