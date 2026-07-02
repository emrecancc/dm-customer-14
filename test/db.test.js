const { User } = require('../src/models');
const sequelize = require('../src/db');

describe('User model', () => {
  beforeEach(() => User.destroy({ where: {}, truncate: true }));

  it('creates a user', async () => {
    const user = await User.create({ name: 'John' });
    expect(user).toBeDefined();
  });

  it('starts with empty database', async () => {
    const count = await User.count();
    expect(count).toBe(0);
  });
});
