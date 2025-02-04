const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello from Node.js Microservice!");
});

app.listen(5000, () => {
  console.log("Node.js service running on port 5000");
});
