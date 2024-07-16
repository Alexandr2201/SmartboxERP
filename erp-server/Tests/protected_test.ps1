$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8
# Замените YOUR_TOKEN на ваш фактический JWT токен
$token

# Формируем заголовок Authorization
$headers = @{
    "Authorization" = "Bearer $token"
    "accept" = "application/json"
}
$headers

# URL защищенного маршрута
$url = "http://localhost:5000/protected"

# Выводим на экран информацию о запросе
Write-Output "Выполняем GET запрос на $url с заголовком Authorization: Bearer $token"

# Выполняем запрос на защищенный маршрут
$protectedResponse = Invoke-WebRequest -Uri $url -Method GET -Headers $headers

# Выводим содержимое ответа
$protectedContent = $protectedResponse.Content
Write-Output $protectedContent