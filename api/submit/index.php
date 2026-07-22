<?php
// Set CORS headers to prevent issues across domains/localhost
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");
header("Content-Type: application/json");

// Handle preflight OPTIONS request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit(0);
}

// Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(["error" => "Method not allowed"]);
    exit;
}

// Get the raw POST data
$rawPayload = file_get_contents("php://input");

// Decode the Discord Webhook URL securely on the server
$encoded = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTQ4OTI4MTM3MzIzNDY1OTMzOC9ZazJ2WkJFUUpqRVYycEdwR045Z05uUzVRaDFBcml4OVNaSk0tSUltVnNvZ0Zpc1d5c0lGMHQyMTlTbkI3NW9kMGRsUQ==";
$webhookUrl = base64_decode($encoded);

if (!$webhookUrl) {
    http_response_code(500);
    echo json_encode(["error" => "Configuration error: Failed to decode target URL"]);
    exit;
}

// Initialize cURL to forward payload to Discord
$ch = curl_init($webhookUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $rawPayload);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) BraandSchoolLeadsProxy/1.0'
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Output matching success/error status to frontend
if ($httpCode >= 200 && $httpCode < 300) {
    echo json_encode(["success" => true]);
} else {
    http_response_code($httpCode ?: 500);
    echo json_encode([
        "error" => "Failed to forward payload to Discord",
        "code" => $httpCode,
        "details" => $response
    ]);
}
?>
