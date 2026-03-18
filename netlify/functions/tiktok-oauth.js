const https = require('https');
const querystring = require('querystring');

const CLIENT_KEY = 'awyugert3kqgusxc';
const CLIENT_SECRET = 'IYoPmIotMHhc37pswoG8HNQSftMtM9bC';
const REDIRECT_URI = 'https://virtuevigil.com/tiktok/callback';

exports.handler = async (event) => {
  const params = event.queryStringParameters || {};
  const action = params.action;

  // Authorize — redirect to TikTok
  if (action === 'authorize') {
    const state = Math.random().toString(36).substring(2);
    const authUrl = `https://www.tiktok.com/v2/auth/authorize/?client_key=${CLIENT_KEY}&scope=video.upload,video.publish,user.info.basic&response_type=code&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&state=${state}`;
    return { statusCode: 302, headers: { Location: authUrl }, body: '' };
  }

  // Callback — exchange code for token
  if (action === 'callback') {
    const { code, error } = params;
    if (error || !code) {
      return { statusCode: 302, headers: { Location: '/tiktok/?error=' + (error || 'no_code') }, body: '' };
    }
    try {
      const tokenData = await postRequest(
        'https://open.tiktokapis.com/v2/oauth/token/',
        querystring.stringify({
          client_key: CLIENT_KEY,
          client_secret: CLIENT_SECRET,
          code,
          grant_type: 'authorization_code',
          redirect_uri: REDIRECT_URI
        }),
        { 'Content-Type': 'application/x-www-form-urlencoded' }
      );
      const token = tokenData.access_token;
      const openId = tokenData.open_id;
      return {
        statusCode: 302,
        headers: { Location: `/tiktok/?connected=1&open_id=${openId}&token_preview=${token ? token.substring(0,8) : 'none'}` },
        body: ''
      };
    } catch (e) {
      return { statusCode: 302, headers: { Location: '/tiktok/?error=token_exchange_failed' }, body: '' };
    }
  }

  return { statusCode: 404, body: 'Unknown action' };
};

function postRequest(url, body, headers) {
  return new Promise((resolve, reject) => {
    const urlObj = new URL(url);
    const options = {
      hostname: urlObj.hostname,
      path: urlObj.pathname,
      method: 'POST',
      headers: { ...headers, 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => { try { resolve(JSON.parse(data)); } catch(e) { reject(e); } });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}
