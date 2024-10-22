const path = require("path");

module.exports = {
  entry: "./frontend/js/main.js",
  output: {
    path: path.resolve(__dirname, "frontend/static/dist"),
    filename: "bundle.js",
  },
};
