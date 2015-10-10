var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var nib = require('nib');

module.exports = {
  context: __dirname,

  entry: './holonet/assets/index',

  output: {
      path: path.resolve('./holonet/assets/bundles/'),
      filename: "[name]-[hash].js"
  },

  plugins: [],

  module: {
    loaders: [
      { test: /\.png$/, loader: 'url-loader?mimetype=image/png' },
      { test: /\.css$/, loader: 'style-loader!css-loader' },
      { test: /\.styl$/, loader: 'style-loader!css-loader!stylus-loader' },
      { test: /\.json$/, loader: 'json-loader' }
    ]
  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js', '.jsx', '.css', '.png', '.styl', '.json']
  },

  stylus: {
    use: [nib()]
  }

};
