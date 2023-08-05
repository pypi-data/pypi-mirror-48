# from tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8
FROM tiangolo/uwsgi-nginx:python3.6-alpine3.9

LABEL maintainer="poipoii <earth.sama@gmail.com>"

ENV WKHTMLTOIMAGE /usr/bin/wkhtmltoimage

# Install wkhtmltopdf
RUN apk --update add --no-cache \
            xvfb \
            wkhtmltopdf \
            # Additionnal dependencies for better rendering
            ttf-freefont \
            fontconfig \
            dbus \
    && \
    # Wrapper for xvfb
    mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf-origin && \
    echo $'#!/usr/bin/env sh\n\
Xvfb :0 -screen 0 1024x768x24 -ac +extension GLX +render -noreset & \n\
DISPLAY=:0.0 wkhtmltopdf-origin $@ \n\
killall Xvfb\
' > /usr/bin/wkhtmltopdf && \
    chmod +x /usr/bin/wkhtmltopdf

# Install eml2png
RUN apk update; \
    apk add --no-cache git && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools flask && \
    pip install git+git://github.com/poipoii/eml2png.git#egg=eml2png && \
    rm -r /root/.cache

# URL under which static (not modified by Python) files will be requested
# They will be served by Nginx directly, without being handled by uWSGI
ENV STATIC_URL /static
# Absolute path in where the static files wil be
ENV STATIC_PATH /app/static

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
# ENV STATIC_INDEX 1
ENV STATIC_INDEX 0

# Add demo app
COPY ./docker/app /app
WORKDIR /app

# Make /app/* available to be imported by Python globally to better support several use cases like Alembic migrations.
ENV PYTHONPATH=/app

# Move the base entrypoint to reuse it
RUN mv /entrypoint.sh /uwsgi-nginx-entrypoint.sh
# Copy the entrypoint that will generate Nginx additional configs
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Run the start script provided by the parent image tiangolo/uwsgi-nginx.
# It will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["/start.sh"]

