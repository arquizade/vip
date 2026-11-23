# Example Standard: API Conventions

## Naming
* Use lowercase, hyphenated route names: `/user-profiles`.
* Use plural nouns for collections.

## Errors
* Return JSON with `error`, `message`, and `request_id` fields.
* Use HTTP status codes that match the failure type.

## Retries
* Retry only idempotent requests.
* Use exponential backoff with jitter.
