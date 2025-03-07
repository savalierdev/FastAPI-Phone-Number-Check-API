# Flask Phone Number Check API

A REST API for validating and checking information about phone numbers.

## Authentication

All API endpoints are secured using API Keys. To access the API, you need to include your API key in the request header:

```
X-API-Key: your-api-key-here
```

If you don't provide a valid API key, you'll receive a 403 Forbidden error.

## Endpoints

### Get Phone Information with Country Code

```
GET /phone/{phone_number}/{country}
```

Example:
```
GET /phone/5551234567/US
```

### Get Phone Information without Country Code

```
GET /phone/{phone_number}
```

Example:
```
GET /phone/15551234567
```

## Response Examples

### Valid Number Response

```json
{
  "message": "Başarılı!",
  "Bu Numara ISS Tarafından Kiralanabilir mi?": "Geçerli",
  "Telefon Numarası": "5551234567",
  "Numara Türü": "Mobil Hat",
  "ISP": "Some Carrier"
}
```

### Invalid Number Response

```json
{
  "message": "Böyle Bir Numara Bulunmuyor",
  "Böyle Bir Numara Olması Mümkün mü?": "Mümkün"
}
```

## API Documentation

Interactive API documentation is available at:

```
/api/documentation
```