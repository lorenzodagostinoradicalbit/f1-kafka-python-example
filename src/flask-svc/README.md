# Flask service

This is a GCLOUD Testing application

The flask service is going to be accessible only from other applications in the same gcloud project.

## What it does

This app should mount a bucket containing the data to be streamed to helicon and exposes 3 endpoints:

- `/`: return the actual readed data
- `/start`: start a new process that reads data ans update the actual data
- `/stop`: stop the process and reset actual data

## Needed ENV vars

In cloud RUN you need to set the following ENV variables:

- **BUCKET**: the gcs bucket name
- **LOG_NAME**: the filename inside the bucket
- **PORT**: *automatically set by gcloud*
- **STREAM_DATA**: if true uses ijson instead of json to optimize

## Build the image and push

Simply run `docker build -t <name> .`

Once builded you should give it a tag like the following:
```bash
docker tag <name> gcr.io/<gc-project-name>/<name>
docker push gcr.io/<gc-project-name>/<name>
```
