# Install Hugo (Extended).
# Pinned to the EXACT version tested locally — do NOT use 'latest', so the deploy
# build can't silently break on a future Hugo release. Bump in one place here.
HUGO_VERSION="0.163.3"
curl -LO "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
sudo dpkg -i "hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
rm "hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
# Fail the build loudly if the installed Hugo isn't the pinned version.
hugo version | grep -q "v${HUGO_VERSION}" || { echo "ERROR: expected Hugo v${HUGO_VERSION}, got:"; hugo version; exit 1; }

# Install babel with React presets.
cd davidbieber.com-main
npm install
cat package.json


# On macOS, install Hugo Extended via Homebrew (recent releases no longer ship a
# macOS tar.gz; only a darwin-universal .pkg). `brew install hugo` is the extended build.
#   brew install hugo
# Or download the installer package:
#   curl -LO https://github.com/gohugoio/hugo/releases/download/v0.163.3/hugo_extended_0.163.3_darwin-universal.pkg