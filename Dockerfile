FROM docker.artifactory.code.dodiis.mil/di-mars/mission-module/python39-nodejs14
RUN apk update && apk upgrade
RUN pip install fuzzywuzzy \
                python-Levenshtein
