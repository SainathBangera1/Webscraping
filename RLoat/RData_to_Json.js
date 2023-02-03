// (Buffer.from(base64data, "base64").toString("ascii"))
const fs = require("fs");
let objData;
try {
  const data = fs.readFileSync("./RLoat/R_Database64.txt", "utf8");
  objData = Buffer.from(data, "base64").toString("ascii");

  fs.writeFile("./RLoat/RData.json", objData, (err) => {
    if (err) {
      console.error(err);
    }
    // file written successfully
  });

  console.log("Done writing Json file...");
} catch (err) {
  console.error(err);
}
