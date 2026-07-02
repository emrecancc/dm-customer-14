const { User } = require('../src/models');
const sequelize = require('../src/database');

describe('User model', () => {
  beforeAll(async () => {
    await sequelize.sync({ force: true });
  });

  beforeEach(async () => {
    await User.destroy({ where: {}, truncate: true });
  });

  test('creates a user', async () => {
    const user = await User.create({ name: 'Alice' });
    expect(user.name).toBe('Alice');
  });

  test('starts with empty database', async () => {
    const count = await User.count();
    expect(count).toBe(0);
  });
});