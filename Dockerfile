FROM alpine:3.6
MAINTAINER Ondrej Nanka "nankaond@cvut.cz"
ENV LANG C.UTF-8
ENV MAXLEN 500
ENV TIMEOUT 5
ENV SENTRY_DSN https://e02a5779e6484938856a095a23b6aeee:cb712522e68d4b37ab36d13924f139ea@sentry.fit.cvut.cz/27
ENV WHITELIST ^ěščřžýáíéóúůďťňĎŇŤŠČŘŽÝÁÍÉÚŮABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*+.,()<>=/ {}-
#ENV WHITELIST .*
ENV FLASK_APP=pyrest
ENV FLASK_DEBUG=true
RUN apk add --no-cache py-gunicorn python curl && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "pyrest:app"]
#CMD ["flask", "run", "--host=0.0.0.0"]
