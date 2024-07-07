# Запрос на защищенный маршрут
$protectedHeaders = @{
    "Authorization" = "Bearer $token"
}

$protectedResponse = Invoke-WebRequest -Uri http://localhost:5000/protected -Method GET -Headers $protectedHeaders
$protectedContent = $protectedResponse.Content
$protectedContent
