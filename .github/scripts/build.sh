# Transform jsx to js.
cd davidbieber.com-main
npx babel hugo/assets/js-src/ --out-dir hugo/assets/js/ --presets react-app/prod
parcel build --out-dir hugo/assets/js/ hugo/assets/js-src/margin-notes.js
npm run build
cd hugo
ls
# Generate the static site.
hugo
