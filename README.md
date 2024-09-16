# simplyask.io

## API URL and example:
```bash
curl -X POST http://127.0.0.1:5000/ask \
-H "Content-Type: application/json" \
-d '{
     "question": "About Dreamview Estates",
     "url": "https://dreamviewestates.co.uk/" 
}'
```


## Example JSON Request:

```bash
{
    "question": "About Dreamview Estates",
    "url": "https://dreamviewestates.co.uk/" 
}
```

## Example JSON Response:

```bash
{
  "answer": "Proudly Achieving Top Prices for residential properties by Dreamview Estates MURRAY LEE, possibly the most well known (and maybe even now the oldest!) North West London Estate Agent has been running Dreamview Estates at 34 Golders Green Road, NW11 8LL since Sept 2012. Certainly Murray, who is a Fell",
  "question": "About Dreamview Estates"
}
```