FROM node:10 AS node

ADD ./hugo /app/hugo

WORKDIR /app/hugo
# Install babel with React presets.
RUN npm install babel-cli@6 babel-preset-react-app@3
# Transform jsx to js.
RUN npx babel assets/js-src/ --out-dir assets/js/ --presets react-app/prod

FROM peaceiris/hugo:v0.62.1 as hugo
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
