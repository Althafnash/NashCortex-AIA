import http from 'http';
import fs from 'fs/promises';
import url from 'url';
import path from 'path';

const port = process.env.PORT || 8000;  

const __filename = url.fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

console.log("Directory:", __dirname);
console.log("File:", __filename);

const server = http.createServer(async (req, res) => {
    try {
        let filepath;

        console.log(`Incoming request for: ${req.url}`);

        if (req.method === "GET") {
            if (req.url === "/") {
                filepath = path.join(__dirname, 'WebServerContent', 'Home.html');
            } else if (req.url === "/commands") {
                filepath = path.join(__dirname, 'WebServerContent', 'commands.html');
            } else {
                res.writeHead(404, { "Content-Type": "text/plain" });
                return res.end("404 - Page Not Found");
            }

            console.log(`Serving file: ${filepath}`);

            const data = await fs.readFile(filepath);

            res.setHeader("Content-Type", "text/html");
            res.writeHead(200);  
            res.end(data);
        } else {
            res.writeHead(405, { "Content-Type": "text/plain" });
            res.end("405 - Method Not Allowed");
        }

    } catch (error) {
        console.error(`Error serving file: ${error.message}`);

        res.writeHead(500, { "Content-Type": "text/plain" });
        res.end("500 - Internal Server Error: " + error.message);
    }
});

server.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
