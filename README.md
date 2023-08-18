# MedTextAPI

Deploy the app locally:

```bash
uvicorn app:app
```

You can send a medical text to the API through typing the following in your browser if deployed locally:

```
http://127.0.0.1:8000/extract_entities/?t=The patient suffers from diabetes since 6 years.
```

Or with the following URL if using the deployed API on [healthuniverse.com](https://www.healthuniverse.com)

```
http://127.0.0.1:8000/extract_entities/?t=The patient suffers from diabetes since 6 years.
```

This will return the following entities:

`{"entities":[[0,"Disease_disorder","diabetes"],[1,"Duration","6"]]}`
