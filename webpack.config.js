const path = require("path");

module.exports = {
  entry: "./js/main.js",
  output: {
    path: path.resolve(__dirname, "static/dist"),
    filename: "bundle.js",
  },
};
