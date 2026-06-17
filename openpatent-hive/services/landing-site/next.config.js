/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  async rewrites() {
    return [
      // Proxy the public API through the same origin (avoids CORS)
      { source: '/api/v1/:path*', destination: `${process.env.PATENTMCP_API || 'http://api.openpatent.ai'}/v1/:path*` },
    ];
  },
};
module.exports = nextConfig;
