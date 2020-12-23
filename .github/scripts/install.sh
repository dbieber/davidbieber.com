curl -LO https://github.com/gohugoio/hugo/releases/download/v0.62.1/hugo_extended_0.62.1_Linux-64bit.deb
sudo dpkg -i hugo_extended_0.62.1_Linux-64bit.deb
rm hugo_extended_0.62.1_Linux-64bit.deb

# Install babel with React presets.
cd davidbieber.com-main
npm install
cat package.json
