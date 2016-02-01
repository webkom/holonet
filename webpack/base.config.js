var path = require("path");
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var nib = require('nib');

module.exports = {
  context: __dirname,

  entry: {
    'app': '../holonet/frontend/index',
    'vendor': [
      'normalize.css',
      'bulma/css/bulma.css'
    ]
  },

  output: {
      path: path.resolve('../holonet/assets/bundles/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
    new webpack.optimize.DedupePlugin(),
    new webpack.ProvidePlugin({
    }),
    new ExtractTextPlugin('[name]-[hash].css')
  ],

  module: {
    loaders: [
      { test: /\.css$/, loader: ExtractTextPlugin.extract('style-loader', 'css-loader') },
      { test: /\.styl$/, loader: ExtractTextPlugin.extract('style-loader', 'css-loader!stylus-loader') },
      { test: /\.less$/, loader: ExtractTextPlugin.extract('style-loader', 'css-loader!less-loader') },
      { test: /\.json$/, loader: 'json-loader' },
      { test: /\.(otf|eot|svg|ttf|woff|woff2|png|jpg|jpeg|svg)(\?.+)?$/, loader: 'file-loader?name=' + '[name].[ext]' }
    ]
  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js', '.jsx', '.css', '.png', '.styl', '.json', '.jpg', '.jpeg', '.sass']
  },

  stylus: {
    use: [nib()]
  }

};
