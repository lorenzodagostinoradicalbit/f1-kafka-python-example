# Node app

This is just an example. This service should be private and callable by anyone.

## Needed envs:

- **PORT**: automaticlly set by google
- **FLASK_SVC**: flask service url

## Build

imply run `docker build -t <name> .`

Once builded you should give it a tag like the following:
```bash
docker tag <name> gcr.io/<gc-project-name>/<name>
docker push gcr.io/<gc-project-name>/<name>
```