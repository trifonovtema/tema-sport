FROM certbot/certbot:latest

COPY ./certbot/renew/cert-renew-crontab /etc/crontabs

# load crontab file
RUN crontab /etc/crontabs/cert-renew-crontab

# run cron in foreground
ENTRYPOINT ["crond", "-f"]