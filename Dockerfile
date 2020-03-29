FROM node:10 AS build

ADD . /app

WORKDIR /build
RUN curl -LO https://github.com/gohugoio/hugo/releases/download/v0.62.1/hugo_extended_0.62.1_Linux-64bit.deb
RUN dpkg -i hugo_extended_0.62.1_Linux-64bit.deb
RUN rm hugo_extended_0.62.1_Linux-64bit.deb

WORKDIR /app/hugo
# Install babel with React presets.
RUN npm install babel-cli@6 babel-preset-react-app@3
# Transform jsx to js.
RUN npx babel assets/js-src/ --out-dir assets/js/ --presets react-app/prod
# Generate the static site.
RUN hugo

FROM python:2
COPY --from=build /app /app

WORKDIR /app
RUN pip install -r requirements.txt

# Get files ready to serve.
RUN cp -r hugo/public/* default/

EXPOSE 80
EXPOSE 443

CMD ["python", "app.py", "--no-ssl"]
