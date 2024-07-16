$headers = @{
    "accept" = "application/json"
    "Content-Type" = "application/json"
}

$body = @{
    "username" = "admin"
    "password" = "A12345aa"
}

$response = Invoke-WebRequest -Uri http://localhost:5000/login -Method POST -Headers $headers -Body ($body | ConvertTo-Json)
$content = $response.Content | ConvertFrom-Json
$token = $content.access_token
$token