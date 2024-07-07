# Получение токена
$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "username" = "user"
    "password" = "D12345dd"
}

$response = Invoke-WebRequest -Uri http://localhost:5000/login -Method POST -Headers $headers -Body ($body | ConvertTo-Json)
$content = $response.Content | ConvertFrom-Json
$token = $content.access_token

$token