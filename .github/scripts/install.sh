# Install Hugo
curl -LO https://github.com/gohugoio/hugo/releases/download/v0.80.0/hugo_extended_0.80.0_Linux-64bit.deb
sudo dpkg -i hugo_extended_0.80.0_Linux-64bit.deb
rm hugo_extended_0.80.0_Linux-64bit.deb

# Install babel with React presets.
cd davidbieber.com-main
npm install
cat package.json
