function Invoke-PostRequest {
    param (
        [string]$Url
    )

    try {
        $response = Invoke-WebRequest -Uri $Url -Method POST
        Write-Output "POST request to $Url successful. Response: $($response.StatusCode)"
    } catch {
        Write-Error "POST request to $Url failed: $_"
    }
}

# Replace 'http://example.com' with your actual URL
$url = 'http://example.com'
Invoke-PostRequest -Url $url
