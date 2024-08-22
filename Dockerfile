ARG MY_IMAGE
#FROM docker.artifactory.code.dodiis.mil/di-mars/mission-module/python39-nodejs14
FROM ${MY_IMAGE}
WORKDIR /opt
COPY . .
RUN apk update && apk upgrade
RUN apk add py3-pip
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
RUN pip3 install fuzzywuzzy \
                python-Levenshtein
