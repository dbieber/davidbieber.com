const path = require('path');
const fs = require('fs');

function findJsxFiles(dir) {
    let jsFiles = [];
    if (!fs.existsSync(dir)) return jsFiles;
    
    const files = fs.readdirSync(dir, { withFileTypes: true });
    
    files.forEach(file => {
        const fullPath = path.join(dir, file.name);
        if (file.isDirectory()) {
            jsFiles = jsFiles.concat(findJsxFiles(fullPath));
        } else if (file.name.endsWith('.jsx') || file.name.endsWith('.js')) {
            // Store the relative path from project root
            jsFiles.push('./' + path.relative('.', fullPath));
        }
    });
    
    return jsFiles;
}

function generateEntries() {
    const entries = {};
    const contentDir = './hugo/content/snippets';
    
    if (!fs.existsSync(contentDir)) {
        console.log(`Content directory ${contentDir} not found`);
        return entries;
    }

    const snippetDirs = fs.readdirSync(contentDir, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory())
        .map(dirent => dirent.name);

    snippetDirs.forEach(snippetDir => {
        const fullPath = path.join(contentDir, snippetDir);
        const jsFiles = findJsxFiles(fullPath);
        
        if (jsFiles.length > 0) {
            // Each snippet directory becomes an entry point
            entries[snippetDir] = jsFiles;
            console.log(`Entry ${snippetDir}:`, jsFiles);
        }
    });

    return entries;
}

module.exports = {
    entry: generateEntries(),
    output: {
        path: path.resolve(__dirname, 'hugo/assets/js'),
        filename: '[name].bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-react']
                    }
                }
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    }
};
