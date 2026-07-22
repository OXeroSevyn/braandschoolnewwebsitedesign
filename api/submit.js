export default async function handler(request, response) {
  // Add CORS headers
  response.setHeader('Access-Control-Allow-Credentials', true);
  response.setHeader('Access-Control-Allow-Origin', '*');
  response.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  response.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  // Handle preflight OPTIONS request
  if (request.method === 'OPTIONS') {
    return response.status(200).end();
  }

  if (request.method !== 'POST') {
    return response.status(405).json({ error: 'Method not allowed' });
  }

  // Fallback to the default webhook URL if environment variable is not defined in Vercel settings
  const webhookUrl = process.env.DISCORD_WEBHOOK_URL || Buffer.from("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTQ4OTI4MTM3MzIzNDY1OTMzOC9ZazJ2WkJFUUpqRVYycEdwR045Z05uUzVRaDFBcml4OVNaSk0tSUltVnNvZ0Zpc1d5c0lGMHQyMTlTbkI3NW9kMGRsUQ==", 'base64').toString('ascii');

  try {
    const res = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(request.body)
    });

    if (res.ok) {
      return response.status(200).json({ success: true });
    } else {
      const text = await res.text();
      return response.status(res.status).json({ error: text });
    }
  } catch (error) {
    return response.status(500).json({ error: error.message });
  }
}
