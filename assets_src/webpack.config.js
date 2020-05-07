const path = require('path');

module.exports = {
  entry: {
    'main': './assets_src/js/main.js',
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, '../core/static/js')
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ],
  },
  devtool: 'source-map',
};
