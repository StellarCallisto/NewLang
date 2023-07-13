const express = require("express")
const app = express()
const path = require('path');
const port = 8888

// install guide:

// install node.js
// install visual studio code
// install git (bash)
// do "npm i express"
// do "npm i -g nodemon"

// test change

app.use(express.static(__dirname))

// pages
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, '/Homepage/page.html'))
})

app.get("/linktree", (req, res) => {
    res.sendFile(path.join(__dirname, '/Link-tree/page.html'))
})

app.get("/cultures", (req, res) => {
    res.sendFile(path.join(__dirname, '/Langs/page.html'))
})

// cultures
app.get("/cultures/maomao/:name", (req, res) => {
    res.sendFile(path.join(__dirname, '/Langs/Mãomaó/'+req.params.name+'.html'))
})
app.get("/cultures/axiria/:name", (req, res) => {
    res.sendFile(path.join(__dirname, '/Langs/Âxiria/'+req.params.name+'.html'))
})

// error 404
app.get('*', function(req, res){
    res.status(404).send("Error 404: Page Not Found. Redirect to base url")
});

// open server
app.listen(port)
console.log("Server Online on localhost:" + port)