# Transform jsx to js.
cd davidbieber.com-main
npx babel hugo/assets/js-src/ --out-dir hugo/assets/js/ --presets react-app/prod
cd hugo
ls
# Generate the static site.
hugo
