ARG BUILD_FROM
FROM $BUILD_FROM

RUN \
    apk add --no-cache \
        git \
        openssh-client \
        py3-pip \
        python3 \
    && pip3 install \
        --no-cache-dir \
        --prefer-binary \
        ovh \
        requests

COPY run.py /
RUN chmod a+x /run.py

CMD [ "/run.py" ]
