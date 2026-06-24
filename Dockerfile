FROM node:10 AS node

ADD ./hugo /app/hugo

WORKDIR /app/hugo
# Install babel with React presets.
RUN npm install babel-cli@6 babel-preset-react-app@3
# Transform jsx to js.
RUN npx babel assets/js-src/ --out-dir assets/js/ --presets react-app/prod

# Install Hugo Extended (same version/source as .github/scripts/install.sh).
FROM debian:bookworm-slim as hugo
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && curl -LO https://github.com/gohugoio/hugo/releases/download/v0.163.3/hugo_extended_0.163.3_linux-amd64.deb \
    && dpkg -i hugo_extended_0.163.3_linux-amd64.deb \
    && rm hugo_extended_0.163.3_linux-amd64.deb \
    && apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*
COPY --from=node /app/hugo /app/hugo

WORKDIR /app/hugo
# Generate the static site.
RUN hugo

FROM python:2

COPY . /app
COPY --from=hugo /app/hugo/public /tmp/hugo-output

WORKDIR /app
RUN pip install -r requirements.txt

# Get files ready to serve.
RUN cp -r /tmp/hugo-output/* default/

EXPOSE 80
EXPOSE 443

CMD ["python", "app.py", "--no-ssl"]
