const config = {
  port: process.env.PORT || 3000,
  nextauth_secret: process.env.NEXTAUTH_SECRET, // required but not set in CI
  nodeEnv: process.env.NODE_ENV || 'development',
};

if (!config.nextauth_secret) {
  throw new Error('NEXTAUTH_SECRET environment variable is required but not set.');
}

module.exports = config;
