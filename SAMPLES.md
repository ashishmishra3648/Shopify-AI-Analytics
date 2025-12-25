# Sample API Interactions

## Request
**Endpoint**: `POST http://localhost:3000/api/v1/queries`
**Headers**:
- `Content-Type: application/json`

**Body**:
```json
{
  "query": "How many units of Product A did I sell last week?"
}
```

## Response (Success)
**Status**: `200 OK`
**Body**:
```json
{
  "answer": "You sold 35 units of Product A last week.",
  "shopify_ql": "FROM sales SHOW sum(net_quantity) WHERE product_title = 'Product A' SINCE -7d UNTIL today",
  "data": {
    "rows": [["Product A", 35]]
  },
  "confidence": "high"
}
```

## Response (Internal Flow - Python Service)
The Rails app forwards the request to the Python service at `http://localhost:8000/analyze` with the shop credentials added.

**Internal Request**:
```json
{
  "query": "How many units of Product A did I sell last week?",
  "shop_domain": "my-shop.myshopify.com",
  "access_token": "shpua_..."
}
```
