const express = require('express');
const path = require('path');
const http = require('http');
const request = require('request');
const cors = require('cors');
const Joi = require('@hapi/joi');
require ('dotenv').config()

var bodyParser = require('body-parser');
var session = require('express-session');

//instantiate server
const app = express();
const port = process.env.PORT || 8080;
app.set('port', port);
const server = http.createServer(app);

//middleware
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname + '/public'));

//ejs
app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs');

// for session
app.use(session({
    secret: process.env.APP_SECRET,
    resave: true,
    saveUninitialized: true
}));
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

// Starts the server.
server.listen(port, function () {
    console.log(`Starting server on port ${port}`);
});

// Login page for host
app.get('/', (req, res) => {
    res.redirect('/login');
});

const USERNAME = 'brunonia'
const PASSWORD = 'Bluenforever123!'

// Login page for host
app.get('/login', (req, res) => {
    res.render('pages/login');
});

// Login page for host
app.post('/login', (req, res) => {
    const schema = Joi.object({
        username: Joi.string().max(100),
        password: Joi.string().max(100)
    });

    const { error, value } = schema.validate({ username: req.body.username, password: req.body.password });

    if (error || !isValidUsernameAndPassword(req.body.username, req.body.password)) {
        // res.status(422);
        res.json({
            isValid: false,
            message: 'invalid arguments'
        });
        res.end();
    } else {
        req.session.loggedin = true;
        res.json({
            isValid: true,
            message: 'valid arguments'
        });
    }
});

const isValidUsernameAndPassword = (username, password) => username === USERNAME && password === PASSWORD;


// user succesfully logged in
app.get('/secure-page', (req, res) => {
    if (req.session.loggedin){
        res.render('pages/secure');
    } else {
        res.redirect('/')
    }
});


// generates random word
app.get('/genword', (req, res) => {
    let keywords = 'projector pokemon iphone fitbit ipad ipod bananas apples nintendo pillow phone tv t-rex bus crayons water bottle pens pencils dog cornflakes alexa earbuds monitor socks sandals xylophone airpods ssd tablet chromebook backpack'.split(' ');
    word = keywords[Math.floor(Math.random() * keywords.length)];
    // if we wanted infinite words we could do so using this
    // request('https://random-word-api.herokuapp.com/word?number=1', (err, resp, body) => console.log(body));
    res.json({
        keyword: word
    });
})

