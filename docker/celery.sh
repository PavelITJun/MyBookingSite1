#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    celery --app=app.tasks.celery:celery worker -l INFO
if [[ "${1}" == "celery_beat" ]]; then
    celery --app=app.tasks.celery:celery worker -l INFO -B
elif [[ "${1}" == "flower" ]]; then
    celery --app=app.tasks.celery:celery flower
fi