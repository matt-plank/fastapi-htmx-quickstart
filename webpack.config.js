const path = require("path");

module.exports = {
  entry: "./frontend/js/main.ts",
  output: {
    path: path.resolve(__dirname, "frontend/static/dist"),
    filename: "bundle.js",
  },
  resolve: {
    extensions: [".ts", ".js"],
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
};
