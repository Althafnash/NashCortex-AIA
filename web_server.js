const http = require('http');

const port = 8000

const server = http.createServer((req,res)=>{
    try{    
        if (req.method === "GET") {
            if (req.url === "/") {
                res.writeHead(200 ,"Content-Type", "text/html");
                res.end("<h1>Hello World</h1>");
            }else if(req.url === "/about"){
                res.writeHead(200 ,"Content-Type", "text/html");
                res.end("<h1>About</h1>");
            }else {
                res.writeHead(404 ,"Content-Type", "text/html");
                res.end("<h1>NOT FOUND</h1>");
            }        
        }else {
            throw new Error("Method not allowed")            
        }
    }catch(error){
        res.writeHead(404 ,"Content-Type", "text/plain");
        res.end("Server Error");
    }
})

server.listen(port, () => {
    console.log(`Server is running on ${port}`);
});